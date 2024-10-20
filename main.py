import filecmp
import os
import re

original_regex = re.compile(r'\s*\([1-9]+\)\s*')
duplicate_regex = re.compile(r'\w+\s*\([1-9]+\)\s*.*')


def detect_duplicate(path: str):
    return re.match(duplicate_regex, os.path.basename(path))


def original_exists(path: str):
    return os.path.exists(make_original_path(path))


def make_original_path(path: str):
    parent, basename = os.path.split(path)
    original_basename = original_regex.sub('', '')
    return os.path.join(parent, original_basename)


def main():
    filenames = os.listdir()
    duplicates = [filename for filename in filenames if detect_duplicate(filename)]

    for duplicate in duplicates:
        if original_exists(duplicate):
            if filecmp.cmp(duplicate, make_original_path(duplicate), False):
                os.remove(duplicate)
        else:
            os.rename(duplicate, make_original_path(duplicate))


if __name__ == '__main__':
    main()
