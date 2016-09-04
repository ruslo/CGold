.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CMake listfiles
---------------

There are several places where CMake code can live: ``CMakeLists.txt`` listfiles
loaded by ``add_subdirectory`` command will help you to create source/binary
tree. This is a skeleton of your project. ``*.cmake`` modules help you to
organize/reuse CMake code. CMake scripts can be executed by ``cmake -P`` and
help you to solve problems in cross-platform fashion without relying on
system specific tools like bash or without introducing external tool dependency
like Python.

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/cmake-sources>`__
  * `Latest ZIP <https://github.com/cgold-examples/cmake-sources/archive/master.zip>`__

.. toctree::
  :glob:
  :maxdepth: 2

  cmake-sources/subdirectories
  cmake-sources/includes
  cmake-sources/scripts
