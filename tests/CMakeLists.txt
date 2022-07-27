# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

add_library(ionic_core STATIC IMPORTED)
set_target_properties(ionic_core PROPERTIES 
             IMPORTED_LOCATION "build/src/libsrc.a")

add_library(glfw_core STATIC IMPORTED)
set_target_properties(glfw_core PROPERTIES 
             IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/lib/libglfw3.a")

add_dependencies(ionic_core ionic_core_test)
add_dependencies(glfw_core ionic_core_test)

add_executable(window_test.out ionic/window/test.cpp)
target_link_libraries(window_test.out ${CMAKE_SOURCE_DIR}/build/src/libsrc.a)
target_link_libraries(window_test.out ${CMAKE_SOURCE_DIR}/lib/libglfw3.a ${GLFW_DEPENDENCIES})
