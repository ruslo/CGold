.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Make
---------

The instructions are the same for both ``Linux`` and ``OSX``. Open a terminal and change
to the directory with the sources:

.. code-block:: none

  > cd cgold-example
  [cgold-example]> ls
  CMakeLists.txt foo.cpp

Generate a Makefile using CMake. Use :ref:`-H. <-H>` :ref:`-B_builds <-B>` for
specifying paths and ``-G "Unix Makefiles"`` for the generator (note that
``Unix Makefiles`` is usually the default generator so ``-G`` is probably not
needed at all):

.. code-block:: none
  :emphasize-lines: 1, 18

  [cgold-example]> cmake -H. -B_builds -G "Unix Makefiles"
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
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
  -- Build files have been written to: /.../cgold-example/_builds

The generated ``Makefile`` can be found in the ``_builds`` directory:

.. code-block:: none

  > ls _builds/Makefile
  _builds/Makefile

Next let's :doc:`build and run the executable </first-step/run-executable/cli-make>`.
