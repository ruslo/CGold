.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Static + shared
===============

Those users who has worked with autotools knows that it's possible to build
both static and shared libraries at one go. Here is an overview how it should
be done in CMake.

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/library-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/library-examples/archive/master.zip>`__

Right way
---------

We will start with the right one. Command `add_library`_ should be used without
``STATIC`` or ``SHARED`` specifier, type of the library will be determined by
value of `BUILD_SHARED_LIBS`_ variable (default type is static):

.. literalinclude:: /examples/library-examples/right-way/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

.. note::

  ``STATIC``/``SHARED``/``MODULE`` specifiers should be used only in cases
  when other type of library is by design not possible for any reasons.
  That's not our case of course since we are trying to build both variants,
  hence library designed to be used as static or shared.

Libraries should be installed to separate directories. So there
will be **two builds** and **two root directories**.
:ref:`Out of source <out-of-source>` will kindly help us:

.. code-block:: shell
  :emphasize-lines: 3, 11, 13, 21

  > cd library-examples
  [library-examples]> rm -rf _builds _install
  [library-examples]> cmake -Hright-way -B_builds/shared -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="`pwd`/_install/configuration-A"
  [library-examples]> cmake --build _builds/shared --target install
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX shared library libfoo.so
  [100%] Built target foo
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../library-examples/_install/configuration-A/lib/libfoo.so

  [library-examples]> cmake -Hright-way -B_builds/static -DCMAKE_INSTALL_PREFIX="`pwd`/_install/configuration-B"
  [library-examples]> cmake --build _builds/static --target install
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX static library libfoo.a
  [100%] Built target foo
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../library-examples/_install/configuration-B/lib/libfoo.a

Autotools two builds
~~~~~~~~~~~~~~~~~~~~

Note that autotools do build library twice too under the hood, so performance
is the same:

.. code-block:: shell
  :emphasize-lines: 6, 9-10

  > mkdir temp
  > cd temp
  [temp]> wget http://www.x.org/releases/individual/lib/libpciaccess-0.13.4.tar.bz2
  [temp]> tar xf libpciaccess-0.13.4.tar.bz2
  [temp]> cd libpciaccess-0.13.4
  [libpciaccess-0.13.4]> ./configure --enable-shared --enable-static
  [libpciaccess-0.13.4]> make V=1
  ...
  libtool: compile:  gcc ... -c linux_devmem.c -fPIC -o .libs/linux_devmem.o
  libtool: compile:  gcc ... -c linux_devmem.c -o linux_devmem.o

Install to one directory
------------------------

Another autotools feature is that both libraries will be installed to the one
directory. That's works fine on Linux since libraries names will be
``libfoo.so`` and ``libfoo.a``, works fine for OSX since libraries names will be
``libfoo.dylib`` and ``libfoo.a``, but not for Windows. Static build will
produce ``foo.lib``:

.. code-block:: bat
  :emphasize-lines: 7

  > cd library-examples
  [library-examples]> rmdir _builds _install /S /Q
  [library-examples]> cmake -Hright-way -B_builds\static -G "Visual Studio 14 2015" -DCMAKE_INSTALL_PREFIX=%cd%\_install
  [library-examples]> cmake --build _builds\static --config Release --target install
  ...
  -- Install configuration: "Release"
  -- Installing: C:/.../library-examples/_install/lib/foo.lib

But shared build will produce **both** ``foo.lib`` and ``foo.dll``, effectively
**overwriting** static library and making it **unusable**:

.. code-block:: bat
  :emphasize-lines: 5-6

  [library-examples]> cmake -Hright-way -B_builds\shared -G "Visual Studio 14 2015" -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=%cd%\_install
  [library-examples]> cmake --build _builds\shared --config Release --target install
  ...
  -- Install configuration: "Release"
  -- Installing: C:/.../library-examples/_install/lib/foo.lib
  -- Installing: C:/.../library-examples/_install/bin/foo.dll

Configs
~~~~~~~

Even if libraries doesn't conflict on file level their **configs** will conflict:

.. code-block:: shell
  :emphasize-lines: 5-7

  > cd library-examples
  [library-examples]> rm -rf _install _builds
  [library-examples]> cmake -Hbar -B_builds/shared -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
  [library-examples]> cmake --build _builds/shared --target install
  [library-examples]> grep lib/libbar.so -IR _install
  _install/lib/cmake/bar/barTargets-release.cmake:  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libbar.so"
  _install/lib/cmake/bar/barTargets-release.cmake:list(APPEND _IMPORT_CHECK_FILES_FOR_bar::bar "${_IMPORT_PREFIX}/lib/libbar.so" )

Config for static variant will have the same ``barTargets-release.cmake`` name:

.. code-block:: shell
  :emphasize-lines: 3-5

  [library-examples]> cmake -Hbar -B_builds/static -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
  [library-examples]> cmake --build _builds/static --target install
  [library-examples]> grep lib/libbar.a -IR _install
  _install/lib/cmake/bar/barTargets-release.cmake:  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libbar.a"
  _install/lib/cmake/bar/barTargets-release.cmake:list(APPEND _IMPORT_CHECK_FILES_FOR_bar::bar "${_IMPORT_PREFIX}/lib/libbar.a" )

Now since configuration files for shared variant are overwritten there is
no way to load ``libbar.so`` using ``find_package(bar CONFIG REQUIRED)``.

.. code-block:: shell

  [library-examples]> grep lib/libbar.so -IR _install
  [library-examples]> echo $?
  1

Two targets
-----------

Problems with two versions of library described in previous section can be
solved by using two different targets. This section cover building of two
targets simultaneously. One target build at the time is equivalent to this code:

.. code-block:: cmake

  add_library(foo foo.cpp)

Even if names differs, e.g. by using ``option``:

.. code-block:: cmake

  option(FOO_STATIC_LIB "Build static library" ON)

  if(FOO_STATIC_LIB)
    add_library(foo_static STATIC foo.cpp)
  else()
    add_library(foo_shared SHARED foo.cpp)
  endif()

.. warning::

  This is logically equivalent to the ``add_library(foo foo.cpp)`` +
  ``BUILD_SHARED_LIBS`` functionality so **should not be used**.
  Use standard CMake features!

So assuming we have code like this:

.. code-block:: cmake

  # Don't do that!
  add_library(foo_static STATIC foo.cpp)
  add_library(foo_shared SHARED foo.cpp)

Philosophical
~~~~~~~~~~~~~

CMake code describe **abstract** configuration. User can choose how this
abstraction used on practice. Let's run this example on OSX:

.. literalinclude:: /examples/library-examples/custom/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

By default we will build executable and static library:

.. code-block:: shell

  > cd library-examples
  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hcustom -B_builds
  [library-examples]> cmake --build _builds
  [library-examples]> ls _builds/libfoo.a _builds/boo
  _builds/libfoo.a
  _builds/boo

But we are free to switch to shared library:

.. code-block:: shell

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hcustom -B_builds -DBUILD_SHARED_LIBS=ON
  [library-examples]> cmake --build _builds
  [library-examples]> ls _builds/libfoo.dylib _builds/boo
  _builds/libfoo.dylib
  _builds/boo

Create bundle:

.. code-block:: shell

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hcustom -B_builds -DCMAKE_MACOSX_BUNDLE=ON
  [library-examples]> cmake --build _builds
  [library-examples]> ls -d _builds/libfoo.a _builds/boo.app
  _builds/libfoo.a
  _builds/boo.app

Or do the both:

.. code-block:: shell

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hcustom -B_builds -DCMAKE_MACOSX_BUNDLE=ON -DBUILD_SHARED_LIBS=ON
  [library-examples]> cmake --build _builds
  [library-examples]> ls -d _builds/libfoo.dylib _builds/boo.app
  _builds/libfoo.dylib
  _builds/boo.app

Forcing any of this violates customization principle.

Non-default behavior
~~~~~~~~~~~~~~~~~~~~

Let's see how two targets approach will be used on user's side:

.. literalinclude:: /examples/library-examples/surprise/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

Targets defined in directory ``boo``:

.. literalinclude:: /examples/library-examples/surprise/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

User builds library and link by default static ``libboo.a`` to ``foo``
executable:

.. code-block:: shell

  > cd library-examples
  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hsurprise -B_builds -DCMAKE_VERBOSE_MAKEFILE=ON
  [library-examples]> cmake --build _builds
  ...
  /usr/bin/c++ -o foo ... boo/libboo.a

User knows that there is ``BUILD_SHARED_LIBS`` variable that change type of
library, so he expects shared in next configuration:

.. code-block:: shell

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hsurprise -B_builds -DCMAKE_VERBOSE_MAKEFILE=ON -DBUILD_SHARED_LIBS=ON

But of course he still got static because type of library is forced:

.. code-block:: shell

  [library-examples]> cmake --build _builds
  /usr/bin/c++ -o foo ... boo/libboo.a

Build time
~~~~~~~~~~

Note that in previous example time of compilation of ``boo`` library
is **doubled**. We are building ``boo.cpp`` **twice** even if we are not
planning to use one of the variants:

.. code-block:: shell
  :emphasize-lines: 5, 13

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hsurprise -B_builds
  [library-examples]> cmake --build _builds
  Scanning dependencies of target boo
  [ 16%] Building CXX object boo/CMakeFiles/boo.dir/boo.cpp.o
  [ 33%] Linking CXX static library libboo.a
  [ 33%] Built target boo
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [ 66%] Linking CXX executable foo
  [ 66%] Built target foo
  Scanning dependencies of target boo_shared
  [ 83%] Building CXX object boo/CMakeFiles/boo_shared.dir/boo.cpp.o
  [100%] Linking CXX shared library libboo_shared.so
  [100%] Built target boo_shared

User of such library pays for something **he doesn't really need**.

PIC conflicts
~~~~~~~~~~~~~

Assume we want to build everything statically but some part of out code
force library to be shared:

.. literalinclude:: /examples/library-examples/use_bar/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 9-10

If ``bar`` is static we will have problem with target ``use_bar_shared`` which
in fact **we don't really interested in**:

.. code-block:: none
  :emphasize-lines: 12-14

  > cd library-examples
  [library-examples]> rm -rf _builds _install
  [library-examples]> cmake -Hbar -B_builds -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
  [library-examples]> cmake --build _builds --target install

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Huse_bar -B_builds -DCMAKE_PREFIX_PATH="`pwd`/_install"
  [library-examples]> cmake --build _builds
  Scanning dependencies of target use_bar_shared
  [ 25%] Building CXX object CMakeFiles/use_bar_shared.dir/use_bar.cpp.o
  [ 50%] Linking CXX shared library libuse_bar_shared.so
  /usr/bin/ld: /.../library-examples/_install/lib/libbar.a(bar.cpp.o):
      relocation R_X86_64_PC32 against symbol `_Z4bar1v' can not be used when
      making a shared object; recompile with -fPIC

