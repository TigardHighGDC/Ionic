# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

import os
from typing import List

def retrieve_copyright() -> List[str]:
    with open('../COPYRIGHT', 'r') as file:
        copyright = file.readlines()

    for line in copyright:
        line = f'// {line}'

    return copyright


def retrieve_files() -> List[str]:
    """files.lst contains all files to be checked"""
    with open('files.lst', 'r') as file:
        files = file.readlines()

    return files


def main():
    os.chdir('../')
    copyright = retrieve_copyright()
    files = retrieve_files()

    for file in files:
        with open(file, 'r') as f:
            contents = f.readlines()

        if copyright[0] != contents[0] or copyright[1] != contents[1]:
            print(f'`{file}` is missing copyright; exiting')
            exit(1)


if __name__ == "__main__":
    main()