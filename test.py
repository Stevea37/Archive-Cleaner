from cleaner import Calculator


def main():
    archives = Calculator.list_archives('.')
    for archive in archives:
        archive = archive.split('/')[len(archive)-1]
        print(archive)

if __name__ == '__main__':
    main()