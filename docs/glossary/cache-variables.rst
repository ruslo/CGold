.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _cache variables:

Cache variables
---------------

For optimization purposes there are special type of variables which lifetime
is not limited with one CMake run (e.g. like
:ref:`regular cmake variables <cmake variables>`). Variables saved in
:ref:`CMakeCache.txt <cmakecache.txt>` file and persist across multiple runs
within a project build tree [1]_.

.. [1] Quote from `documentation <https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables>`__.
