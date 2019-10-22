.. Copyright (c) 2016-2017, Ruslan Baratov
.. All rights reserved.

.. spelling::

  PowerShell

.. _-S:

-S
--

.. note::

  Has been replaced in 3.13 with the official source directory flag of :ref:`-S <-S>`.

Add ``-S<path-to-source-tree>`` to set directory with ``CMakeLists.txt``.
This internal option is not documented but
`widely used by community <https://github.com/search?q=%22cmake+-S%22&ref=searchresults&type=Code&utf8=%E2%9C%93>`__.
There must be no spaces between ``-S`` and ``<path-to-source-tree>``
(otherwise option will be interpreted as synonym to ``--help``). Always must
be used with :ref:`-B <-B>` option. Example:

.. code-block:: none

  cmake -S. -B_builds

Use current directory as a source tree (i.e. start with
``./CMakeLists.txt``) and put generated files to the ``./_builds`` folder.

Path to this directory will be saved in
`CMAKE_SOURCE_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html>`__
variable.

.. warning::

  PowerShell will modify arguments and put the space between ``-S`` and ``.``.
  You can protect argument by quoting it:

  .. code-block:: none

    cmake '-S.' -B_builds

.. seealso::

  * :ref:`-S <-S>`
  * :ref:`-B <-B>`
  * :ref:`Source tree <source tree>`

.. admonition:: CMake mailing list

  * `Document -S/-B <http://www.mail-archive.com/cmake-developers@cmake.org/msg16693.html>`__
