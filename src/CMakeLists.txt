# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

set(SOURCES
    window/window.cpp
)

add_library(src ${SOURCES})

include_directories(BEFORE "{CMAKE_CURRENT_LIST_DIR}/inc")
