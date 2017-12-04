.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

C++ standard
============

C++ standard flags should be set globally. You should avoid using any commands
that set it locally for target or project.

.. note::

  Example tested with GCC 5.4.1 on Linux. Different compilers may work
  with C++ standards differently.

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/toolchain-usage-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/toolchain-usage-examples/archive/master.zip>`__


Example
=======

Let's assume we have header-only library ``boo`` implemented by ``Boo.hpp``
which can work with both C++98 and C++11:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/base/Boo.hpp
  :language: cpp

Library ``foo`` that depends on ``boo`` and use C++11 **internally**:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/base/Foo.hpp
  :language: cpp

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/base/Foo.cpp
  :language: cpp
  :emphasize-lines: 5

Executable ``baz`` knows nothing about standards and just use API of
``Boo`` and ``Foo`` classes, ``Foo`` is optional:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/base/main.cpp
  :language: cpp

Graphically it will look like this:

.. image:: /examples/toolchain-usage-examples/globals/cxx-standard/base/base.png
  :align: center
  :alt: Targets

CMake project :

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/base/CMakeLists.txt
  :language: cmake

Overview:

* ``boo`` provide same API for both C++11 and C++98 configuration so user
  don't have to worry about standards.
* ``foo`` use some C++11 feature but only internally.
* ``baz`` don't know anything about used standards, interested only in ``boo``
  or ``foo`` API.

Imagine that ``baz`` for the long time relies only on ``boo``, it's important
to keep this functionality even for old C++98 configuration. But there is
``foo`` library that use C++11 and allow us to introduce some optimization.

We want:

* C++11 with ``foo``
* C++11 without ``foo``
* C++98 with ``foo`` should produce error message as soon as possible
* C++98 without ``foo``

Bad
===

The first thing that comes to mind after looking at C++ code is that since
``foo`` use ``constexpr`` feature internally we should do:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/bad/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 14

This is not correct and will end with error on link stage after successful
generation and compilation:

.. code-block:: none
  :emphasize-lines: 2, 9, 17-19

  [examples]> rm -rf _builds
  [examples]> cmake -Htoolchain-usage-examples/globals/cxx-standard/bad -B_builds -DWITH_FOO=ON
  -- The C compiler identification is GNU 5.4.1
  -- The CXX compiler identification is GNU 5.4.1
  ...
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../examples/_builds
  [examples]> cmake --build _builds
  Scanning dependencies of target foo
  [ 25%] Building CXX object CMakeFiles/foo.dir/Foo.cpp.o
  [ 50%] Linking CXX static library libfoo.a
  [ 50%] Built target foo
  Scanning dependencies of target baz
  [ 75%] Building CXX object CMakeFiles/baz.dir/main.cpp.o
  [100%] Linking CXX executable baz
  CMakeFiles/baz.dir/main.cpp.o: In function `main':
  main.cpp:(.text+0x64): undefined reference to `Foo::optimize(Boo::InternalThread&)'
  collect2: error: ld returned 1 exit status
  CMakeFiles/baz.dir/build.make:95: recipe for target 'baz' failed
  make[2]: *** [baz] Error 1
  CMakeFiles/Makefile2:104: recipe for target 'CMakeFiles/baz.dir/all' failed
  make[1]: *** [CMakeFiles/baz.dir/all] Error 2
  Makefile:83: recipe for target 'all' failed
  make: *** [all] Error 2

The reason is violation of ODR rule, similar example have been described
:doc:`before </tutorials/libraries/symbols/odr-global>`.
Effectively we are having two different libraries ``boo_11`` and ``boo_98``
with the same symbols:

.. image:: /examples/toolchain-usage-examples/globals/cxx-standard/bad/bad.png
  :align: center
  :alt: Targets

Toolchain
=========

Let's create toolchain file ``cxx11.cmake`` instead so we can use it to set
standard globally for all targets in project:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/toolchain/cxx11.cmake
  :language: cmake

You can add it with ``-DCMAKE_TOOLCHAIN_FILE=/path/to/cxx11.cmake``:

.. code-block:: none
  :emphasize-lines: 2, 20, 29-31

  [examples]> rm -rf _builds
  [examples]> cmake -Htoolchain-usage-examples/globals/cxx-standard/toolchain -B_builds -DCMAKE_TOOLCHAIN_FILE=cxx11.cmake -DWITH_FOO=YES
  -- The C compiler identification is GNU 5.4.1
  -- The CXX compiler identification is GNU 5.4.1
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
  Scanning dependencies of target foo
  [ 25%] Building CXX object CMakeFiles/foo.dir/Foo.cpp.o
  [ 50%] Linking CXX static library libfoo.a
  [ 50%] Built target foo
  Scanning dependencies of target baz
  [ 75%] Building CXX object CMakeFiles/baz.dir/main.cpp.o
  [100%] Linking CXX executable baz
  [100%] Built target baz
  [examples]> ./_builds/baz
  C++ standard: 201103
  With Foo support

Looks better now!

try_compile
===========

The next thing we need to improve is early error detection. Note that now
if we try to specify ``WITH_FOO=ON`` with C++98 there will be no errors
reported on generation stage. Build will failed while trying to compile ``foo``
target.

To do this you can create C++ file and add few samples of features you
are planning to use:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/try_compile/features_used_by_foo.cpp
  :language: cpp
  :emphasize-lines: 3

Use CMake module with ``try_compile`` to test this code:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/try_compile/features_used_by_foo.cmake
  :language: cmake
  :emphasize-lines: 6-11

Include this check before creating target ``foo``:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/try_compile/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13

Defaults
========

As usual cache variables allow us to set default values if needed:

.. literalinclude:: /examples/toolchain-usage-examples/globals/cxx-standard/defaults/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5-11, 15

.. note::

  * Toolchain should be set before first ``project`` command, see
    :ref:`Project: Tools discovering <project tools discovering>`

.. seealso::

  * :ref:`Cache variables: Use case <cache use case>`

Scalability
===========

If this example looks simple and used approach look like an overkill just
imagine next situation:

* ``boo`` is external library that supports C++98, C++11, C++14, etc. standards
  and consists of 1000+ source files
* ``foo`` is external library that supports only few modern standards and tested
  with C++11 and C++17. Consist of 1000+ source files and non-trivially
  interacts with ``boo``
* Your project ``baz`` has ``boo`` requirement and optional ``foo``, should
  works correctly in all possibles variations

The worst that may happen if you will use toolchain approach is that ``foo``
will fail with **compile** error instead of error on generation stage. The
error will be plain, such as ``Can't use 'auto', -std=c++11 is missing?``.
This can be easily improved with ``try_compile``.

If you will keep using locally specified standard like modifying
``CXX_STANDARD`` property and conflict will occur:

* there will be **no warning** messages on generate step
* there will be **no warning** messages on compile step
* link will fail with opaque error pointing to some **implementation details**
  inside ``boo`` library while your usage of ``boo`` API will look completely
  fine

When you will try to find error elsewhere:

* stand-alone version of ``boo`` will work correctly with all examples and
  standards
* stand-alone version of ``foo`` will interact correctly with ``boo`` with all
  examples and supported standards
* your project ``baz`` will work correctly with ``boo`` if you will use
  configuration without ``foo``

Summary
=======

* Use toolchain if you need to specify standard, set default toolchain if needed
* Avoid using ``CXX_STANDARD`` in your code
* Avoid using ``CMAKE_CXX_STANDARD`` anywhere except toolchain
* Avoid using ``target_compile_features`` module
* If you have to use them for any reason at least protect it with ``if``:

.. code-block:: cmake

  if(NOT EXISTS "${CMAKE_TOOLCHAIN_FILE}")
    set_target_properties(boo PROPERTIES CXX_STANDARD 14)
    target_compile_features(foo PUBLIC cxx_constexpr)
  endif()
