.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Simple error
------------

Here is an example of trivial "undefined reference" error with diagnostic and,
of course, fix instructions.

Library ``boo``:

.. literalinclude:: /examples/library-examples/link-error/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. literalinclude:: /examples/library-examples/link-error/boo/Boo.hpp
  :language: cpp
  :emphasize-lines: 8

.. literalinclude:: /examples/library-examples/link-error/boo/Boo.cpp
  :language: cpp
  :emphasize-lines: 5-7

Library ``foo`` use library ``boo`` but since we are trying to trigger an error
the ``target_link_libraries`` directive is intentionally missing:

.. literalinclude:: /examples/library-examples/link-error/foo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. literalinclude:: /examples/library-examples/link-error/foo/Foo.hpp
  :language: cpp
  :emphasize-lines: 8

.. literalinclude:: /examples/library-examples/link-error/foo/Foo.cpp
  :language: cpp
  :emphasize-lines: 6-9

Final ``baz`` executable:

.. literalinclude:: /examples/library-examples/link-error/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 11-12

.. literalinclude:: /examples/library-examples/link-error/main.cpp
  :language: cpp
  :emphasize-lines: 1, 4, 5

Generate project:

.. code-block:: none
  :emphasize-lines: 2

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hlink-error -B_builds
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
  -- Build files have been written to: /.../library-examples/_builds

First let's build library ``boo``:

.. code-block:: none
  :emphasize-lines: 1, 7

  [library-examples]> cmake --build _builds --target boo
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../library-examples/_builds
  Scanning dependencies of target boo
  [ 50%] Building CXX object boo/CMakeFiles/boo.dir/Boo.cpp.o
  [100%] Linking CXX static library libboo.a
  [100%] Built target boo

An attempt to build executable ``baz`` will fail with link error:

.. code-block:: none
  :emphasize-lines: 1, 8, 10

  > cmake --build _builds --target baz
  Scanning dependencies of target foo
  [ 25%] Building CXX object foo/CMakeFiles/foo.dir/Foo.cpp.o
  [ 50%] Linking CXX static library libfoo.a
  [ 50%] Built target foo
  Scanning dependencies of target baz
  [ 75%] Building CXX object CMakeFiles/baz.dir/main.cpp.o
  [100%] Linking CXX executable baz
  foo/libfoo.a(Foo.cpp.o): In function `Foo::foo(int, char)':
  Foo.cpp:(.text+0x35): undefined reference to `Boo::boo(int, int)'
  collect2: error: ld returned 1 exit status
  CMakeFiles/baz.dir/build.make:95: recipe for target 'baz' failed
  make[3]: *** [baz] Error 1
  CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/baz.dir/all' failed
  make[2]: *** [CMakeFiles/baz.dir/all] Error 2
  CMakeFiles/Makefile2:79: recipe for target 'CMakeFiles/baz.dir/rule' failed
  make[1]: *** [CMakeFiles/baz.dir/rule] Error 2
  Makefile:118: recipe for target 'baz' failed
  make: *** [baz] Error 2

Use ``nm`` tool to verify that symbol is indeed undefined:

.. code-block:: none
  :emphasize-lines: 1, 5

  > nm --undefined-only --demangle _builds/foo/libfoo.a

  Foo.cpp.o:
                   U __stack_chk_fail
                   U Boo::boo(int, int)

Library ``boo`` has it:

.. code-block:: none
  :emphasize-lines: 1, 4

  > nm --defined-only --demangle _builds/boo/libboo.a

  Boo.cpp.o:
  0000000000000000 T Boo::boo(int, int)

So library ``foo`` depends on library ``boo``, every time we are linking
``foo`` we have to link ``boo`` too. This can be expressed by
``target_link_libraries`` command. Fix:

.. literalinclude:: /examples/library-examples/link-error-fix/foo/CMakeLists.txt
  :diff: /examples/library-examples/link-error/foo/CMakeLists.txt

Should work now:

.. code-block:: none
  :emphasize-lines: 2, 21, 32-33

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hlink-error-fix -B_builds
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
  -- Build files have been written to: /.../library-examples/_builds

  [library-examples]> cmake --build _builds
  Scanning dependencies of target boo
  [ 16%] Building CXX object boo/CMakeFiles/boo.dir/Boo.cpp.o
  [ 33%] Linking CXX static library libboo.a
  [ 33%] Built target boo
  Scanning dependencies of target foo
  [ 50%] Building CXX object foo/CMakeFiles/foo.dir/Foo.cpp.o
  [ 66%] Linking CXX static library libfoo.a
  [ 66%] Built target foo
  Scanning dependencies of target baz
  [ 83%] Building CXX object CMakeFiles/baz.dir/main.cpp.o
  [100%] Linking CXX executable baz
  [100%] Built target baz
