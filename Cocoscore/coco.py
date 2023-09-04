import cocoscore.ml.fasttext_helpers as fth
import cocoscore.tools.data_tools as dt
import oss

import fasttext

model_path = 'demo.ftz'
dataset_path = 'demo.tsv'
sentences_path = 'sentences.txt'
fasttext_path = 'fasttext'
prob_path = 'probabilities.txt.gz'
scored_dataset_path = 'demo_scored.tsv'

fth.fasttext_predict(model_path, sentences_path, fasttext_path, prob_path)
probabilities = fth.load_fasttext_class_probabilities(prob_path)

df = dt.load_data_frame(dataset_path, class_labels=False)
df['predicted'] = probabilities
with open(scored_dataset_path, 'wt') as test_out:
    df.to_csv(test_out, sep='\t', header=False, index=False,
                   columns=['pmid', 'paragraph', 'sentence', 'entity1', 'entity2', 'predicted'])
                   
os.remove(prob_path) # remove intermediary class probabilities file
