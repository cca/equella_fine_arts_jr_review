# Fine Arts Junior Review

Process Informer report into CSV fit for an EQUELLA taxonomy, upload to the appropriate taxonomy. The process looks like:

- download CSV (column headers on) from Informer report "[LIB - EP - Library - Fine Arts Junior Review Students](https://vm-informer-01.cca.edu/informer/?locale=en_US#action=ReportRun&reportId=79626253&launch=false)" & name it fajr.csv
- run `./fajr-process.py fajr.csv` (1st argument is the Informer CSV)
- this automatically adds usernames to the EQUELLA "FA JR exhibit students" group & generates a taxonomy CSV named "taxo.csv"
- run `./upload.sh` (no arguments) to upload the taxonomy to EQUELLA, it expects the "taxo.csv" file
- afterwards the upload script will offer to archive fajr.csv & taxo.csv in a "data" directory
- for Animation/Film students, I usually run updates within a Python shell like:

```python
from fajr_group import *
users = [ 'one', 'two' ] # paste in all the usernames after formatting as a list
add_to_fajr_group(users, anima=True)
```

The "fajr-process.py" script relies on the included `uptaxo` script which in turn is a wrapper around EQUELLA's UploadTaxonomy.py (included in the integration package) as well as a configured ".equellarc" file (see [equella-cli](https://github.com/cca/equella_cli) for details on that).

# LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
