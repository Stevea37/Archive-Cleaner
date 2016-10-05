# Archive-Cleaner
Clean up backup archives

THIS SCRIPT DELETES BACKUP FILES TO INCREASE THE INTERVAL BETWEEN DATA SNAPSHOTS, FOR SPACE SAVING PURPOSES.

$ python cleaner.py --help
usage: cleaner.py [-h] -p ROOT_PATH -o [OPTIONS [OPTIONS ...]]

Cleans up old backups to leave more room on the backup server.

E.g. python cleaner.py -p /path/to/archive -o 3:4 7:7.

The example provided will keep an archive from every 4th day if it's more than 3 days old and archive every 7 days if it's more than a week old.

The format of backups this script takes is BACKUP_SET-VERSION.

optional arguments:
  -h, --help            show this help message and exit
  -p ROOT_PATH, --root-path ROOT_PATH
                        The root path of your backups.
  -o [OPTIONS [OPTIONS ...]], --options [OPTIONS [OPTIONS ...]]
                        Your age threshold and desired interval size separated
                        by a colon
