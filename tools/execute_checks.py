# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

"""
This is a local testing script.
"""

import os

def main():
    os.chdir('checks/')

    for root, _, files in os.walk('./'):
        for file in files:
            if file.endswith('.py'):
                print(f'Executing {file}...')
                exit_code = os.system(f'python3 {root}/{file}')
                
                if exit_code != 0:
                    print(f'{root}/{file} failed; exiting')
                    exit(1)

    print('All checks passed; exiting')


if __name__ == "__main__":
    main()