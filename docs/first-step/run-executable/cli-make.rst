.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Make
---------

Usually to build executable with Make you need to find directory with ``Makefile``
and run ``make`` in it:

.. code-block:: none

  > cd _builds
  [cgold-example/_builds]> make
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX executable foo
  [100%] Built target foo

But CMake offer cross-tool way to do exactly the same by ``cmake --build _builds``:

.. code-block:: none

  [cgold-example]> cmake --build _builds
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX executable foo
  [100%] Built target foo

Run ``foo``:

.. code-block:: none

  [cgold-example]> ./_builds/foo
  Hello from CGold!

Done!
