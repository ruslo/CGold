.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  foo
  cpp

Minimal example
---------------

Create an empty directory and put ``foo.cpp`` and ``CMakeLists.txt`` files into it.

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/minimal-example>`__
  * `Latest ZIP <https://github.com/cgold-examples/minimal-example/archive/master.zip>`__

``foo.cpp`` is the C++ source of our executable:

.. literalinclude:: /examples/minimal-example/foo.cpp
  :language: cpp

``CMakeLists.txt`` is a project configuration, i.e. source for :ref:`CMake <CMake>`:

.. literalinclude:: /examples/minimal-example/CMakeLists.txt
  :language: cmake

Description
===========

foo.cpp
~~~~~~~

Explanation of the ``foo.cpp`` content is out of the scope of this document, so it will
be skipped.

CMakeLists.txt
~~~~~~~~~~~~~~

The first line of ``CMakeLists.txt`` is a comment and will be ignored:

.. literalinclude:: /examples/minimal-example/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 1

The next line tells us about the ``CMake`` version for which this file is written:

.. literalinclude:: /examples/minimal-example/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

``2.8`` means we can use this configuration with ``CMake`` versions like
``2.8``, ``2.8.7``, ``3.0``, ``3.5.1``, etc. but not with ``2.6.0`` or ``2.4.2``.

With the declaration of the project ``foo``, the ``Visual Studio`` solution will
have name ``foo.sln``, and the ``Xcode`` project name will be ``foo.xcodeproj``:

.. literalinclude:: /examples/minimal-example/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

Adding executable ``foo`` with source ``foo.cpp``:

.. literalinclude:: /examples/minimal-example/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

:ref:`CMake <CMake>` has some predefined settings so it will figure out the following
things:

* ``*.cpp`` extension is for the C++ sources, so target ``foo`` will be built with the C++ compiler
* on Windows executables usually have the suffix ``.exe``, so the resulting binary will be named ``foo.exe``
* on Unix platforms like OSX or Linux executables usually have no suffixes,
  so the resulting binary will be named ``foo``