.. note::

  Such issue **can't be solved** by library usage requirements since library
  ``bar`` don't know a priory will it be linked to shared library or not.

.. admonition:: Stackoverflow

  * `Why isn't all code compiled position independent? <http://stackoverflow.com/q/813980/2288008>`__

Scalability
~~~~~~~~~~~

Two targets approach doesn't scale. If we have ``add_library(foo foo.cpp)`` we
can do control of such code:

.. code-block:: cmake

  add_library(foo foo.cpp)
  add_executable(boo boo.cpp)
  target_link_libraries(boo PUBLIC foo)

Using ``BUILD_SHARED_LIBS``:

* ``ON`` - executable linked with shared library
* ``OFF`` - executable linked with static library

In this code:

.. code-block:: cmake

  add_library(foo_static STATIC foo.cpp)
  add_library(foo_shared SHARED foo.cpp)

What should we do? Create two targets?

.. code-block:: cmake

  add_executable(boo_static boo.cpp)
  target_link_libraries(boo_static PUBLIC foo_static)

  add_executable(boo_shared boo.cpp)
  target_link_libraries(boo_shared PUBLIC foo_shared)

What if there will be more dependencies?

.. code-block:: cmake

  add_library(foo_static STATIC foo.cpp)
  add_library(foo_shared SHARED foo.cpp)

  add_library(bar_static STATIC foo.cpp)
  add_library(bar_shared SHARED foo.cpp)

  # 1 - shared, 0 - static
  add_executable(boo_0_0 boo.cpp)
  add_executable(boo_0_1 boo.cpp)
  add_executable(boo_1_0 boo.cpp)
  add_executable(boo_1_1 boo.cpp)

  target_link_libraries(boo_0_0 PUBLIC foo_static boo_static)
  target_link_libraries(boo_0_1 PUBLIC foo_static boo_shared)
  target_link_libraries(boo_1_0 PUBLIC foo_shared boo_static)
  target_link_libraries(boo_1_1 PUBLIC foo_shared boo_shared)

