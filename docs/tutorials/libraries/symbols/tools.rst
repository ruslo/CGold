.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Tools
=====

The tool for listing symbols differs for different platforms.

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/library-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/library-examples/archive/master.zip>`__

Example
-------

Here is an example of library which has both defined and undefined symbols:

.. literalinclude:: /examples/library-examples/library-symbols/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

Method ``Boo::boo`` declared and will be defined:

.. literalinclude:: /examples/library-examples/library-symbols/Boo.hpp
  :language: cpp
  :emphasize-lines: 8

.. literalinclude:: /examples/library-examples/library-symbols/Boo.cpp
  :language: cpp
  :emphasize-lines: 7

Method ``Foo::foo`` declared, will be used but **will not be** defined:

.. literalinclude:: /examples/library-examples/library-symbols/Foo.hpp
  :language: cpp
  :emphasize-lines: 8

.. literalinclude:: /examples/library-examples/library-symbols/Boo.cpp
  :language: cpp
  :emphasize-lines: 5, 10

Build library:

.. code-block:: none
  :emphasize-lines: 2, 21, 24, 27-28

  [library-examples]> rm -rf _builds
  [library-examples]> cmake -Hlibrary-symbols -B_builds
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
  [ 50%] Building CXX object CMakeFiles/boo.dir/Boo.cpp.o
  [100%] Linking CXX static library libboo.a
  [100%] Built target boo

  [library-examples]> ls _builds/libboo.a
  _builds/libboo.a

Linux
-----

Use ``nm`` for Linux:

.. code-block:: none
  :emphasize-lines: 2

  > which nm
  /usr/bin/nm

Install instructions for Ubuntu:

.. code-block:: none

  > sudo apt-get install binutils

``nm --defined-only`` will show symbols defined by current module.
Add ``--demangle`` to beautify output:

.. code-block:: none
  :emphasize-lines: 1, 4

  [library-examples]> nm --defined-only --demangle _builds/libboo.a

  Boo.cpp.o:
  0000000000000000 T Boo::boo(int, char)

``nm --undefined-only`` will show undefined:

.. code-block:: none
  :emphasize-lines: 1, 5

  [library-examples]> nm --undefined-only --demangle _builds/libboo.a

  Boo.cpp.o:
                   U __stack_chk_fail
                   U Foo::foo(char, double)

OSX
---

Same ``nm`` tool with ``--defined-only``/``--undefined-only`` options can be
used on ``OSX`` platform. However ``--demangle`` is not available, ``c++filt``
can be used instead:

.. code-block:: none
  :emphasize-lines: 2, 5

  > which nm
  /usr/bin/nm

  > which c++filt
  /usr/bin/c++filt

Defined symbols:

.. code-block:: none
  :emphasize-lines: 1, 4

  > nm --defined-only _builds/libboo.a | c++filt

  _builds/libboo.a(Boo.cpp.o):
  0000000000000000 T Boo::boo(int, char)

Undefined symbols:

.. code-block:: none
  :emphasize-lines: 1, 4

  > nm --undefined-only _builds/libboo.a | c++filt

  _builds/libboo.a(Boo.cpp.o):
  Foo::foo(char, double)

Windows
-------

``DUMPBIN`` tool can help to discover symbols on Windows platform. It's
available via :ref:`Developer Command Prompt <developer command prompt>`:

.. code-block:: none

  > where dumpbin
  ...\msvc\2015\VC\bin\dumpbin.exe

Add ``/SYMBOLS`` to see the table. Defined symbols can be filtered by
``External`` + ``SECT``:

.. code-block:: none
  :emphasize-lines: 2

  [library-examples]> dumpbin /symbols _builds\Debug\boo.lib | findstr "External" | findstr "SECT"
  00A 00000000 SECT4  notype ()    External     | ?boo@Boo@@QAEHHD@Z (public: int __thiscall Boo::boo(int,char))
  01C 00000000 SECT7  notype       External     | __real@3ff0000000000000

Undefined by ``External`` + ``UNDEF``:

.. code-block:: none
  :emphasize-lines: 2

  [library-examples]> dumpbin /symbols _builds\Debug\boo.lib | findstr "External" | findstr "UNDEF"
  00B 00000000 UNDEF  notype ()    External     | ?foo@Foo@@QAEHDN@Z (public: int __thiscall Foo::foo(char,double))
  00C 00000000 UNDEF  notype ()    External     | @_RTC_CheckStackVars@8
  00D 00000000 UNDEF  notype ()    External     | __RTC_CheckEsp
  00E 00000000 UNDEF  notype ()    External     | __RTC_InitBase
  00F 00000000 UNDEF  notype ()    External     | __RTC_Shutdown
  019 00000000 UNDEF  notype       External     | __fltused

.. seealso::

  * `DUMPBIN reference <https://msdn.microsoft.com/en-us/library/c1h23y6c.aspx>`__
  * `DUMPBIN /SYMBOLS <https://msdn.microsoft.com/en-us/library/b842y285.aspx>`__

Use ``/EXPORTS`` if you want to see the symbols available in DLL:

.. code-block:: none
  :emphasize-lines: 2

  [library-examples]> dumpbin /exports _builds\Release\boo.dll | findstr "Boo"
    1    0 00001000 ?boo@Boo@@QAEHHD@Z

Use ``undname`` to demangle:

.. code-block:: none
  :emphasize-lines: 1, 6

  [library-examples]> undname ?boo@Boo@@QAEHHD@Z
  Microsoft (R) C++ Name Undecorator
  Copyright (C) Microsoft Corporation. All rights reserved.

  Undecoration of :- "?boo@Boo@@QAEHHD@Z"
  is :- "public: int __thiscall Boo::boo(int,char)"

.. seealso::

  * `DUMPBIN /EXPORTS <https://msdn.microsoft.com/en-us/library/30e78zd0.aspx>`__
  * `Viewing Decorated Names <https://msdn.microsoft.com/en-us/library/5x49w699.aspx>`__
