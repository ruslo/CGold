.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _out-of-source:

Out-of-source build
===================

The next important term is "out-of-source build". "Out-of-source build" is a
good practice of keeping separately generated files from
:ref:`build tree <build tree>` and source files from
:ref:`source tree <source tree>`. CMake do support contrary "in-source build"
layout but such approach has no real benefits and unrecommended.

Multiple configurations
-----------------------

Out-of-source build allow you to have different configurations simultaneously
without conflicts, e.g. Debug and Release variant:

.. code-block:: shell

  > cmake -H. -B_builds/Debug -DCMAKE_BUILD_TYPE=Debug
  > cmake -H. -B_builds/Release -DCMAKE_BUILD_TYPE=Release

or any other kind of customization, e.g. options:

.. code-block:: shell

  > cmake -H. -B_builds/feature-on -DFOO_FEATURE=ON
  > cmake -H. -B_builds/feature-off -DFOO_FEATURE=OFF

generators:

.. code-block:: shell

  > cmake -H. -B_builds/xcode -G Xcode
  > cmake -H. -B_builds/make -G "Unix Makefiles"

platforms:

.. code-block:: shell

  > cmake -H. -B_builds/osx -G Xcode
  > cmake -H. -B_builds/ios -G Xcode -DCMAKE_TOOLCHAIN_FILE=/.../ios.cmake

VCS friendly
------------

Out-of-source build allow you to ignore temporary binaries by just adding
``_builds`` directory to the no-tracking-files list:

.. code-block:: none

  # .gitignore

  _builds

compare it with similar file for in-source build:

.. code-block:: none

  # .gitignore

  *.sln
  *.vcxproj
  *.vcxproj.filters
  *.xcodeproj
  CMakeCache.txt
  CMakeFiles
  CMakeScripts
  Debug/*
  Makefile
  Win32/*
  cmake_install.cmake
  foo
  foo.build/*
  foo.dir/*
  foo.exe
  x64/*

Other notes
-----------

In-source build at the first glance may looks more friendly for the developers
who used to store projects/solution files in :ref:`VCS <VCS>`. But in fact
out-of-source build will remind you one more time that now your workflow
changed, CMake is in charge and :ref:`you should not <affecting workflow>` edit
your project settings in IDE.

Another note is that out-of-source mean not only set ``cmake -B_builds`` but
also remember to put any kind of automatically generated files to ``_builds``.
E.g. if you have C++ template ``myproject.h.in`` which is used to generate
``myproject.h``, then you need to keep ``myproject.h.in`` in source tree and put
``myproject.h`` to the build tree.
