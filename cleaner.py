import sys
import datetime
import os


class Cleaner:
    @staticmethod
    def confirm(question):
        confirm_delete = raw_input(question)
        if confirm_delete.lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def clean(archive_list):
        for archive in archive_list:
            print(archive)
        if Cleaner.confirm('Are you sure you want to delete the archives listed above? (y/n): '):
            for archive in archive_list:
                os.remove(archive)


class Calculator:

    @staticmethod
    def list_recurse(path):
        results = []
        for root, subFolders, files in os.walk(path):

            for result_file in files:
                file_path = os.path.join(root, result_file)

                if file_path.endswith('.tgz'):
                    results.append(file_path)
        return results

    @staticmethod
    def match_archive(archive_list, younger_than, older_than, step):
        results = []
        for archive in archive_list:
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(archive))
            duration = datetime.datetime.today() - modified_date

            if older_than <= duration.days <= younger_than:
                results.append(archive)
        return results[::step]

    @staticmethod
    def calculator(recursive_archive_dir, cleaning_options):
        results = []
        cleaning_options = cleaning_options.sort(key=lambda n: n.split(',')[0])
        for index, option in cleaning_options:
            older_than = option.split(',')[0]
            if index > 0:
                younger_than = cleaning_options[index - 1].split(',')[0]
            else:
                younger_than = 0

            step = option.split(',')[1]
            results.extend(Calculator.match_archive(recursive_archive_dir, younger_than, older_than, step))
        return results


def main():

    archive_dir = Calculator.list_recurse(sys.argv[1])
    cleaning_options = sys.argv[2:]

    if len(cleaning_options) == 0:
        print("After providing the archive directory, you must also provide the cleaning options.")
        print("E.g. python cleaner.py /path/to/archive 30,2 90,3.")
        print("The example provided will keep every other archive older than "
              "30 days old and every 3 archives older than 90 days.")
        exit()

    results = Calculator.calculator(archive_dir, cleaning_options)
    if len(results) > 0:
        Cleaner.clean(results)
    else:
        print('No archives found.')


if __name__ == '__main__':
    main()
