from __future__ import annotations

import filecmp
import os
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from re import Match


# similar: The files are apparently duplicate (by their names)
# identical: The files are similar and their contents are also same

original_regex = re.compile(r'\s*\([1-9]+\)\s*')
duplicate_regex = re.compile(r'\w+\s*\([1-9]+\)\s*.*')


def detect_similar(path: str) -> Match:
    return duplicate_regex.fullmatch(os.path.basename(path))


def similarly_original_exists(path: str) -> bool:
    return os.path.exists(make_similar_original_path(path))


def identical_exists(duplicate_path: str) -> bool:
    similar_original_path = make_similar_original_path(duplicate_path)
    return similarly_original_exists(duplicate_path) and filecmp.cmp(similar_original_path, duplicate_path, False)


def make_similar_original_path(path: str) -> str:
    parent, basename = os.path.split(path)
    original_basename = original_regex.sub('', basename)
    return os.path.join(parent, original_basename)


def main() -> None:
    filenames = os.listdir()
    duplicates = [filename for filename in filenames if detect_similar(filename)]

    for duplicate in duplicates:
        if similarly_original_exists(duplicate):
            if identical_exists(duplicate):
                os.remove(duplicate)
        else:
            os.rename(duplicate, make_similar_original_path(duplicate))


if __name__ == '__main__':
    main()
