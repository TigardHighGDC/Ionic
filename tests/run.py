# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

"""
Automated test runner.
Should be ran from the root directory of the project.
"""

import os

def main():
    # Find all .out files in the tests/ directory and run them
    for file in os.listdir('tests'):
        if file.endswith('.out'):
            exit_code = os.system('./tests/' + file)

            if exit_code != 0:
                print('Test failed: ' + file)
                exit(1)

    print('All tests passed!')
    print('Exit code 0.')

if __name__ == '__main__':
    main()