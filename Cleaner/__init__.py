import os


class Cleaner(object):
    def __init__(self, results):
        if len(results) <= 0:
            print('No archives found.')
        else:
            self.archives = results
        for archive in self.archives:
            print(archive)

    def clean(self):
        confirm_delete = raw_input('Are you sure you want to delete the archives listed above? (y/n): ')
        if confirm_delete.lower() == 'y':
            for archive in self.archives:
                os.remove(archive)
