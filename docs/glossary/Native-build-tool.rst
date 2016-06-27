.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Native build tool
-----------------

.. _Native build tool:

Native build tool (also known as ``native tool`` or ``native build system``) is
the real tool (collection of tools such as compiler+IDE) used to build your
software. :ref:`CMake <CMake>` is not a build tool itself since it can't build
your projects or help with development like IDE do. CMake responsibility is to
**generate** native build tool files from abstracted configuration code.

Examples:

* Xcode
* Visual Studio
* Ninja
* Make

Quotes
======

Quote from `CMAKE_OBJECT_PATH_MAX <https://cmake.org/cmake/help/latest/variable/CMAKE_OBJECT_PATH_MAX.html>`_:

.. code-block:: text

  Maximum object file full-path length allowed by native build tools

Quote from `CMake <https://cmake.org/cmake/help/latest/manual/cmake.1.html#description>`_:

.. code-block:: text

  Users build a project by using CMake to generate a build system for a native
  tool on their platform

Quote from `CMake options <https://cmake.org/cmake/help/latest/manual/cmake.1.html#options>`_:

.. code-block:: text

  CMake may support multiple native build systems on certain platforms
