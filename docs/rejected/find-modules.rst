.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

FindXXX.cmake
=============

There are no instructions for writing ``FindXXX.cmake`` files like
`FindZLIB.cmake`_ because it's easier to add some code to generate
`ZLIBConfig.cmake`_ automatically.

Quote from `CMake wiki <https://cmake.org/Wiki/CMake:Improving_Find*_Modules>`__:

.. code-block:: none

  If creating a Find* module for a library that already uses CMake as its build
  system, please create a *Config.cmake instead, and submit it upstream. This
  solution is much more robust.

.. admonition:: CMake documentation

  * `Creating packages <https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#creating-packages>`__

.. admonition:: Stackoverflow

  * `MODULE vs CONFIG <http://stackoverflow.com/a/20857070/2288008>`__

.. admonition:: Examples on GitHub

  * `Package example <https://github.com/forexample/package-example>`__

.. _FindZLIB.cmake: https://github.com/Kitware/CMake/blob/7a47745d69003ec580e8f38d26dbf8858a4f5b18/Modules/FindZLIB.cmake
.. _ZLIBConfig.cmake: https://github.com/hunter-packages/zlib/blob/8d3ad09e42332d21a578d6e6ecf2756d58e48761/CMakeLists.txt#L222
