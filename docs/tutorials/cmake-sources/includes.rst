.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _include modules:

Include modules
===============

CMake modules is a common way to reuse code.

Include standard
~~~~~~~~~~~~~~~~

CMake comes with a set of
`standard modules <https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html>`__:

.. literalinclude:: /examples/cmake-sources/include-processor-count/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 6

.. code-block:: none
  :emphasize-lines: 2, 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Sinclude-processor-count -B_builds
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

You can modify a ``CMAKE_MODULE_PATH`` variable to add the path with your
custom CMake modules:

.. literalinclude:: /examples/cmake-sources/include-users/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8

.. literalinclude:: /examples/cmake-sources/include-users/modules/MyModule.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: none
  :emphasize-lines: 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Sinclude-users -B_builds
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

  include(tool_verifier) # BAD! What if a parent project already has 'tool_verifier'?

  include(foo_tool_verifier) # Good, includes "./cmake/Modules/foo_tool_verifier.cmake"

.. seealso::

  * `OpenCV modules <https://github.com/opencv/opencv/tree/5f30a0a076e57c412509becd1fb618170cbfa179/cmake>`__

.. seealso::

  * :ref:`Function names <function name recommendation>`
  * :ref:`Cache names <cache name recommendation>`

Modify correct
~~~~~~~~~~~~~~

Note that the correct way to set this path is to **append** it to an existing
value:

.. literalinclude:: /examples/cmake-sources/modify-path/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 8, 10

For example when a user wants to use his own modules instead of standard for
any reason:

.. literalinclude:: /examples/cmake-sources/modify-path/standard/ProcessorCount.cmake
  :language: cmake
  :emphasize-lines: 4-5

Works fine:

.. code-block:: none
  :emphasize-lines: 3-4

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Smodify-path -B_builds "-DCMAKE_MODULE_PATH=`pwd`/modify-path/standard"
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

.. code-block:: none
  :emphasize-lines: 3

  [cmake-sources]> rm -rf _builds
  [cmake-sources]> cmake -Smodify-incorrect -B_builds "-DCMAKE_MODULE_PATH=`pwd`/modify-incorrect/standard"
  Number of processors: 4
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../cmake-sources/_builds
