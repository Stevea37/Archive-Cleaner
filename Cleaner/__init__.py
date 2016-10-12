import os


class Cleaner(object):
    def __init__(self, calc):
        self.calc = calc
        if len(self.calc.results['remove']) <= 0:
            print('No archives found.')
            self.proceed_cleaning = False
        else:
            self.proceed_cleaning = True
            print('KEEP')
            print('----------------------')
            for archive in self.calc.results['keep']:
                print(archive)
            print(' ')
            print('REMOVE')
            print('----------------------')
            for archive in self.calc.results['remove']:
                print(archive)
            print(' ')

    def clean(self):
        if self.calc.compromised_interval:
            print('One or more archives cannot be deleted as the interval left would be too far over the threshold'
                  ' (125% of the specified interval).')
        if self.proceed_cleaning:
            if not self.calc.force:
                confirm_delete = raw_input('Are you sure you want to delete the archives listed above? (y/n): ')
            else:
                confirm_delete = 'y'

            if confirm_delete.lower() == 'y':
                for archive in self.calc.results['remove']:
                    os.remove(archive)
