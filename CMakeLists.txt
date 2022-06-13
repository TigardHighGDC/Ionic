# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.10)

project(thsgdc_ionic_game_engine LANGUGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(src)

target_link_libraries(thgdc_ionic_game_engine PUBLIC src)

target_include_directories(thsgdc_ionic_game_engine PUBLIC
    "${PROJCET_BINARY_DIR}"
    "${PROJECT_SOURCE_DIR}/src")