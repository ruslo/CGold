.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _-B:

-B
--

Add ``-B<path-to-binary-tree>`` to set the path to directory where CMake will
store generated files. There must be no spaces between ``-B`` and
``<path-to-binary-tree>``. Always must be used with :ref:`-H <-H>` option.

Path to this directory will be saved in
`CMAKE_BINARY_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html>`__
variable.

.. note::
Starting with CMake 3.13,  ``-B`` is an officially supported flag and can handle
spaces correctly and can be used independently of the :ref:`-S <-S>` or :ref:`-H <-H>` options.

.. code-block:: none

  cmake -B _builds .

.. seealso::

  * :ref:`Binary tree <binary tree>`
  * :ref:`-S <-S>`
  * :ref:`-H <-H>`
