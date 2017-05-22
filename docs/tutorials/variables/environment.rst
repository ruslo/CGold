.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Environment variables
---------------------

Read
====

Environment variable can be read by using ``$ENV{...}`` syntax:

.. literalinclude:: /examples/usage-of-variables/read-env/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

.. code-block:: none
  :emphasize-lines: 2-3, 5-6

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> echo $USERNAME
  ruslo
  [usage-of-variables]> export USERNAME
  [usage-of-variables]> cmake -Hread-env -B_builds
  Environment variable USERNAME: ruslo
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Set
===

By using ``set(ENV{...})`` syntax CMake can set environment variable:

.. literalinclude:: /examples/usage-of-variables/set-env/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

.. code-block:: none
  :emphasize-lines: 2-3, 5-6

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> echo $USERNAME
  ruslo
  [usage-of-variables]> export USERNAME
  [usage-of-variables]> cmake -Hset-env -B_builds
  Environment variable USERNAME: Jane Doe
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Unset
=====

Unset environment variable:

.. literalinclude:: /examples/usage-of-variables/unset-env/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

.. code-block:: none
  :emphasize-lines: 2-3, 5-6

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> echo $USERNAME
  ruslo
  [usage-of-variables]> export USERNAME
  [usage-of-variables]> cmake -Hunset-env -B_builds
  Environment variable USERNAME:
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Inheriting
==========

Child process will inherit environment variables of parent:

.. literalinclude:: /examples/usage-of-variables/env-inherit/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8, 15, 24, 29

.. literalinclude:: /examples/usage-of-variables/env-inherit/level1.cmake
  :language: cmake
  :emphasize-lines: 3, 8

.. literalinclude:: /examples/usage-of-variables/env-inherit/level2.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: none
  :emphasize-lines: 2, 3, 7

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Henv-inherit -B_builds
  Set environment variable
  Top level ABC: This is ABC
  Environment variable from level1: This is ABC
  Environment variable from level2: This is ABC
  Unset environment variable
  Top level ABC:
  Environment variable from level1:
  Environment variable from level2:
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Configure step
==============

Note that in previous examples variable was set on
:ref:`configure step <configure>`:

.. literalinclude:: /examples/usage-of-variables/env-configure/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 6

.. code-block:: none
  :emphasize-lines: 2, 3

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Henv-configure -B_builds
  Environment variable ABC: 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

But environment variable remains the same on :ref:`build step <build>`:

.. literalinclude:: /examples/usage-of-variables/env-configure/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 11

.. literalinclude:: /examples/usage-of-variables/env-configure/script.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: none
  :emphasize-lines: 3

  [usage-of-variables]> cmake --build _builds
  Scanning dependencies of target foo
  Environment variable from script:
  Built target foo

No tracking
===========

CMake doesn't track changes of used environment variables so if your CMake code
depends on environment variable and you're planning to change it from time to
time it will break normal :ref:`workflow <workflow>`:

.. literalinclude:: /examples/usage-of-variables/env-depends/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

.. warning::

  Do not write code like that!

.. code-block:: none
  :emphasize-lines: 2-3, 25

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> export ABC=abc
  [usage-of-variables]> cmake -Henv-depends -B_builds
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
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> cmake --build _builds
  Scanning dependencies of target abc-tgt
  [ 50%] Building CXX object CMakeFiles/abc-tgt.dir/foo.cpp.o
  [100%] Linking CXX executable abc-tgt
  [100%] Built target abc-tgt

Let's update environment variable:

.. code-block:: none
  :emphasize-lines: 1

  [usage-of-variables]> export ABC=123

Name of the target **was not changed**:

.. code-block:: none
  :emphasize-lines: 2

  [usage-of-variables]> cmake --build _builds
  [100%] Built target abc-tgt

You have to run configure manually yourself:

.. code-block:: none
  :emphasize-lines: 1, 9

  [usage-of-variables]> cmake -Henv-depends -B_builds
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> cmake --build _builds
  Scanning dependencies of target 123-tgt
  [ 50%] Building CXX object CMakeFiles/123-tgt.dir/foo.cpp.o
  [100%] Linking CXX executable 123-tgt
  [100%] Built target 123-tgt

Summary
=======

* CMake can set, unset and read environment variables
* Check carefully configure-build steps where you set environment variables
* Child processes will inherit environment variables of parent
* Do not make your CMake code depends on environment variable if that
  variable may change
