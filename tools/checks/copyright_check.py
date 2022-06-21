# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

import os

def main():
    os.chdir('../')

    with open('../COPYRIGHT', 'r') as file:
        copyright = file.readlines()

    for i, line in enumerate(copyright):
        copyright[i] = f'// {line}'

    # files.lst contains all files to be checked
    with open('files.lst', 'r') as file:
        files = file.readlines()

    for file in files:
        file = file.strip()

        with open(file, 'r') as f:
            contents = f.readlines()

        if copyright[0] != contents[0] or copyright[1] != contents[1]:
            print(f'`{file}` is missing copyright; exiting')
            exit(1)


if __name__ == "__main__":
    main()