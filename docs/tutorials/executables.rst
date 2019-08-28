.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Executables
===========

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/executable-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/executable-examples/archive/master.zip>`__

.. admonition:: CMake documentation

  * `add_executable <https://cmake.org/cmake/help/latest/command/add_executable.html>`__

Simple
------

Building executable from ``main.cpp``:

.. literalinclude:: /examples/executable-examples/simple/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

.. code-block:: none
  :emphasize-lines: 2, 20

  [executable-examples]> rm -rf _builds
  [executable-examples]> cmake -Ssimple -B_builds
  -- The C compiler identification is GNU 5.4.0
  -- The CXX compiler identification is GNU 5.4.0
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /usr/bin/c++
  -- Check for working CXX compiler: /usr/bin/c++ -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../executable-examples/_builds
  [executable-examples]> cmake --build _builds
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/main.cpp.o
  [100%] Linking CXX executable foo
  [100%] Built target foo

.. code-block:: none
  :emphasize-lines: 2

  [executable-examples]> ./_builds/foo
  Hello from CGold!

.. _target duplicates:

Duplicates
----------

Targets are global, you can't declare two targets with the same name even
if they are declared in different ``CMakeLists.txt``:

.. literalinclude:: /examples/executable-examples/duplicates/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6-7

.. literalinclude:: /examples/executable-examples/duplicates/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. literalinclude:: /examples/executable-examples/duplicates/bar/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. code-block:: none
  :emphasize-lines: 2, 17-22

  [examples]> rm -rf _builds
  [examples]> cmake -Sexecutable-examples/duplicates -B_builds
  -- The C compiler identification is GNU 5.4.0
  -- The CXX compiler identification is GNU 5.4.0
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /usr/bin/c++
  -- Check for working CXX compiler: /usr/bin/c++ -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  CMake Error at bar/CMakeLists.txt:1 (add_executable):
    add_executable cannot create target "foo" because another target with the
    same name already exists.  The existing target is an executable created in
    source directory
    "/.../executable-examples/duplicates/boo".
    See documentation for policy CMP0002 for more details.
