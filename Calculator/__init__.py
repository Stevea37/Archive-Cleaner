import os
from datetime import datetime, timedelta


class Calculator(object):

    def __init__(self, path, options):
        if len(options) <= 0:
            print("After providing the archive directory, you must also provide the cleaning options.")
            print("E.g. python cleaner.py /path/to/archive 30,2 90,3.")
            print("The example provided will keep every other archive older than "
                  "30 days old and every 3 archives older than 90 days.")
            exit()

        self.options = options
        self.options = options.sort(key=lambda n: n.split(',')[0])

        if path is None:
            ValueError('Please specify a path')
        self.path = path
        self.archives = self.categorise_archives()

    def list_archives(self):
        results = []
        for root, subFolders, files in os.walk(self.path):
            for result_file in files:
                file_path = os.path.join(root, result_file)
                if file_path.endswith('.tgz'):
                    results.append(file_path)
        return results

    def categorise_archives(self):
        archive_dictionary = {}
        for archive in self.list_archives():
            module_name = os.path.basename(archive).split('-')[0]
            if module_name in archive_dictionary:
                archive_dictionary[module_name].append(archive)
            else:
                archive_dictionary[module_name] = [archive]
        for module in archive_dictionary:
            archive_dictionary[module].sort(key=lambda n: os.stat(n).st_mtime)
        return archive_dictionary

    def match_archives(self, max_age, min_age, step):
        results = []
        for module in self.archives:
            frame_results = []
            for index, archive in enumerate(self.archives[module]):
                archive_date = os.path.getmtime(archive)
                modified_date = datetime.fromtimestamp(archive_date)
                duration = datetime.today() - modified_date
                if min_age <= duration.days <= max_age:
                    frame_results.append(archive)
            category_results = []
            for index, archive in enumerate(frame_results):
                if index == 0:
                    last_index = index
                    continue
                this_time = datetime.fromtimestamp(os.path.getmtime(archive))
                last_time = datetime.fromtimestamp(os.path.getmtime(self.archives[module][last_index]))
                if (this_time - last_time) <= timedelta(days=step):
                    category_results.append(archive)
                else:
                    last_index = index
            results.extend(category_results)
        return results

    def calculate(self):
        results = []
        for index, option in enumerate(self.options):
            print(option)
            min_age = option.split(',')[0]
            if index < len(self.options):
                max_age = self.options[index + 1].split(',')[0]
            else:
                max_age = 0
            step = option.split(',')[1]
            matched_archives = self.match_archives(max_age, min_age, step)
            results.extend(matched_archives)
        return results
