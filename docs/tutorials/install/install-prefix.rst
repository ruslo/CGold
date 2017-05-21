.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CMAKE_INSTALL_PREFIX
--------------------

.. admonition:: CMake documentation

  * `CMAKE_INSTALL_PREFIX <https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html>`__

``CMAKE_INSTALL_PREFIX`` variable can be used to control destination directory
of install procedure:

.. literalinclude:: /examples/install-examples/simple/CMakeLists.txt
  :language: cmake

.. code-block:: none
  :emphasize-lines: 2, 10, 12, 17

  [install-examples]> rm -rf _builds
  [install-examples]> cmake -Hsimple -B_builds -DCMAKE_INSTALL_PREFIX=_install/config-A
  [install-examples]> cmake --build _builds --target install
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX static library libfoo.a
  [100%] Built target foo
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../install-examples/_install/config-A/lib/libfoo.a

  [install-examples]> cmake -Hsimple -B_builds -DCMAKE_INSTALL_PREFIX=_install/config-B
  [install-examples]> cmake --build _builds --target install
  [100%] Built target foo
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../install-examples/_install/config-B/lib/libfoo.a

Modify
======

This variable is designed to be modified on user side. Do not force it in
code!

.. literalinclude:: /examples/install-examples/modify-bad/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

.. code-block:: none
  :emphasize-lines: 2

  [install-examples]> rm -rf _builds
  [install-examples]> cmake -Hmodify-bad -B_builds -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
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
  -- Build files have been written to: /.../install-examples/_builds

Library unexpectedly installed to ``3rdparty/root`` instead of ``_install``:

.. code-block:: none
  :emphasize-lines: 8

  [install-examples]> cmake --build _builds --target install
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX static library libfoo.a
  [100%] Built target foo
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../install-examples/_builds/3rdParty/root/lib/libfoo.a

.. note::

  Use :ref:`CACHE <cache use case>` in such case

On the fly
==========

``Make`` do support changing of install directory on the fly by ``DESTDIR``:

.. code-block:: none
  :emphasize-lines: 3, 7, 10, 14

  [install-examples]> rm -rf _builds
  [install-examples]> cmake -Hsimple -B_builds -DCMAKE_INSTALL_PREFIX=""
  [install-examples]> make -C _builds DESTDIR="`pwd`/_install/config-A" install
  ...
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../install-examples/_install/config-A/lib/libfoo.a
  make: Leaving directory '/.../install-examples/_builds'

  [install-examples]> make -C _builds DESTDIR="`pwd`/_install/config-B" install
  ...
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../install-examples/_install/config-B/lib/libfoo.a
  make: Leaving directory '/.../install-examples/_builds'

Read
====

Because of the ``DESTDIR`` feature, CPack functionality, different nature of
build and install stages often usage of ``CMAKE_INSTALL_PREFIX`` variable
on configure step is an indicator of wrongly written code:

.. literalinclude:: /examples/install-examples/wrong-usage/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8-14

User may not want to install such project at all, so copying of file to root
is something unintended and quite surprising. If you're lucky you will get
problems with permissions on configure step instead of a silent copy:

.. code-block:: none
  :emphasize-lines: 2, 17-20

  [install-examples]> rm -rf _builds
  [install-examples]> cmake -Hwrong-usage -B_builds
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
  CMake Error at CMakeLists.txt:9 (file):
    file COPY cannot copy file
    "/.../install-examples/wrong-usage/README"
    to "/usr/local/share/foo/README".

  -- Configuring incomplete, errors occurred!
  See also "/.../install-examples/_builds/CMakeFiles/CMakeOutput.log".

CPack will use separate directory for install so ``README`` will not be included
in archive:

.. code-block:: none
  :emphasize-lines: 3, 11, 12

  [install-examples]> rm -rf _builds _install
  [install-examples]> cmake -Hwrong-usage -B_builds -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
  [install-examples]> (cd _builds && cpack -G TGZ)
  CPack: Create package using TGZ
  CPack: Install projects
  CPack: - Run preinstall target for: foo
  CPack: - Install project: foo
  CPack: Create package
  CPack: - package: /.../install-examples/_builds/foo-0.1.1-Linux.tar.gz generated.
  [install-examples]> tar xf _builds/foo-0.1.1-Linux.tar.gz
  [install-examples]> find foo-0.1.1-Linux -type f
  foo-0.1.1-Linux/lib/libfoo.a

Implicit read
=============

All work should be delegated to ``install`` command instead, in such case
``CMAKE_INSTALL_PREFIX`` will be read implicitly:

.. literalinclude:: /examples/install-examples/right-usage/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7

