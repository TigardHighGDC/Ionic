# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

set(SOURCES
    window/window.cpp
)

add_library(src ${SOURCES})

target_include_directories(src PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
add_library(glfw_core STATIC IMPORTED)
set_target_properties(glfw_core PROPERTIES 
             IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/lib/libglfw3.a")
