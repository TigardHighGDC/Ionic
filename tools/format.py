# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

import os

def main():
    with open('files.lst', 'r') as file:
        """files.lst contains a list of files to be formatted"""
        for line in file:
            print(f'Formatting {line.strip()}')
            os.system(f'clang-format -i -style=file {line.strip()}')


if __name__ == '__main__':
    main()