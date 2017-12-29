.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

Link order
----------

GNU linker
==========

This problem occurs only when you're using GNU linker. From ``man ld`` on
Linux:

.. code-block:: none

   The linker will search an archive only once, at the location where it is
   specified on the command line.  If the archive defines a symbol which was
   undefined in some object which appeared before the archive on the command
   line, the linker will include the appropriate file(s) from the archive.
   However, an undefined symbol in an object appearing later on the command
   line will not cause the linker to search the archive again.

There is no such issue on OSX for example, quote from ``man ld``:

.. code-block:: none

  ld will only pull .o files out of a static library if needed to resolve
  some symbol reference.  Unlike traditional linkers, ld will continually
  search a static library while linking. There is no need to specify a
  static library multiple times on the command line.

Example tested on Linux with GCC compiler and standard ``ld`` linker:

.. code-block:: none
  :emphasize-lines: 1-2, 8-9

  > ld --version
  GNU ld (GNU Binutils for Ubuntu) 2.26.1
  Copyright (C) 2015 Free Software Foundation, Inc.
  This program is free software; you may redistribute it under the terms of
  the GNU General Public License version 3 or (at your option) a later version.
  This program has absolutely no warranty.

  > gcc --version
  gcc (Ubuntu 5.4.1-2ubuntu1~16.04) 5.4.1 20160904
  Copyright (C) 2015 Free Software Foundation, Inc.
  This is free software; see the source for copying conditions.  There is NO
  warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Problem
=======

Example with two libraries ``bar``, ``boo`` and executable ``foo``:

.. literalinclude:: /examples/library-examples/link-order-bad/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6, 7, 9

Library ``bar`` doesn't depend on anything and define function ``int bar()``:

.. literalinclude:: /examples/library-examples/link-order-bad/bar.cpp
  :language: cpp
  :emphasize-lines: 3-5

Library ``boo`` depends on ``bar`` and define function ``int boo()``:

.. literalinclude:: /examples/library-examples/link-order-bad/boo.cpp
  :language: cpp
  :emphasize-lines: 5-7

Executable ``foo`` depends on ``boo``:

.. literalinclude:: /examples/library-examples/link-order-bad/foo.cpp
  :language: cpp
  :emphasize-lines: 5-7

Build will fail with linker error:

.. code-block:: none
  :emphasize-lines: 2, 20, 40, 42-45

  [examples]> rm -rf _builds
  [examples]> cmake -Hlibrary-examples/link-order-bad -B_builds -DCMAKE_VERBOSE_MAKEFILE=ON
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
  ...
  [ 16%] Building CXX object CMakeFiles/bar.dir/bar.cpp.o
  /usr/bin/c++     -o CMakeFiles/bar.dir/bar.cpp.o -c /.../examples/library-examples/link-order-bad/bar.cpp
  [ 33%] Linking CXX static library libbar.a
  ...
  /usr/bin/ar qc libbar.a  CMakeFiles/bar.dir/bar.cpp.o
  /usr/bin/ranlib libbar.a
  [ 33%] Built target bar
  ...
  [ 50%] Building CXX object CMakeFiles/boo.dir/boo.cpp.o
  /usr/bin/c++     -o CMakeFiles/boo.dir/boo.cpp.o -c /.../examples/library-examples/link-order-bad/boo.cpp
  [ 66%] Linking CXX static library libboo.a
  ...
  /usr/bin/ar qc libboo.a  CMakeFiles/boo.dir/boo.cpp.o
  /usr/bin/ranlib libboo.a
  [ 66%] Built target boo
  ...
  [ 83%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  /usr/bin/c++     -o CMakeFiles/foo.dir/foo.cpp.o -c /.../examples/library-examples/link-order-bad/foo.cpp
  [100%] Linking CXX executable foo
  ...
  /usr/bin/c++    -rdynamic CMakeFiles/foo.dir/foo.cpp.o  -o foo libbar.a libboo.a
  libboo.a(boo.cpp.o): In function `boo()':
  boo.cpp:(.text+0x5): undefined reference to `bar()'
  collect2: error: ld returned 1 exit status
  ...

Note that linker can't find symbol ``int bar()`` from ``bar`` library even
if ``libbar.a`` is present in command line.

To understand the reason of error you have to understand how linker works:

* All files passed to linker processed from **left to right**
* Linker **collects undefined symbols** from files to the pool of undefined
  symbols
* If object from archive doesn't resolve any symbols from pool of undefined
  symbols, then **it dropped**

Next thing happens in example above:

* 3 files passed to linker to create final ``foo`` executable:

  * object ``CMakeFiles/foo.dir/foo.cpp.o``
  * archive ``libbar.a``
  * archive ``libboo.a``

* ``CMakeFiles/foo.dir/foo.cpp.o`` has undefined symbol ``int boo()``.
  Current pool of undefined symbols is ``int boo()``

* Archive ``libbar.a`` defines ``int bar()``, doesn't have any undefined
  symbols and doesn't resolve any symbols from pool. Hence **we drop it**.
  Current pool of undefined symbols is ``int boo()``

* Archive ``libboo.a`` defines ``int boo()`` and has undefined symbol
  ``int bar()``. ``int boo()`` removed from pool and ``int bar()`` added.
  Current pool of undefined symbols is ``int bar()``

* No files left. Pool of undefined symbols is not empty and error about
  unresolved ``int bar()`` symbol reported.

Fix
===

To fix this you should declare dependency between ``boo`` and ``bar``:

.. literalinclude:: /examples/library-examples/link-order-fix/CMakeLists.txt
  :diff: /examples/library-examples/link-order-bad/CMakeLists.txt

This approach both clean (``foo`` doesn't explicitly depends on ``bar``, why
``target_link_libraries(foo PUBLIC bar)`` used?) and correct - CMake will
control the right order of files:

.. code-block:: none
  :emphasize-lines: 2, 20, 22

  [examples]> rm -rf _builds
  [examples]> cmake -Hlibrary-examples/link-order-fix -B_builds -DCMAKE_VERBOSE_MAKEFILE=ON
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
  ...
  /usr/bin/c++    -rdynamic CMakeFiles/foo.dir/foo.cpp.o  -o foo libboo.a libbar.a
  make[2]: Leaving directory '/.../examples/_builds'
  [100%] Built target foo
  make[1]: Leaving directory '/.../examples/_builds'
  /home/ruslo/work/_ci/cmake/bin/cmake -E cmake_progress_start /.../examples/_builds/CMakeFiles 0

Summary
=======

* If one library depends on symbols from other library you have to express it
  by ``target_link_libraries`` command. Even if you may not have problems
  in current setup they may appear later or on another platform.

* If you have "undefined reference" error even if library with missing symbols
  is present in command line, then it may means that the order is not correct.
  Fix it by adding ``target_link_libraries(boo PUBLIC bar)``, where ``boo``
  is library with unresolved symbols and ``bar`` is library which defines
  those symbols.
