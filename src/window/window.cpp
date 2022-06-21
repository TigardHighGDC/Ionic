// Copyright (c) TigardHighGDC
// SPDX-License-Identifier: Apache-2.0

#include "window.h"

#include <GLFW/glfw3.h>

#include <iostream>
#include <string>

namespace ionic {

Window::Window(const std::string& title, int width, int height) {
    if (glfwInit() == false) {
        std::cerr << "Failed to initialize GLFW; aborting...\n";
        return;
    }

    // 4 AA
    glfwWindowHint(GLFW_SAMPLES, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    window = glfwCreateWindow(width, height, title.c_str(), nullptr, nullptr);
    glfwMakeContextCurrent(window);
}

Window::~Window() {
    glfwDestroyWindow(window);
    glfwTerminate();
}

void Window::close() {
    glfwSetWindowShouldClose(window, true);

    if (glfwWindowShouldClose(window)) {
        glfwTerminate();
    }
}

[[nodiscard]] bool Window::isClosed() const {
    return glfwWindowShouldClose(window);
}

} // namespace ionic