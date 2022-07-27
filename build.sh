# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

set -e

read -r -p "Do you wish to also run the build tests? [y/n]: "

if ! [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Building without tests..."
    echo "Running cmake..."
    cmake . -DBUILD_TESTING=OFF
    echo "Running make..."
    make
else
    echo "Building with tests..."
    echo "Running cmake..."
    cmake . -DBUILD_TESTING=ON
    echo "Running make..."
    make
    echo "Running tests..."
    python3 tests/run.py
fi

echo "Done!"