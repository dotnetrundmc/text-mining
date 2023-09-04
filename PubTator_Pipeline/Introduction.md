**Required input:** `PMID` (pubmed_Id's)

# Changelog (after Michael's code) V1

1. Merged test and train into one dataset.
2. Checked if we can give more than 100 through the GET method. I tried with 1000 and it worked for me, but it takes 3 minutes for every 100 requests. I did not time how long it took for 1000, but it's definitely less than 30 minutes.
3. Created a dictionary to store output (Key: Concept_name, Value: Pubmed_id's) - created a condition for the PubMed ID to be added to the list of values if it's not already present in the list for a given concept name.
4. Encapsulated the code in the "fetch_pubmed_concepts" function to be used recursively. It takes your DataFrame "df" and an optional parameter "max_pmid_count" to specify the maximum number of PMIDs you want to process. It returns the dictionary as the result.

## PubTator Pipeline V2 Change Log

Key functionalities of the PubTator pipeline version 2:

### Data Loading
- Loads Gene-Disease dataset from Figshare and combines test/train files.
- Reads data into a pandas DataFrame.

### PubTator API
- Queries PubTator API to fetch gene annotations for PMIDs.
- The API accepts a list of PMIDs and concepts like "gene".
- Makes requests in a loop for each PMID.
- Parses XML response to extract gene info.

Key highlights are:

- Loading and combining external dataset.
- Interacting with PubTator API to annotate entities.
- Storing annotations in a DataFrame structure.
- Analyzing annotations to find interactions.
- Outputting results to a file.
- Includes improvements like progress tracking and error handling.

### Change Log after V1 to V2

### Data Storage
- Stores gene annotations in a DataFrame.
- Contains columns for gene ID, name, PMID, and type.
- Handles multiple annotations per PMID.

### Post-Processing
- Finds gene-gene interactions by mapping PMIDs to concepts.
- Outputs interactions to a text file.

### Visualization
- Exploring suitable tools to visualize large network maps (underway...).

### Enhancements
- Added a progress bar to track API requests.
- Handles API errors and failures.
- Improved data structures for faster lookups.
- Added file output for analysis.
