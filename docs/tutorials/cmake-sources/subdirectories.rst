.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Subdirectories
==============

.. literalinclude:: /examples/cmake-sources/subdirectories/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6-7, 12, 13, 15

.. literalinclude:: /examples/cmake-sources/subdirectories/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-7, 9

.. literalinclude:: /examples/cmake-sources/subdirectories/boo/bar/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-7

.. code-block:: shell
  :emphasize-lines: 2, 4-5, 7-8, 12, 13, 17, 18

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hsubdirectories -B_builds
  Before project:
    CMAKE_SOURCE_DIR: /.../cmake-sources/subdirectories
    CMAKE_BINARY_DIR: /.../cmake-sources/_builds
  Top level:
    CMAKE_CURRENT_SOURCE_DIR: /.../cmake-sources/subdirectories
    CMAKE_CURRENT_BINARY_DIR: /.../cmake-sources/_builds
  Subdirectory 'boo':
    CMAKE_SOURCE_DIR: /.../cmake-sources/subdirectories
    CMAKE_BINARY_DIR: /.../cmake-sources/_builds
    CMAKE_CURRENT_SOURCE_DIR: /.../cmake-sources/subdirectories/boo
    CMAKE_CURRENT_BINARY_DIR: /.../cmake-sources/_builds/boo
  Subdirectory 'bar':
    CMAKE_SOURCE_DIR: /.../cmake-sources/subdirectories
    CMAKE_BINARY_DIR: /.../cmake-sources/_builds
    CMAKE_CURRENT_SOURCE_DIR: /.../cmake-sources/subdirectories/boo/bar
    CMAKE_CURRENT_BINARY_DIR: /.../cmake-sources/_builds/boo/bar
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

.. admonition:: CMake documentation

  * `add_subdirectory <https://cmake.org/cmake/help/latest/command/add_subdirectory.html>`__
  * `CMAKE_SOURCE_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html>`__
  * `CMAKE_BINARY_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html>`__
  * `CMAKE_CURRENT_SOURCE_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_CURRENT_SOURCE_DIR.html>`__
  * `CMAKE_CURRENT_BINARY_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_CURRENT_BINARY_DIR.html>`__

.. seealso::

  * :ref:`-H <-H>`
  * :ref:`-B <-B>`
