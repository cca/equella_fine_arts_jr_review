# Fine Arts Junior Review

Process Informer report into CSV fit for an EQUELLA taxonomy, upload to the appropriate taxonomy. The process looks like:

- download CSV (column headers on) from Informer report "LIB - EP - Library - Fine Arts Junior Review Students"
- run `python fajr-process.py` passing the CSV as an argument
- run `./upload.sh` (no arguments) to upload to EQUELLA

