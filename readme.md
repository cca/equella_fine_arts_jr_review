# Fine Arts Junior Review

Process an Informer report into a CSV fit for an EQUELLA taxonomy, upload to the appropriate taxonomy. The process looks like:

- download CSV (column headers on) from Informer report "[LIB - EP - Library - Fine Arts Junior Review Students](https://vm-informer-01.cca.edu/informer/?locale=en_US#action=ReportRun&reportId=79626253&launch=false)" & name it fajr.csv
- run `./fajr-process.py fajr.csv` (1st argument is the Informer CSV)
- this automatically adds usernames to the EQUELLA "FA JR exhibit students" group & generates a taxonomy CSV named "taxo.csv"
- run `./upload.sh` (no arguments) to upload the taxonomy to EQUELLA, it expects the "taxo.csv" file
- afterwards the upload script will offer to archive fajr.csv & taxo.csv in a "data" directory

The "fajr-process.py" script relies on a configured ".equellarc" file (see [equella-cli](https://github.com/cca/equella_cli) for details on that) with a configured OAuth token in your user's home directory, while the upload.sh script relies on the `uptaxo` abstraction over EQUELLA's command-line tools for updating taxonomies.

# LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
