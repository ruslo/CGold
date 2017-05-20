.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

ODR violation (local)
---------------------

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/library-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/library-examples/archive/master.zip>`__

The next example is about scenario when badly written CMake code leads to
:ref:`ODR <odr>` violation.

Assume we have library ``boo``:

.. literalinclude:: /examples/library-examples/link-error-odr-local/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3-4

.. literalinclude:: /examples/library-examples/link-error-odr-local/boo/Boo.hpp
  :language: cpp
  :emphasize-lines: 8-12, 14

.. literalinclude:: /examples/library-examples/link-error-odr-local/boo/Boo.cpp
  :language: cpp
  :emphasize-lines: 5-6

Methods of ``boo`` used in library ``foo``:

.. literalinclude:: /examples/library-examples/link-error-odr-local/foo/Foo.hpp
  :language: cpp
  :emphasize-lines: 8

.. literalinclude:: /examples/library-examples/link-error-odr-local/foo/Foo.cpp
  :language: cpp
  :emphasize-lines: 4, 7-8

.. literalinclude:: /examples/library-examples/link-error-odr-local/foo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

And final executable ``baz``:

.. literalinclude:: /examples/library-examples/link-error-odr-local/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 11

.. literalinclude:: /examples/library-examples/link-error-odr-local/main.cpp
  :language: cpp
  :emphasize-lines: 4

Let's build the project now:

.. code-block:: shell
  :emphasize-lines: 2, 4-5

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hlink-error-odr-local -B_builds -DCMAKE_VERBOSE_MAKEFILE=ON
  ...
  [library-examples]> cmake --build _builds

Link will fail with "undefined reference" error:

.. code-block:: none
  :emphasize-lines: 1, 3, 5, 7

  /usr/bin/c++ -DBOO_USE_SHORT_INT /.../Boo.cpp
  ...
  /usr/bin/c++ /.../Foo.cpp
  ...
  /usr/bin/c++ -rdynamic CMakeFiles/baz.dir/main.cpp.o -o baz foo/libfoo.a boo/libboo.a
  foo/libfoo.a(Foo.cpp.o): In function `Foo::foo(int, int)':
  Foo.cpp:(.text+0x23): undefined reference to `Boo::boo(int, unsigned long long)'
  collect2: error: ld returned 1 exit status
  CMakeFiles/baz.dir/build.make:99: recipe for target 'baz' failed
  make[2]: *** [baz] Error 1

Check symbols we need:

.. code-block:: none
  :emphasize-lines: 4

  [library-examples]> nm --defined-only --demangle _builds/boo/libboo.a

  Boo.cpp.o:
  0000000000000000 T Boo::boo(int, short)

Indeed that's not what we are looking for:

.. code-block:: none
  :emphasize-lines: 4

  [library-examples]> nm --undefined-only --demangle _builds/foo/libfoo.a

  Foo.cpp.o:
      U Boo::boo(int, unsigned long long)

The reason of the failure is that we use ``BOO_USE_SHORT_INT`` while building
``boo`` library and not using it while building library ``foo``. Since in both
cases we are loading ``boo/Boo.hpp`` header (which depends on
``BOO_USE_SHORT_INT``) we should define ``BOO_USE_SHORT_INT`` in both cases too.
`target_compile_definitions <https://cmake.org/cmake/help/latest/command/target_compile_definitions.html>`__
can help us to solve the issue:

.. literalinclude:: /examples/library-examples/link-error-odr-local-fix/boo/CMakeLists.txt
  :diff: /examples/library-examples/link-error-odr-local/boo/CMakeLists.txt

Links fine now:

.. code-block:: none
  :emphasize-lines: 5, 7, 9, 15, 18

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hlink-error-odr-local-fix -B_builds -DCMAKE_VERBOSE_MAKEFILE=ON
  ...
  [library-examples]> cmake --build _builds
  /usr/bin/c++ -DBOO_USE_SHORT_INT /.../Boo.cpp
  ...
  /usr/bin/c++ -DBOO_USE_SHORT_INT /.../Foo.cpp
  ...
  /usr/bin/c++ -DBOO_USE_SHORT_INT /.../main.cpp
  ...
  /usr/bin/c++ -rdynamic CMakeFiles/baz.dir/main.cpp.o -o baz foo/libfoo.a boo/libboo.a
  ...
  > nm --defined-only --demangle _builds/boo/libboo.a
  Boo.cpp.o:
  0000000000000000 T Boo::boo(int, short)
  > nm --undefined-only --demangle _builds/foo/libfoo.a
  Foo.cpp.o:
      U Boo::boo(int, short)
