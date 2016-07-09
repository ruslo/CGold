.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Version and policies
--------------------

Like any other piece of sofware :ref:`CMake <CMake>` evolves, effectively
introducing new features and deprecating dangerous or confusing behaviour.

There are two entities that help you to manage difference between old and new
versions of CMake:

* Command
  `cmake_minimum_required <https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html>`__
  for checking what minimum version of CMake user should have to run your
  configuration

* `CMake policies <https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html>`__
  for fune tuning newly introduced behaviour

cmake_minimum_required
======================

.. seealso::

 * `Official documentation <https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html>`__

What version to put into this command is mostly an executive decision. You
need to know:

* what version is installed on users hosts?
* is it appropriate to ask them to install newer version?
* what features do they need?
* do you need to be backward compatible for one users and have fresh features
  for another?

The last case will fit most of them but will harder to maintain for developer
and probably will require automatic testing system with good coverage.

.. seealso::

  * `CMake versions for Hunter <https://docs.hunter.sh/en/latest/quick-start/cmake.html>`__

For example the code with version ``2.8`` as a minimum one and with ``3.0``
features will look like:

.. code-block:: cmake

  cmake_minimum_required(VERSION 2.8)

  if(NOT CMAKE_VERSION VERSION_LESS "3.0") # means 'NOT version < 3.0', i.e. 'version >= 3.0'
    # Code with 3.0 features
  endif()

For the test or preliminary project you can just set the current version
you're using.

Command ``cmake_minimum_required`` **must be the first** command in your
:ref:`CMakeLists.txt <cmakelists.txt>`. If you're planning to support several
versions of CMake then you need to put the smallest one in
``cmake_minimum_required`` and call it in the first line of CMakeLists.txt.

Even if some commands look harmless at the first glance it may be not so
in fact, e.g. ``project`` is the place where a lot of checks happens and where
toolchain is loaded. If you run this example on ``Cygwin`` platform:

.. literalinclude:: /examples/minimum-required-example/bad/CMakeLists.txt
  :language: cmake

CMake will think that you're running code with old policies and warns you:

.. code-block:: shell

  [minimum-required-example]> cmake -Hbad -B_builds/bad
  -- The C compiler identification is GNU 4.9.3
  -- The CXX compiler identification is GNU 4.9.3
  CMake Warning at /.../share/cmake-3.3.1/Modules/Platform/CYGWIN.cmake:15 (message):
    CMake no longer defines WIN32 on Cygwin!

    (1) If you are just trying to build this project, ignore this warning or
    quiet it by setting CMAKE_LEGACY_CYGWIN_WIN32=0 in your environment or in
    the CMake cache.  If later configuration or build errors occur then this
    project may have been written under the assumption that Cygwin is WIN32.
    In that case, set CMAKE_LEGACY_CYGWIN_WIN32=1 instead.

    (2) If you are developing this project, add the line

      set(CMAKE_LEGACY_CYGWIN_WIN32 0) # Remove when CMake >= 2.8.4 is required

    at the top of your top-level CMakeLists.txt file or set the minimum
    required version of CMake to 2.8.4 or higher.  Then teach your project to
    build on Cygwin without WIN32.
  Call Stack (most recent call first):
    /.../share/cmake-3.3.1/Modules/CMakeSystemSpecificInformation.cmake:36 (include)
    CMakeLists.txt:1 (project)
  ...
  -- Detecting CXX compile features - done
  Using CMake version 3.3.1
  ...

Fixed version:

.. literalinclude:: /examples/minimum-required-example/good/CMakeLists.txt
  :language: cmake

with no warnings:

.. code-block:: bash

  [minimum-required-example]> cmake -Hgood -B_builds/good
  -- The C compiler identification is GNU 4.9.3
  -- The CXX compiler identification is GNU 4.9.3
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /usr/bin/c++.exe
  -- Check for working CXX compiler: /usr/bin/c++.exe -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  Using CMake version 3.3.1
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../minimum-required-example/_builds/good

.. seealso::

  * `Example on GitHub <https://github.com/cgold-examples/minimum-required-example>`__
  * Archive with latest version: `zip <https://github.com/cgold-examples/minimum-required-example/archive/master.zip>`__

CMake policies
==============

.. seealso::

 * `Official documentation <https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html>`__
