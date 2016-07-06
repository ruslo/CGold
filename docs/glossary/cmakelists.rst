.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _cmakelists.txt:

CMakeLists.txt
--------------

File with :ref:`CMake <CMake>` code. CMake processing will start from top level
``CMakeLists.txt`` in :ref:`source tree <source tree>` and continue with other
dependent ``CMakeLists.txt`` files added by
`add_subdirectory`_ directive or any kind of CMake files
added by `include`_. In latter case file name may differs from
``CMakeLists.txt``. In general in this document by ``CMakeLists.txt`` meant
any file with CMake code.

.. _add_subdirectory: https://cmake.org/cmake/help/latest/command/add_subdirectory.html
.. _include: https://cmake.org/cmake/help/latest/command/include.html