.. code-block:: none
  :emphasize-lines: 2

  [install-examples]> rm -rf _builds _install
  [install-examples]> cmake -Hright-usage -B_builds -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
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
  -- Build files have been written to: /.../install-examples/_builds

Correct install directory:

.. code-block:: none
  :emphasize-lines: 8-9

  [install-examples]> cmake --build _builds --target install
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX static library libfoo.a
  [100%] Built target foo
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../install-examples/_install/lib/libfoo.a
  -- Installing: /.../install-examples/_install/share/foo/README

Correct packing:

.. code-block:: none
  :emphasize-lines: 1, 9-11

  [install-examples]> (cd _builds && cpack -G TGZ)
  CPack: Create package using TGZ
  CPack: Install projects
  CPack: - Run preinstall target for: foo
  CPack: - Install project: foo
  CPack: Create package
  CPack: - package: /.../install-examples/_builds/foo-0.1.1-Linux.tar.gz generated.
  [install-examples]> tar xf _builds/foo-0.1.1-Linux.tar.gz
  [install-examples]> find foo-0.1.1-Linux -type f
  foo-0.1.1-Linux/share/foo/README
  foo-0.1.1-Linux/lib/libfoo.a

Install script
==============

Same logic can be applied if ``CMAKE_INSTALL_PREFIX`` used in script created
by ``configure_file`` command:

.. literalinclude:: /examples/install-examples/configure/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7, 9

.. literalinclude:: /examples/install-examples/configure/script.cmake.in
  :language: cmake
  :emphasize-lines: 5, 7, 8

Configure for ``DESTDIR`` usage:

.. code-block:: none
  :emphasize-lines: 2

  [install-examples]> rm -rf _builds _install foo-0.1.1-Linux
  [install-examples]> cmake -Hconfigure -B_builds -DCMAKE_INSTALL_PREFIX=""
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
  -- Build files have been written to: /.../install-examples/_builds

``DESTDIR`` read correctly:

.. code-block:: none
  :emphasize-lines: 1, 5-6, 8-9

  [install-examples]> make DESTDIR="`pwd`/_install/config-A" -C _builds install
  make: Entering directory '/.../install-examples/_builds'
  Install the project...
  -- Install configuration: ""
  Incorrect value: ''
  Correct value: '/.../install-examples/_install/config-A'
  make: Leaving directory '/.../install-examples/_builds'
  [install-examples]> find _install/config-A -type f
  _install/config-A/share/foo/info

Changing directory on the fly:

.. code-block:: none
  :emphasize-lines: 1, 5-6, 8-9

  [install-examples]> make DESTDIR="`pwd`/_install/config-B" -C _builds install
  make: Entering directory '/.../install-examples/_builds'
  Install the project...
  -- Install configuration: ""
  Incorrect value: ''
  Correct value: '/.../install-examples/_install/config-B'
  make: Leaving directory '/.../install-examples/_builds'
  [install-examples]> find _install/config-B -type f
  _install/config-B/share/foo/info

Regular install:

.. code-block:: none
  :emphasize-lines: 2, 20, 23-26

  [install-examples]> rm -rf _builds _install
  [install-examples]> cmake -Hconfigure -B_builds -DCMAKE_INSTALL_PREFIX="`pwd`/_install"
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
  -- Build files have been written to: /.../install-examples/_builds
  [install-examples]> cmake --build _builds --target install
  Install the project...
  -- Install configuration: ""
  Incorrect value: '/.../install-examples/_install'
  Correct value: '/.../install-examples/_install'
  [install-examples]> find _install -type f
  _install/share/foo/info

Packing:

.. code-block:: none
  :emphasize-lines: 1, 6-7, 11-12

  [install-examples]> (cd _builds && cpack -G TGZ)
  CPack: Create package using TGZ
  CPack: Install projects
  CPack: - Run preinstall target for: foo
  CPack: - Install project: foo
  Incorrect value: '/.../install-examples/_install'
  Correct value: '/.../install-examples/_builds/_CPack_Packages/Linux/TGZ/foo-0.1.1-Linux'
  CPack: Create package
  CPack: - package: /.../install-examples/_builds/foo-0.1.1-Linux.tar.gz generated.
  [install-examples]> tar xf _builds/foo-0.1.1-Linux.tar.gz
  [install-examples]> find foo-0.1.1-Linux -type f
  foo-0.1.1-Linux/share/foo/info

Summary
=======

* Do not **force** value of ``CMAKE_INSTALL_PREFIX``
* Use of ``CMAKE_INSTALL_PREFIX`` on configure, generate, build steps is an
  indicator of badly designed code
* Use ``install`` instead of ``CMAKE_INSTALL_PREFIX``
* Respect ``DESTDIR``