Duplication
~~~~~~~~~~~

Additionally to scalability problems in previous example we have a risk
to have same code repeated twice for system with complex dependencies. Assume
we have library ``bar`` in two variants simultaneously:

.. literalinclude:: /examples/library-examples/dup/bar/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

And target ``baz`` that for some reason decide that shared variant of linkage
is preferable:

.. literalinclude:: /examples/library-examples/dup/baz/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

Our executable links to both libraries. Probably we don't know/not interested
in fact that ``baz`` use ``bar`` too. We decide that static linkage is
preferable for any reason:

.. literalinclude:: /examples/library-examples/dup/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8

Let's build it:

.. code-block:: shell

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hdup -B_builds
  [library-examples]> cmake --build _builds

We are linked to the ``libbaz.so`` and we **do linked** to ``libbar_shared.so``
because it's dependency of ``baz``:

.. code-block:: shell
  :emphasize-lines: 2, 4-5

  > ldd _builds/foo
    ...
    libbaz.so => /.../library-examples/_builds/baz/libbaz.so (0x00007f6d2f2a4000)
    libbar_shared.so => /.../library-examples/_builds/bar/libbar_shared.so (0x00007f6d2e927000)

At the same time we have ``bar`` linked statically:

.. code-block:: shell
  :emphasize-lines: 2, 5

  > objdump -d _builds/foo | grep -A5 'barv.*:'
  0000000000400c12 <_Z3barv>:
    400c12:       55                      push   %rbp
    400c13:       48 89 e5                mov    %rsp,%rbp
    400c16:       b8 42 00 00 00          mov    $0x42,%eax
    400c1b:       5d                      pop    %rbp
    400c1c:       c3                      retq

