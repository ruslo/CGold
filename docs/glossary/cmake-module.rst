.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _cmake module:

CMake module
============

:ref:`Listfiles <listfile>` located in directories specified by
`CMAKE_MODULE_PATH <https://cmake.org/cmake/help/latest/variable/CMAKE_MODULE_PATH.html>`__
and having extension ``.cmake`` called **modules**. They can be loaded by
``include`` command. Unlike ``add_subdirectory`` command
``include(<modulename>)`` doesn't create new node in a source/binary tree
hierarchies and doesn't introduce new scope for variables.

.. note::

  In general by ``include`` you can load file with any name, not only
  ``*.cmake``. For example:

  .. code-block:: cmake

    include(some/file/abc.tt) # file with extension '.tt'
    include(another/file/XYZ) # file without extension

  Or even ``CMakeLists.txt``:

  .. code-block:: cmake

    include(foo/bar/CMakeLists.txt)

  Though it is confusing, doesn't make sense and should be avoided.

.. admonition:: CMake documentation

  * `Modules <https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#modules>`__
  * `include <https://cmake.org/cmake/help/latest/command/include.html>`__
