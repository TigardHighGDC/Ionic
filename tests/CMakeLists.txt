# Copyright (c) TigardHighGDC
# SPDX-License-Identifier: Apache-2.0

add_library(ionic_core STATIC IMPORTED)

if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/build/")
    set(ionic_core_SRC "${CMAKE_SOURCE_DIR}/build/src/libsrc.a")
else()
    set(ionic_core_SRC "${CMAKE_SOURCE_DIR}/src/libsrc.a")
endif()

set_target_properties(ionic_core PROPERTIES 
            IMPORTED_LOCATION ionic_core_SRC)

add_library(glfw_core STATIC IMPORTED)
set_target_properties(glfw_core PROPERTIES 
             IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/lib/libglfw3.a")

add_dependencies(ionic_core ionic_core_test)
add_dependencies(glfw_core ionic_core_test)

add_executable(window_test.out ionic/window/test.cpp)
target_link_libraries(window_test.out ${ionic_core_SRC})
target_link_libraries(window_test.out ${CMAKE_SOURCE_DIR}/lib/libglfw3.a ${GLFW_DEPENDENCIES})
