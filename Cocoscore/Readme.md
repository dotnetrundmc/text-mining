**Required input:** `PMID` (pubmed_Id's)

# Cocoscore demo model
coco.py contains a few paths and points to a few files:
- model_path. Model used for cocoscore. Model used here was found at: https://figshare.com/ndownloader/files/13252745. (~780MB)
- This is the only file you (should need to download)
- dataset_path: has the following columns, file contains pmid, paragraph number, first co-mentioned entity, second co-mentioned entity, text co-mentioning the entities
- fasttext_path: points to the location of fasttext. Install to the folder of which your files are in i.e. /fasttext
- prob_path: probabilities. Haven't used this file and it seems to run without it...
- scored_dataset_path: where the scored dataset will be saved

### output of file
tab delimited file with the following columns:
- pmid
- paragraph number
- sentence number
- first co-mentioned entity
- second co-mentiond entity
- probabilities of the entities






