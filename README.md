# Archive-Cleaner
Clean up backup archives

THIS SCRIPT DELETES BACKUP FILES TO INCREASE THE INTERVAL BETWEEN DATA SNAPSHOTS, FOR SPACE SAVING PURPOSES. WHEN RUN MORE THAN ONCE, THE INTERVALS MAY BECOME DISTORTED.

pyton cleaner.py path/to/backup/set if_older_than_this_number,days_interval

Example usage:
pyton cleaner.py ../../backups/archives/10.102.81.196 7,2 30,3 90,5
