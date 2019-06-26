.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

Object libraries
================

.. admonition:: CMake documentation

  * `Object Libraries <https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#object-libraries>`__
  * `add_library(... OBJECT ...) <https://cmake.org/cmake/help/latest/command/add_library.html#object-libraries>`__

As documentation states ``OBJECT`` library is a non-archival collection of object files.
``OBJECT`` libraries have few limitations which makes them harder to use.

target_link_libraries
~~~~~~~~~~~~~~~~~~~~~

``OBJECT`` library can't be used on the right hand side of ``target_link_libraries`` command.
In practice it means that you will not be able to make a hierarchy of targets as you
do with regular ``add_library`` command.

Example:

.. code-block:: cmake
  :emphasize-lines: 9

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_library(boo OBJECT boo.cpp)

  add_library(foo OBJECT foo.cpp)
  target_link_libraries(foo PUBLIC boo)

  add_executable(baz $<TARGET_OBJECTS:foo> baz.cpp)

Will produce an error:

.. code-block:: none

  CMake Error at CMakeLists.txt:8 (target_link_libraries):
    Object library target "foo" may not link to anything.

You should put all dependent components to ``add_executable``
explicitly:

.. code-block:: cmake
  :emphasize-lines: 13-15

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_library(boo OBJECT boo.cpp)

  add_library(foo OBJECT foo.cpp)

  add_executable(
      baz
      $<TARGET_OBJECTS:foo>
      # List all 'foo' dependencies explicitly
      $<TARGET_OBJECTS:boo>
      # ...
      baz.cpp
  )

If this component is optional:

.. code-block:: cmake
  :emphasize-lines: 6, 10, 12, 20

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  option(FOO_WITH_BOO "With 'boo' component" ON)

  if(FOO_WITH_BOO)
    add_library(boo OBJECT boo.cpp)
    set(boo_objects $<TARGET_OBJECTS:boo>)
  else()
    set(boo_objects "")
  endif()

  add_library(foo OBJECT foo.cpp)

  add_executable(
      baz
      $<TARGET_OBJECTS:foo>
      ${boo_objects}
      baz.cpp
  )

Target name
~~~~~~~~~~~

Even if an ``OBJECT`` library is not a "real" target you will still have
to name it carefully as a regular target since it will occupy slot in
pool of names. As a result you can't use it as a local temporary helper tool:

.. code-block:: cmake

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_subdirectory(boo)
  add_subdirectory(bar)

.. code-block:: cmake
  :emphasize-lines: 3

  # boo/CMakeLists.txt

  add_library(core OBJECT x1.cpp x2.cpp)
  add_executable(boo $<TARGET_OBJECTS:core> boo.cpp)

.. code-block:: cmake
  :emphasize-lines: 3

  # bar/CMakeLists.txt

  add_library(core OBJECT y1.cpp y2.cpp)
  add_executable(bar $<TARGET_OBJECTS:core> bar.cpp)

Error:

.. code-block:: none

  CMake Error at bar/CMakeLists.txt:1 (add_library):
    add_library cannot create target "core" because another target with the
    same name already exists.  The existing target is created in source
    directory "/.../boo".  See documentation
    for policy CMP0002 for more details.

Usage requirements
~~~~~~~~~~~~~~~~~~

Usage requirements will not be propagated:

.. code-block:: cmake

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  include_directories("${CMAKE_CURRENT_LIST_DIR}")

  add_library(boo OBJECT boo.cpp boo.hpp)
  target_compile_definitions(boo PUBLIC FOO_WITH_BOO)

  add_executable(baz $<TARGET_OBJECTS:boo> baz.cpp)

.. code-block:: cpp
  :emphasize-lines: 6-8

  // boo.hpp

  #ifndef BOO_HPP_
  #define BOO_HPP_

  #if !defined(FOO_WITH_BOO)
  # error "FOO_WITH_BOO is not defined!"
  #endif

  #endif // BOO_HPP_

.. code-block:: cpp
  :emphasize-lines: 3

  // baz.cpp

  #include <boo.hpp>

  int main() {
  }

``boo.cpp`` source will compile fine because ``FOO_WITH_BOO``
will be added:

.. code-block:: none

  /usr/bin/g++ -DFOO_WITH_BOO ... -o CMakeFiles/boo.dir/boo.cpp.o -c /.../boo.cpp

But not ``baz.cpp``:

.. code-block:: none

  /usr/bin/g++ ... -o CMakeFiles/baz.dir/baz.cpp.o -c /.../baz.cpp
  In file included from /.../baz.cpp:3:0:
  /.../boo.hpp:7:3: error: #error "FOO_WITH_BOO is not defined!"
   # error "FOO_WITH_BOO is not defined!"
     ^

No real sources
~~~~~~~~~~~~~~~

As mentioned in documentation you can't have target with only
``OBJECT`` files. E.g. this code will not work with Xcode:

.. code-block:: cmake

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_library(boo OBJECT boo.cpp)
  add_executable(foo $<TARGET_OBJECTS:boo>)

  enable_testing()
  add_test(NAME foo COMMAND foo)

No warnings or build errors but when you will try to test it:

.. code-block:: none

  1: Test command:
  Unable to find executable: /.../_builds/Release/foo
  1/1 Test #1: foo ..............................***Not Run   0.00 sec

.. note::

  As a workaround you can add dummy source file to the executable.

Name conflict
~~~~~~~~~~~~~

You can't have two source files with the same names even if they are located
in different directories. This code will not work with Xcode generator:

.. code-block:: cmake
  :emphasize-lines: 6

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_library(boo OBJECT x.cpp boo/x.cpp)
  add_executable(foo foo.cpp $<TARGET_OBJECTS:boo>)

As a workaround source files can be renamed:

.. code-block:: cmake
  :emphasize-lines: 6

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_library(boo OBJECT x.1.cpp boo/x.2.cpp)
  add_executable(foo foo.cpp $<TARGET_OBJECTS:boo>)

Or additional target can be introduced:

.. code-block:: cmake
  :emphasize-lines: 7

  # CMakeLists.txt

  cmake_minimum_required(VERSION 3.2)
  project(foo)

  add_library(boo.1 OBJECT x.cpp)
  add_library(boo.2 OBJECT boo/x.cpp)
  add_executable(foo foo.cpp $<TARGET_OBJECTS:boo.1> $<TARGET_OBJECTS:boo.2>)
