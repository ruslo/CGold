.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _-B:

-B
--

Add ``-B<path-to-build-tree>`` to set the path to directory where CMake will
store generated files. There must be no spaces between ``-B`` and
``<path-to-build-tree>``. Always must be used with :ref:`-H <-H>` option.

Path to this directory will be saved in
`CMAKE_BINARY_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html>`__
variable.

.. seealso::

  * :ref:`Build tree <build tree>`
  * :ref:`-H <-H>`
