.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _cmakelists.txt:

CMakeLists.txt
--------------

CMakeLists.txt is a :ref:`listfile <listfile>` which plays the role of entry
point for current source directory. CMake processing will start from top level
``CMakeLists.txt`` in :ref:`source tree <source tree>` and continue with other
dependent ``CMakeLists.txt`` files added by `add_subdirectory`_ directive.
Each ``add_subdirectory`` will create new node in the source/binary tree
hierarchy and introduce new scope for variables.

.. admonition:: CMake documentation

  * `Directories <https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#directories>`__

.. _add_subdirectory: https://cmake.org/cmake/help/latest/command/add_subdirectory.html
