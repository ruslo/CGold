.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

Multi-configuration generator
-----------------------------

Generator that allows to use several build types on build step while doing
only one configure step. List of available build types can be specified by
`CMAKE_CONFIGURATION_TYPES <https://cmake.org/cmake/help/latest/variable/CMAKE_CONFIGURATION_TYPES.html>`__.
Default value for ``CMAKE_CONFIGURATION_TYPES`` is a list of:

* ``Debug``
* ``Release``
* ``MinSizeRel``
* ``RelWithDebInfo``

Example of configuring ``Debug`` + ``Release`` project and building ``Debug``
variant:

.. code-block:: none

  > cmake -H. -B_builds -DCMAKE_CONFIGURATION_TYPES=Release;Debug -GXcode
  > cmake --build _builds --config Debug

It is legal to use same ``_builds`` directory to build ``Release`` variant
without rerunning configure again:

.. code-block:: none

  > cmake --build _builds --config Release

Multi-configuration generators:

* `Xcode <https://cmake.org/cmake/help/latest/generator/Xcode.html>`__
* `Visual Studio <https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators>`__

.. admonition:: CGold

  * :doc:`Single-configuration generator </glossary/single-config>`
