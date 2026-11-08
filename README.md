# Identifying authors by gender in the Austrian National Library (ONB)

Scripts and dataset to extract records of translated fiction in the ONB's collection with gender labels added from GND.

Includes frequency counts and visualizations for gender ratios and most translated women writers.

Presented at the ONBLabs symposium, November 9th 2026.

# Dataset

Bibliographic entries have been collected as MARC21 files, transformed into tables.

- Timeframe (publishing year): 1858-2026.

- Date extracted: 21.10.2026

- Scope: All translations of German fiction (all editions that have German marked as an original language, meaning the language of the original text, MARC field #41). How many translations have been collected by the ONB is not known. Data has been extracted in batches of 10.000 (limit by the ONB).

Datasets from SRU search query (CSV):
**LT_131026_onb_request_after2013_xmlresults.csv**
**LT_131026_onb_request_before2013_xmlresults.csv**

# Data enrichment with GND's gender labels

The tables from from SRU search query were imported and merged in OpenRefine. Via Reconciliation, the GND's gender labels have been added by matching author_id.

The final dataset with gender labels: 
**LT-301026-onb-request-reconciled.csv**

# Folders

## onb_extract
ipynb scripts for extracting bibliographic entries via SRU, including the resulting MARC files and tables.

## results
frequency tables and figures for gender data.

# How-to use this repository
Scripts work with Python version 3.14.7.
Install all dependencies first, then run:

1. Extract bibliographic entries via SRU:
  Run 1_onb_request.ipynb
  This will give you: LT_131026_onb_request_after2013_xmlresults.xml
  LT_131026_onb_request_before2013_xmlresults.xml

2. Get the desired fields from MARC (author name, author ID, title, year, language, ISBNs) and transform to a CSV:
   Run 2_onb_gender_export.py
   This willl give you: LT_131026_onb_request_after2013_xmlresults.csv
   LT_131026_onb_request_before2013_xmlresults.csv

4. Import both tables into OpenRefine and do the following transformations:

   <img width="299" height="266" alt="Screenshot 2026-11-08 at 13 53 41" src="https://github.com/user-attachments/assets/3acf9963-b9cc-4f13-824e-c1008077872d" />

   Export the table as CSV. This will give you: LT-301026-onb-request-reconciled.csv

6. Run descriptive statistics and get visualizations:
Run 3_onb_gender_stats.ipynb

# License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
