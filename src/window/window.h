// Copyright (c) TigardHighGDC
// SPDX-License-Identifier: Apache-2.0

#ifndef IONIC_WINDOW_WINDOW_H_
#define IONIC_WINDOW_WINDOW_H_

#include <GLFW/glfw3.h>

#include <iostream>
#include <string>

namespace ionic {

class Window {
   public:
    Window(const std::string& title, int width, int height);
    ~Window();

    void close();

    [[nodiscard]] bool isClosed() const;

   private:
    GLFWwindow* window;
};

}  // namespace ionic

#endif  // IONIC_WINDOW_WINDOW_H_