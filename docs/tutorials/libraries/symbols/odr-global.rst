.. Copyright (c) 2017, Ruslan Baratov
.. All rights reserved.

ODR violation (global)
----------------------

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/library-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/library-examples/archive/master.zip>`__

Next code shows the ODR violation example based on the same ``#ifdef``
technique but the reason and solution will be different.

Assume we have library ``boo`` which can be used with both C++98 and C++11
standards:

.. literalinclude:: /examples/library-examples/link-error-odr-global/boo/Boo.hpp
  :language: cpp
  :emphasize-lines: 6-8, 12-18

.. literalinclude:: /examples/library-examples/link-error-odr-global/boo/Boo.cpp
  :language: cpp
  :emphasize-lines: 8-12

.. literalinclude:: /examples/library-examples/link-error-odr-global/boo/CMakeLists.txt
  :language: cmake

Library ``foo`` depends on ``boo``:

.. literalinclude:: /examples/library-examples/link-error-odr-global/foo/Foo.hpp
  :language: cpp
  :emphasize-lines: 8

.. literalinclude:: /examples/library-examples/link-error-odr-global/foo/Foo.cpp
  :language: cpp
  :emphasize-lines: 9

Assuming that library ``foo`` use some C++11 features (this fact is not
reflected in C++ code though) first that came to mind is to modify
``CXX_STANDARD`` property:

.. literalinclude:: /examples/library-examples/link-error-odr-global/foo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6

Final executable:

.. literalinclude:: /examples/library-examples/link-error-odr-global/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 11

.. literalinclude:: /examples/library-examples/link-error-odr-global/baz.cpp
  :language: cpp
  :emphasize-lines: 4, 7

Link will fail for the same reason as with previous example. We are not using
C++11 flags while building ``boo`` library but using C++11 flags while building
``foo`` and C++11 flag is analyzed in ``boo/Boo.hpp`` which is loaded by
both targets:

.. code-block:: none
  :emphasize-lines: 8

  [examples]> rm -rf _builds
  [examples]> cmake -Hlibrary-examples/link-error-odr-global -B_builds
  ...
  [examples]> cmake --build _builds
  ...
  [100%] Linking CXX executable baz
  foo/libfoo.a(Foo.cpp.o): In function `Foo::foo()':
  Foo.cpp:(.text+0x52): undefined reference to `Boo::boo(std::thread&)'
  collect2: error: ld returned 1 exit status
  CMakeFiles/baz.dir/build.make:96: recipe for target 'baz' failed
  make[2]: *** [baz] Error 1

Can this issue be fixed using the same approach as
``target_compile_definitions(boo PUBLIC "BOO_USE_SHORT_INT")``? Note that
if we set ``set_target_properties(boo PROPERTIES CXX_STANDARD 11)`` we
can't use ``boo`` with the C++98 targets for the exact same reason, even if
``boo`` is designed to work with both standards.

The main difference here is that ``BOO_USE_SHORT_INT`` is **local** to the
library ``boo`` and hence should be controlled locally (as shown before in
``CMakeLists.txt`` of ``boo`` library). Meanwhile C++98/C++11 flags are
**global** and hence should be declared globally somewhere. In our simple case
where all targets connected together in one project, we can add
``CMAKE_CXX_STANDARD`` to the configure step.

Removing local modification of ``CXX_STANDARD``:

.. literalinclude:: /examples/library-examples/link-error-odr-global-fix/foo/CMakeLists.txt
  :diff: /examples/library-examples/link-error-odr-global/foo/CMakeLists.txt

Building C++11 variant:

.. code-block:: none
  :emphasize-lines: 2, 7

  [examples]> rm -rf _builds
  [examples]> cmake -Hlibrary-examples/link-error-odr-global-fix -B_builds -DCMAKE_CXX_STANDARD=11
  ...
  [examples]> cmake --build _builds
  ...
  [examples]> ./_builds/baz
  Boo: 2011

Building C++98 variant:

.. code-block:: none
  :emphasize-lines: 2, 7

  [examples]> rm -rf _builds
  [examples]> cmake -Hlibrary-examples/link-error-odr-global-fix -B_builds -DCMAKE_CXX_STANDARD=98
  ...
  [examples]> cmake --build _builds
  ...
  [examples]> ./_builds/baz
  Boo: 1998

If we have more complex hierarchy of targets which are sequentially
build/installed, we have to use same ``CMAKE_CXX_STANDARD`` value for each
participating project. ``CMAKE_CXX_STANDARD`` is not the only property with
global nature, it might be helpful to set all such properties/flags in one
place - :doc:`toolchain </tutorials/toolchain>`.

If you still want to set global flags locally for any reason then at least
put the code under ``if`` condition:

.. code-block:: cmake

  if(NOT EXISTS "${CMAKE_TOOLCHAIN_FILE}")
    set(CMAKE_CXX_STANDARD 11)
    set_target_properties(boo PROPERTIES CXX_STANDARD 11)
    # ...
  endif()
