.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

write_compiler_detection_header
===============================

.. admonition:: CMake documentation

  * `WriteCompilerDetectionHeader <https://cmake.org/cmake/help/latest/module/WriteCompilerDetectionHeader.html>`__

This module doesn't provide enough abstraction. You have to specify supported
compilers explicitly. From documentation:

.. code-block:: none

  Compilers which are known to CMake, but not specified are detected and a
  preprocessor #error is generated for them.

Meaning that this code:

.. code-block:: cmake
  :emphasize-lines: 12

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.10)
  project(foo)

  include(WriteCompilerDetectionHeader)

  set(gen_include "${CMAKE_CURRENT_BINARY_DIR}/generated/")
  write_compiler_detection_header(
      FILE "${gen_include}/${PROJECT_NAME}/detection.hpp"
      PREFIX ${PROJECT_NAME}
      COMPILERS Clang MSVC
      FEATURES cxx_variadic_templates
      VERSION 3.10
  )

  add_executable(foo foo.cpp)
  target_include_directories(
      foo PUBLIC "$<BUILD_INTERFACE:${gen_include}>"
  )

.. code-block:: cpp

  // foo.cpp
  #include <foo/detection.hpp>

  int main() {
  }

Will return error while compiling with GCC:

.. code-block:: none
  :emphasize-lines: 3

  /usr/bin/g++ ... -c /.../foo.cpp
  In file included from /.../foo.cpp:2:0:
  /.../generated/foo/detection.hpp:192:6: error: #error Unsupported compiler
   #    error Unsupported compiler
        ^

Compiler identification relies on ``CMAKE_<LANG>_COMPILER_ID`` which is not
guaranteed to be set by CMake.
From `documentation <https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_ID.html>`__:

.. code-block:: none

  This variable is not guaranteed to be defined for all compilers or languages.
