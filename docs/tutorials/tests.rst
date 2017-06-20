.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

.. spelling::

  config

Tests
=====

In previous section we have checked that executable is working by finding it
in binary tree and running it explicitly. If we have several executables
or want to run the same executable with different parameters we can organize
everything into test suite driven by CTest tool.

.. admonition:: CMake documentation

  * `ctest <https://cmake.org/cmake/help/latest/manual/ctest.1.html>`__
  * `add_test <https://cmake.org/cmake/help/latest/command/add_test.html>`__
  * `enable_testing <https://cmake.org/cmake/help/latest/command/enable_testing.html>`__

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/test-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/test-examples/archive/master.zip>`__

Creating two executables:

.. literalinclude:: /examples/test-examples/simple/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6-7

Executable ``boo``:

.. literalinclude:: /examples/test-examples/simple/boo.cpp
  :language: cpp
  :emphasize-lines: 3-5

Executable ``bar``:

.. literalinclude:: /examples/test-examples/simple/bar.cpp
  :language: cpp
  :emphasize-lines: 3-8

Testing allowed by ``enable_testing`` directive which must be
called in **the root directory**:

.. literalinclude:: /examples/test-examples/simple/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 9

Come up with some tests name and specify executable arguments if needed:

.. literalinclude:: /examples/test-examples/simple/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 10-13

Configure and build project:

.. code-block:: none
  :emphasize-lines: 2, 20

  [examples]> rm -rf _builds
  [examples]> cmake -Htest-examples/simple -B_builds
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
  -- Build files have been written to: /.../examples/_builds
  [examples]> cmake --build _builds
  Scanning dependencies of target boo
  [ 25%] Building CXX object CMakeFiles/boo.dir/boo.cpp.o
  [ 50%] Linking CXX executable boo
  [ 50%] Built target boo
  Scanning dependencies of target bar
  [ 75%] Building CXX object CMakeFiles/bar.dir/bar.cpp.o
  [100%] Linking CXX executable bar
  [100%] Built target bar

Enter ``_builds`` directory and use ``ctest`` tool to run all tests:

.. code-block:: none
  :emphasize-lines: 2

  [examples]> cd _builds
  [examples/_builds]> ctest
  Test project /.../examples/_builds
      Start 1: boo
  1/3 Test #1: boo ..............................   Passed    0.00 sec
      Start 2: bar
  2/3 Test #2: bar ..............................   Passed    0.00 sec
      Start 3: bar-with-args
  3/3 Test #3: bar-with-args ....................   Passed    0.00 sec

  100% tests passed, 0 tests failed out of 3

  Total Test time (real) =   0.02 sec

Multi-config testing
--------------------

Note that for the
:doc:`multi-configuration generators </glossary/multi-config>`
you have to specify build type while running ``ctest``. Otherwise no
tests will be run. Example of Visual Studio project:

.. code-block:: none
  :emphasize-lines: 1, 5, 8, 11

  [examples\_builds]> ctest
  Test project C:/.../examples/_builds
      Start 1: boo
  Test not available without configuration.  (Missing "-C <config>"?)
  1/3 Test #1: boo ..............................***Not Run   0.00 sec
      Start 2: bar
  Test not available without configuration.  (Missing "-C <config>"?)
  2/3 Test #2: bar ..............................***Not Run   0.00 sec
      Start 3: bar-with-args
  Test not available without configuration.  (Missing "-C <config>"?)
  3/3 Test #3: bar-with-args ....................***Not Run   0.00 sec

  0% tests passed, 3 tests failed out of 3

  Total Test time (real) =   0.02 sec

  The following tests FAILED:
            1 - boo (Not Run)
            2 - bar (Not Run)
            3 - bar-with-args (Not Run)
  Errors while running CTest

Just add ``-C Debug`` to test with ``Debug`` build type:

.. code-block:: none
  :emphasize-lines: 1, 4, 6, 8

  [examples\_builds]> ctest -C Debug
  Test project C:/.../examples/_builds
      Start 1: boo
  1/3 Test #1: boo ..............................   Passed    0.04 sec
      Start 2: bar
  2/3 Test #2: bar ..............................   Passed    0.02 sec
      Start 3: bar-with-args
  3/3 Test #3: bar-with-args ....................   Passed    0.01 sec

  100% tests passed, 0 tests failed out of 3

  Total Test time (real) =   0.09 sec

Verbose output
--------------

By default only ``Passed``/``Failed`` information is shown. You can control
tests output by ``-V``/``-VV`` options:

.. code-block:: none
  :emphasize-lines: 1, 8, 15, 22-25

  [examples/_builds]> ctest -VV
  ...
  test 1
      Start 1: boo

  1: Test command: /.../examples/_builds/boo
  1: Test timeout computed to be: 9.99988e+06
  1: boo
  1/3 Test #1: boo ..............................   Passed    0.00 sec
  test 2
      Start 2: bar

  2: Test command: /.../examples/_builds/bar
  2: Test timeout computed to be: 9.99988e+06
  2: bar argc: 1
  2/3 Test #2: bar ..............................   Passed    0.00 sec
  test 3
      Start 3: bar-with-args

  3: Test command: /.../examples/_builds/bar "arg1" "arg2" "arg3"
  3: Test timeout computed to be: 9.99988e+06
  3: bar argc: 4
  3: argv[1]: arg1
  3: argv[2]: arg2
  3: argv[3]: arg3
  3/3 Test #3: bar-with-args ....................   Passed    0.00 sec

  100% tests passed, 0 tests failed out of 3

  Total Test time (real) =   0.01 sec

Subset of tests
---------------

It is possible to run only subset of tests instead of all suite. For example
running all tests with ``bar`` pattern in name by using regular expression:

.. code-block:: none
  :emphasize-lines: 1, 4, 6

  [examples/_builds]> ctest -R bar
  Test project /.../examples/_builds
      Start 2: bar
  1/2 Test #2: bar ..............................   Passed    0.00 sec
      Start 3: bar-with-args
  2/2 Test #3: bar-with-args ....................   Passed    0.00 sec

  100% tests passed, 0 tests failed out of 2

  Total Test time (real) =   0.01 sec

Or only ``bar`` test:

.. code-block:: none
  :emphasize-lines: 1, 4

  [examples/_builds]> ctest -R '^bar$'
  Test project /.../examples/_builds
      Start 2: bar
  1/1 Test #2: bar ..............................   Passed    0.00 sec

  100% tests passed, 0 tests failed out of 1

  Total Test time (real) =   0.01 sec
