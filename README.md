# Tigard High Game Development Club Ionic C++ Game Engine

![Ionic Image](images/ionic-titan-logo.png)

The Ionic C++ Game Engine is a simple game engine designed specifically for
['to be filled'](). This engine was developed by Tigard High Students during
the 2022-2023 school year.

- Read our [Project Guidelines](https://github.com/TigardHighGDC/Ionic/blob/main/docs/guidelines.md).
- Our [Issue Project Board](https://github.com/TigardHighGDC/Ionic/projects/3) keeps track of all current issues.
- Our [Code Review Project Board](https://github.com/TigardHighGDC/Ionic/projects/1) keeps track of all PR's under review.
- Join our [Discord Server](https://discord.gg/ZvsKGCFUQb).

![Clang Format Check](https://github.com/TigardHighGDC/Ionic/actions/workflows/clang-format-check.yml/badge.svg?event=push)

## Building the Project

### Dependencies

The Ionic Game Engine has lots of dependencies. This is an incomplete list of
the most import ones.

- [GLFW](https://www.glfw.org/)
- [gcc](https://gcc.gnu.org/)
- [python3](https://www.python.org/)

### Running the build script

The `build.sh` does everything you need to build the project from the command line.

This includes:

- Building the core engine and linking glfw.
- Optionally running the associated static tests on your local machine.

Simply run:

```Command Line
$ ./build.sh
Do you wish to also run the build tests? [y/n]: y
Building with tests...
Running cmake...
-- Configuring done
-- Generating done
-- Build files have been written to: /home/brandon/documents/Ionic
Running make...
Consolidate compiler generated dependencies of target src
[ 50%] Built target src
Consolidate compiler generated dependencies of target window_test.out
[100%] Built target window_test.out
Running tests...
All tests passed!
Exit code 0.
Done!
```

Optionally, we also recommend using the CMake VSCode extension for simple
control over the project build process.

## Maintainer List

- [Brandon Pacewic](https://github.com/BrandonPacewic)
- [Nathan St. John](https://github.com/Galaxy25)

## License

Copyright (c) TigardHighGDC

SPDX-License-Identifier: Apache-2.0
