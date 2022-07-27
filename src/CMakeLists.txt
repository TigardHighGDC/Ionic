# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

set(SOURCES 
    window/window.cpp
)

add_library(src ${SOURCES})

target_include_directories(src PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}") 