// Copyright (c) TigardHighGDC
// SPDX-License-Identifier: Apache-2.0

#include "../../../src/window/window.h"

#include <cassert>

int main() {
    ionic::Window window("title", 800, 600);
    assert(!window.isClosed());
    
    window.close();
    assert(window.isClosed());

    return 0;
}