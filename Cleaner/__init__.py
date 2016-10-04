import os


class Cleaner(object):
    def __init__(self, results):
        if len(results['remove']) <= 0:
            print('No archives found.')
            self.proceed_cleaning = False
        else:
            self.proceed_cleaning = True
            self.archives = results
            print('KEEP')
            print('----------------------')
            for archive in self.archives['keep']:
                print(archive)
            print(' ')
            print('REMOVE')
            print('----------------------')
            for archive in self.archives['remove']:
                print(archive)
            print(' ')

    def clean(self):
        if self.proceed_cleaning:
            confirm_delete = raw_input('Are you sure you want to delete the archives listed above? (y/n): ')
            if confirm_delete.lower() == 'y':
                for archive in self.archives['remove']:
                    os.remove(archive)