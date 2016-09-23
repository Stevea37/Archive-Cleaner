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
    def clean(archives):
        for archive in archives:
            print(archive)
        if Cleaner.confirm('Are you sure you want to delete the archives listed above? (y/n): '):
            for archive in archives:
                os.remove(archive)


class Calculator:
    @staticmethod
    def list_archives(path):
        results = []
        for root, subFolders, files in os.walk(path):
            for result_file in files:
                file_path = os.path.join(root, result_file)
                if file_path.endswith('.tgz'):
                    results.append(file_path)
        return results

    @staticmethod
    def match_archive(archives, max_age, min_age, step):
        results = []
        for archive in archives:
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(archive))
            duration = datetime.datetime.today() - modified_date
            if min_age <= duration.days <= max_age:
                results.append(archive)
        return results[::step]

    @staticmethod
    def sort_archives(archives):
        print(archives)

    @staticmethod
    def calculate(options):
        results = []
        recursive_archive_dir = Calculator.list_archives(sys.argv[1])
        options = options.sort(key=lambda n: n.split(',')[0])
        for index, option in options:
            min_age = option.split(',')[0]
            if index > len(options):
                max_age = options[index + 1].split(',')[0]
            else:
                max_age = 0
            step = option.split(',')[1]
            results.extend(Calculator.match_archive(recursive_archive_dir, max_age, min_age, step))
        return results


def main():
    options = sys.argv[2:]
    if len(options) <= 0:
        print("After providing the archive directory, you must also provide the cleaning options.")
        print("E.g. python cleaner.py /path/to/archive 30,2 90,3.")
        print("The example provided will keep every other archive older than "
              "30 days old and every 3 archives older than 90 days.")
        exit()

    results = Calculator.calculate(options)
    if len(results) > 0:
        Cleaner.clean(results)
    else:
        print('No archives found.')


if __name__ == '__main__':
    main()
