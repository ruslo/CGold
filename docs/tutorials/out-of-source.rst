.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _out-of-source:

Out-of-source build
===================

The next important term is "out-of-source build". "Out-of-source build" is a
good practice of keeping separate the generated files of the
:ref:`binary tree <binary tree>` from the source files of the
:ref:`source tree <source tree>`. CMake does support the contrary "in-source build"
layout, but such an approach has no real benefit and is not recommended.

.. _out-of-source-config:

Multiple configurations
-----------------------

An out-of-source build allows you to have different configurations simultaneously
without conflicts, e.g. Debug and Release variants:

.. code-block:: none

  > cmake -H. -B_builds/Debug -DCMAKE_BUILD_TYPE=Debug
  > cmake -H. -B_builds/Release -DCMAKE_BUILD_TYPE=Release

or any other kind of customization, e.g. options:

.. code-block:: none

  > cmake -H. -B_builds/feature-on -DFOO_FEATURE=ON
  > cmake -H. -B_builds/feature-off -DFOO_FEATURE=OFF

generators:

.. code-block:: none

  > cmake -H. -B_builds/xcode -G Xcode
  > cmake -H. -B_builds/make -G "Unix Makefiles"

platforms:

.. code-block:: none

  > cmake -H. -B_builds/osx -G Xcode
  > cmake -H. -B_builds/ios -G Xcode -DCMAKE_TOOLCHAIN_FILE=/.../ios.cmake

VCS friendly
------------

An out-of-source build allows you to ignore temporary binaries by just adding
the ``_builds`` directory to the no-tracking-files list:

.. code-block:: none

  # .gitignore

  _builds

compare it with the entries required for an in-source build:

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

An in-source build at first glance may look more friendly for developers
who are used to storing project/solution files in :ref:`VCS <VCS>`. But in fact
an out-of-source build will remind you one more time that now your workflow has
changed, CMake is in charge and :ref:`you should not <affecting workflow>` edit
your project settings in your IDE.

Another note is that using an out-of-source build means that not only do you
need to set ``cmake -B_builds`` but also remember that you have to put any
kind of automatically generated files into ``_builds``.
E.g. if you have a C++ template ``myproject.h.in`` which is used to generate
``myproject.h``, then you need to keep ``myproject.h.in`` in the source tree
and put ``myproject.h`` in the binary tree.
