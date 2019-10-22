.. Copyright (c) 2016-2017, Ruslan Baratov
.. All rights reserved.

.. spelling::

  PowerShell

.. _-S:

-S
--

Add ``-S <path-to-source-tree>`` to set directory with ``CMakeLists.txt``.
This option was added in CMake 3.13 and replaces the the undocumented and internal variable ``-S``. This option can be used independently of ``-B``.

.. code-block:: none

  cmake -S . -B _builds

Use current directory as a source tree (i.e. start with
``./CMakeLists.txt``) and put generated files to the ``./_builds`` folder.

Path to this directory will be saved in
`CMAKE_SOURCE_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html>`__
variable.

.. seealso::

  * :ref:`-B <-B>`
  * :ref:`Source tree <source tree>`
