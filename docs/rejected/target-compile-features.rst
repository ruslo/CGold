.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

target_compile_features
=======================

.. admonition:: CMake documentation

  * `CMake compile features <https://cmake.org/cmake/help/latest/manual/cmake-compile-features.7.html>`__
  * `target_compile_features <https://cmake.org/cmake/help/latest/command/target_compile_features.html>`__

This function sets locally something that belongs to global settings.
Such behavior can lead to nontrivial errors. See for details:

* :doc:`ODR violation (global) </tutorials/libraries/symbols/odr-global>`
* :doc:`C++ standard </tutorials/toolchain/globals/cxx-standard>`
