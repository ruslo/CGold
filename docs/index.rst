.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CGold: The Hitchhiker's Guide to the CMake
------------------------------------------

Welcome to **CGold**!

This guide will show you how to use :ref:`CMake <CMake>` and helps you to write elegant,
correct and scalable projects. We'll start from the simple cases and add more features one
by one. This tutorial covers only part of :ref:`CMake <CMake>` capabilities - some topics
are skipped intentionally in favor of better modern approaches. E.g. there are
no instructions for writing ``Find*.cmake`` files like `FindZLIB.cmake`_ because
it's easier to add some code to generate `ZLIBConfig.cmake`_ automatically.
There will be no hints about writing superbuild project using
`ExternalProject`_ because same can be done nicely with :ref:`Hunter package
manager <Hunter>`. Document designed to be a good tutorial for the very
begginers but touches some aspects which may be interested to advanced
developers too. Look at it as a skeleton/starting point for further :ref:`CMake <CMake>`
learning.

Enjoy!

.. _CMake capabilities: https://cmake.org/cmake/help/latest/
.. _FindZLIB.cmake: https://github.com/Kitware/CMake/blob/7a47745d69003ec580e8f38d26dbf8858a4f5b18/Modules/FindZLIB.cmake
.. _ZLIBConfig.cmake: https://github.com/hunter-packages/zlib/blob/8d3ad09e42332d21a578d6e6ecf2756d58e48761/CMakeLists.txt#L222
.. _ExternalProject: https://cmake.org/cmake/help/latest/module/ExternalProject.html
.. _Hunter package manager: https://github.com/ruslo/hunter

.. toctree::
  :maxdepth: 2

  /overview
  /first-step
  /tutorials
  /platforms
  /generators

.. toctree::
  :hidden:
  :maxdepth: 1

  /glossary
