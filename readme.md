# Fine Arts Junior Review

Process Informer report into CSV fit for an EQUELLA taxonomy, upload to the appropriate taxonomy. The process looks like:

- download CSV (column headers on) from Informer report "[LIB - EP - Library - Fine Arts Junior Review Students](https://vm-informer-01.cca.edu/informer/?locale=en_US#action=ReportRun&reportId=79626253&launch=false)" & name it fajr.csv
- run `./fajr-process.py fajr.csv > taxo.csv` (1st argument is the Informer CSV)
- run `./upload.sh` (no arguments) to upload to EQUELLA, it expects a "taxo.csv" file
- afterwards the upload script will archive fajr.csv and taxo.csv in a "data" directory

Relies on the included `uptaxo` script which is a wrapper around EQUELLA's UploadTaxonomy.py (included in the integration package) as well as a configured ".equellarc" file (see [equella-cli](https://github.com/cca/equella_cli) for details on that).

# LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
