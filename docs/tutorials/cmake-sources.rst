.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  cmake

CMake sources
-------------

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/cmake-sources>`__
  * `Latest ZIP <https://github.com/cgold-examples/cmake-sources/archive/master.zip>`__

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

Include modules
===============

Include standard
~~~~~~~~~~~~~~~~

.. literalinclude:: /examples/cmake-sources/include-processor-count/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 6

.. code-block:: shell
  :emphasize-lines: 2, 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hinclude-processor-count -B_builds
  Number of processors: 4
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

.. admonition:: CMake documentation

  * `ProcessorCount <https://cmake.org/cmake/help/latest/module/ProcessorCount.html>`__

.. warning::

  Do not include ``Find*.cmake`` modules such way. ``Find*.cmake`` modules
  designed to be used via
  `find_package <https://cmake.org/cmake/help/latest/command/find_package.html>`__.

Include custom
~~~~~~~~~~~~~~

You can modify ``CMAKE_MODULE_PATH`` variable to add the path with your
custom CMake modules:

.. literalinclude:: /examples/cmake-sources/include-users/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8

.. literalinclude:: /examples/cmake-sources/include-users/modules/MyModule.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: shell
  :emphasize-lines: 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hinclude-users -B_builds
  Hello from MyModule!
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

.. admonition:: CMake documentation

  * `CMAKE_MODULE_PATH <https://cmake.org/cmake/help/latest/variable/CMAKE_MODULE_PATH.html>`__

.. _module name recommendation:

Recommendation
++++++++++++++

To avoid conflicts of your modules with modules from other projects (if they
are mixed together by ``add_subdirectory``) do "namespace" their names with the
project name:

.. code-block:: cmake
  :emphasize-lines: 6, 8

  cmake_minimum_required(VERSION 2.8)
  project(foo)

  list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules")

  include(tool_verifier) # BAD! What if parent project already has 'tool_verifier'?

  include(foo_tool_verifier) # Good, includes "./cmake/Modules/foo_tool_verifier.cmake"

.. seealso::

  * `OpenCV modules <https://github.com/opencv/opencv/tree/5f30a0a076e57c412509becd1fb618170cbfa179/cmake>`__

Modify correct
~~~~~~~~~~~~~~

Note that the correct way to set this path is to **append** it to existing
value:

.. literalinclude:: /examples/cmake-sources/modify-path/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8, 10

For example when user want to use his own modules instead of standard for
any reason:

.. literalinclude:: /examples/cmake-sources/modify-path/standard/ProcessorCount.cmake
  :language: cmake
  :emphasize-lines: 4-5

Works fine:

.. code-block:: shell
  :emphasize-lines: 3-4

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hmodify-path -B_builds "-DCMAKE_MODULE_PATH=`pwd`/modify-path/standard"
  Force processor count
  Number of processors: 16
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

Modify incorrect
~~~~~~~~~~~~~~~~

It's not correct to set them ignoring current state:

.. literalinclude:: /examples/cmake-sources/modify-incorrect/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

In this case if user want to use custom modules:

.. literalinclude:: /examples/cmake-sources/modify-incorrect/standard/ProcessorCount.cmake
  :language: cmake
  :emphasize-lines: 4-5

They will **not** be loaded:

.. code-block:: shell
  :emphasize-lines: 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Hmodify-incorrect -B_builds "-DCMAKE_MODULE_PATH=`pwd`/modify-incorrect/standard"
  Number of processors: 4
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds

Scripts
=======

.. admonition:: CMake documentation

  * `CMake options <https://cmake.org/cmake/help/latest/manual/cmake.1.html#options>`__

Example
~~~~~~~

.. literalinclude:: /examples/cmake-sources/script/create-file.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: shell
  :emphasize-lines: 2, 4, 6

  [cmake-sources]> rm -f Hello.txt
  [cmake-sources]> cmake -P script/create-file.cmake
  [cmake-sources]> ls Hello.txt
  Hello.txt
  [cmake-sources]> cat Hello.txt
  Created by script

Minimum required (bad)
~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /examples/cmake-sources/minimum-required-bad/script.cmake
  :language: cmake
  :emphasize-lines: 6, 9

.. code-block:: shell
  :emphasize-lines: 1, 2, 14

  [cmake-sources]> cmake -P minimum-required-bad/script.cmake
  MYNAME: Jane Doe
  CMake Warning (dev) at minimum-required-bad/script.cmake:6 (if):
    Policy CMP0054 is not set: Only interpret if() arguments as variables or
    keywords when unquoted.  Run "cmake --help-policy CMP0054" for policy
    details.  Use the cmake_policy command to set the policy and suppress this
    warning.

    Quoted variables like "Jane Doe" will no longer be dereferenced when the
    policy is set to NEW.  Since the policy is not set the OLD behavior will be
    used.
  This warning is for project developers.  Use -Wno-dev to suppress it.

  MYNAME is empty!

Minimum required (good)
~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /examples/cmake-sources/minimum-required-good/script.cmake
  :language: cmake
  :emphasize-lines: 8, 11

.. code-block:: shell
  :emphasize-lines: 1, 2

  [cmake-sources]> cmake -P minimum-required-good/script.cmake
  MYNAME: Jane Doe

cmake -E
~~~~~~~~

.. admonition:: CMake documentation

  * `Command-Line Tool Mode <https://cmake.org/cmake/help/latest/manual/cmake.1.html#command-line-tool-mode>`__

.. literalinclude:: /examples/cmake-sources/without-command-line/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13, 20

.. literalinclude:: /examples/cmake-sources/command-line/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5
