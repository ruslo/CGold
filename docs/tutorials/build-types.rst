.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  Multi

Build types
-----------

.. admonition:: Stackoverflow

  * `CMAKE_BUILD_TYPE not being used in CMakeLists.txt <http://stackoverflow.com/a/24470998/2288008>`__

Detect Multi/Single
===================

.. code-block:: cmake
  :emphasize-lines: 1

  string(COMPARE EQUAL "${CMAKE_CFG_INTDIR}" "." is_single)
  if(is_single)
    message("Single-configuration generator")
  else()
    message("Multi-configuration generator")
  endif()

.. admonition:: CMake documentation

  * `CMAKE_CFG_INTDIR <https://cmake.org/cmake/help/latest/variable/CMAKE_CFG_INTDIR.html>`__

.. warning::

  ``if(XCODE OR MSVC)`` condition doesn't work because ``MSVC`` **defined**
  for NMake single-configuration generator too.

.. warning::

  ``if(XCODE OR MSVC_IDE)`` condition doesn't work because ``MSVC_IDE`` is
  **not defined** for Visual Studio MDD toolchain.