So effectively code of function ``bar`` present in our dependencies twice!
First time in executable and second time in linked shared library:

.. code-block:: shell
  :emphasize-lines: 2, 5

  > objdump -d _builds/bar/libbar_shared.so | grep -A5 'barv.*:'
  0000000000000610 <_Z3barv>:
   610:   55                      push   %rbp
   611:   48 89 e5                mov    %rsp,%rbp
   614:   b8 42 00 00 00          mov    $0x42,%eax
   619:   5d                      pop    %rbp
   61a:   c3                      retq

Summary
-------

* Use ``STATIC``/``SHARED``/``MODULE`` only if **library designed**
  to have no other types
* Use **no specifiers** if library designed to be used as static or shared.
  Respect ``BUILD_SHARED_LIBS`` variable
* Install static and shared libraries to **separate directories**

.. admonition:: Stackoverflow

  * `Build static + shared <http://stackoverflow.com/a/18551243/2288008>`__
  * `Recompiling source twice <http://stackoverflow.com/a/22269819/2288008>`__

.. admonition:: CMake mailing list

  * `Static & shared library <https://cmake.org/pipermail/cmake/2005-August/007030.html>`__

.. _add_library: https://cmake.org/cmake/help/latest/command/add_library.html
.. _BUILD_SHARED_LIBS: https://cmake.org/cmake/help/latest/variable/BUILD_SHARED_LIBS.html
