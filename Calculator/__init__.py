import os
import datetime


class Calculator(object):

    def __init__(self, path, options):
        if len(options) <= 0:
            print("After providing the archive directory, you must also provide the cleaning options.")
            print("E.g. python cleaner.py /path/to/archive 30,2 90,3.")
            print("The example provided will keep every other archive older than "
                  "30 days old and every 3 archives older than 90 days.")
            exit()
        if path is None:
            ValueError('Please specify a path')
        self.options = options.sort(key=lambda n: n.split(',')[0])
        self.path = path
        self.archives = self.list_archives()

    def list_archives(self):
        results = []
        for root, subFolders, files in os.walk(self.path):
            for result_file in files:
                file_path = os.path.join(root, result_file)
                if file_path.endswith('.tgz'):
                    results.append(file_path)
        return results

    def match_archive(self, max_age, min_age, step):
        results = []
        for archive in self.archives:
            archive_date = os.path.getmtime(archive)
            modified_date = datetime.datetime.fromtimestamp(archive_date)
            duration = datetime.datetime.today() - modified_date
            if min_age <= duration.days <= max_age:
                results.append(archive)
        return results[::step]

    def sort_archives(self, archives):
        return archives

    def calculate(self):
        results = []
        for index, option in self.options:
            min_age = option.split(',')[0]
            if index > len(self.options):
                max_age = self.options[index + 1].split(',')[0]
            else:
                max_age = 0
            step = option.split(',')[1]
            matched_archives = self.match_archive(max_age, min_age, step)
            sorted_archives = self.sort_archives(matched_archives)
            for archives in sorted_archives:
                results.append(archives)
        return results
