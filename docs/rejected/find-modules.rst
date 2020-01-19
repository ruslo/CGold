.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

FindXXX.cmake
=============

There are no instructions for writing ``FindXXX.cmake`` files like
``FindZLIB.cmake``_ because it's easier to add some code to generate
``ZLIBConfig.cmake``_ automatically.

Quote from `CMake wiki <https://cmake.org/Wiki/CMake:Improving_Find*_Modules>`__:

.. code-block:: none

  If creating a Find* module for a library that already uses CMake as its build
  system, please create a *Config.cmake instead, and submit it upstream. This
  solution is much more robust.

.. admonition:: CMake documentation

  * `Creating packages <https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#creating-packages>`__

.. admonition:: Examples on GitHub

  * `Package example <https://github.com/forexample/package-example>`__
