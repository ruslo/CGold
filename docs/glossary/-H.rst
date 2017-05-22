.. Copyright (c) 2016-2017, Ruslan Baratov
.. All rights reserved.

.. spelling::

  PowerShell

.. _-H:

-H
--

Add ``-H<path-to-source-tree>`` to set directory with ``CMakeLists.txt``.
This internal option is not documented but
`widely used by community <https://github.com/search?q=%22cmake+-H%22&ref=searchresults&type=Code&utf8=%E2%9C%93>`__.
There must be no spaces between ``-H`` and ``<path-to-source-tree>``
(otherwise option will be interpreted as synonym to ``--help``). Always must
be used with :ref:`-B <-B>` option. Example:

.. code-block:: none

  cmake -H. -B_builds

Use current directory as a source tree (i.e. start with
``./CMakeLists.txt``) and put generated files to the ``./_builds`` folder.

Path to this directory will be saved in
`CMAKE_SOURCE_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html>`__
variable.

.. warning::

  PowerShell will modify arguments and put the space between ``-H`` and ``.``.
  You can protect argument by quoting it:

  .. code-block:: none

    cmake '-H.' -B_builds

.. seealso::

  * :ref:`-B <-B>`
  * :ref:`Source tree <source tree>`

.. admonition:: Stackoverflow

  * `Changing CMake files standard location <http://stackoverflow.com/a/13713684/2288008>`__
  * `How to tell CMake where to put build files? <http://stackoverflow.com/a/20611964/2288008>`__

.. admonition:: CMake mailing list

  * `Document -H/-B <http://www.mail-archive.com/cmake-developers@cmake.org/msg16693.html>`__
