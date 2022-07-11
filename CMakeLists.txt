# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.10)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
project(thsgdc_ionic_game_engine VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(glfw)
add_subdirectory(src)