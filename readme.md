# Fine Arts Junior Review

Process Informer report into CSV fit for an EQUELLA taxonomy, upload to the appropriate taxonomy. The process looks like:

- download CSV (column headers on) from Informer report "LIB - EP - Library - Fine Arts Junior Review Students"
- run `python fajr-process.py data/informer.csv > taxo.csv` (where 1st argument is the Informer CSV)
- run `./upload.sh` (no arguments) to upload to EQUELLA, it expects a "taxo.csv" file
- afterwards the upload script will archive CSVs in a "data" directory
