# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.4...3.21.6 FATAL_ERROR)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

project(thsgdc_ionic_game_engine VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(DGLFW_USE_WAYLAND ON)
set(BUILD_TESTING ON)

set(GLFW_DEPENDENCIES X11 Xrandr Xinerama Xxf86vm Xcursor GL dl pthread)

add_subdirectory(src)

set(BUILD_TESTING ON)

if(BUILD_TESTING)
    add_subdirectory(tests)
endif()