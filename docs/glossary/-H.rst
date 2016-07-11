.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _-H:

-H
--

Add ``-H<path-to-source-tree>`` to set directory with ``CMakeLists.txt``.
This internal option is not documented but
`widely used by community <https://github.com/search?q=%22cmake+-H%22&ref=searchresults&type=Code&utf8=%E2%9C%93>`__.
There must be no spaces between ``-H`` and ``<path-to-source-tree>``
(otherwise option will be interpreted as synonym to ``--help``). Always must
be used with :ref:`-B <-B>` option. Example:

.. code-block:: shell

  cmake -H. -B_builds

Use current directory as a source tree (i.e. start with
``./CMakeLists.txt``) and put generated files to the ``./_builds`` folder.

.. seealso::

  * :ref:`-B <-B>`
  * :ref:`Source tree <source tree>`

.. admonition:: Stackoverflow

  * `Changing CMake files standard location <http://stackoverflow.com/a/13713684/2288008>`__

.. admonition:: CMake mailing list

  * `Document -H/-B <http://www.mail-archive.com/cmake-developers@cmake.org/msg16693.html>`__
