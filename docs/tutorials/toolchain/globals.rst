.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

Globals
=======

Even if toolchain is originally designed to help with cross-compiling and
usually containing fancy variables like
`CMAKE_SYSTEM_NAME <https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html>`__
or
`CMAKE_FIND_ROOT_PATH <https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_ROOT_PATH.html>`__
in practice it can help you with holding compiler settings that logically
doesn't belong to some particular local ``CMakeLists.txt`` but rather should be
shared across various projects.

.. toctree::
  :maxdepth: 2

  /tutorials/toolchain/globals/cxx-standard
