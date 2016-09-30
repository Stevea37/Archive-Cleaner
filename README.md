# Archive-Cleaner
Clean up backup archives

THIS SCRIPT DELETES BACKUP FILES TO INCREASE THE INTERVAL BETWEEN DATA SNAPSHOTS, FOR SPACE SAVING PURPOSES. THIS CANNOT DIFFERENTIATE BETWEEN DIFFERENT BACKUP SETS AT THE MOMENT. PLEASE DO NOT USE THIS ON MORE THAN ONE SET OF BACKUPS.

I will be changing the interval to days rather than deleting every Nth backup.


pyton cleaner.py path/to/backup/set if_older_than_this_number,keep_every_nth_backup

Example usage:
pyton cleaner.py ../../backups/archives/10.102.81.196 7,2 30,3 90,5
