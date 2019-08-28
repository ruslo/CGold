.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

Single-configuration generator
------------------------------

Generator that allows to have only single build type while configuring project.
Build type defined by
`CMAKE_BUILD_TYPE <https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html>`__
on configure step and can't be changed on build step.

Example of building ``Debug`` variant:

.. code-block:: none

  > cmake -S. -B_builds -DCMAKE_BUILD_TYPE=Debug
  > cmake --build _builds

To use another build type like ``Release`` use
:ref:`out-of-source feature <out-of-source-config>`.

All generators that are not
:doc:`multi-configuration </glossary/multi-config>` are single-configuration.
Typical example of such generator is a
`Unix Makefiles <https://cmake.org/cmake/help/latest/generator/Unix%20Makefiles.html>`__
generator.
