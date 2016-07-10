.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Project declaration
-------------------

Next must-have command is
`project <https://cmake.org/cmake/help/latest/command/project.html>`__.
Command ``project(foo)`` will set languages to C and C++ (default),
declare some ``foo_*`` variables and run build tool checks. If it's sounds
good for you and you don't want to dive into details, put ``project(foo)``
**right after** ``cmake_minimum_required`` in top-level CMakeLists.txt and move
to the :doc:`/tutorials/syntax` section.

.. seealso::

  * `Official documentation <https://cmake.org/cmake/help/latest/command/project.html>`__

Tools discovering
=================

By default on calling ``project`` command CMake will try to detect compilers
for default languages: C and C++. Let's add some variables and check where
they are defined:

.. literalinclude:: /examples/project-examples/set-compiler/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3-5,9-11

.. seealso::

  * `Example on GitHub <https://github.com/cgold-examples/project-examples>`__
  * Archive with latest version: `zip <https://github.com/cgold-examples/project-examples/archive/master.zip>`__

Run test on ``Linux``:

.. code-block:: shell
  :emphasize-lines: 2, 4-5, 9, 15, 21-22

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Hset-compiler -B_builds
  Before 'project':
    C: ''
    C++: ''
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
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
  After 'project':
    C: '/usr/bin/cc'
    C++: '/usr/bin/c++'
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

CMake will run tests for other tools as well, so try to avoid
checking of anything before ``project``, place all checks
**after project declared**.

.. admonition:: Stackoverflow
  :class: tip

  * `Why CMAKE_COMPILER_IS_GNUCXX and CMAKE_CXX_COMPILER_ID are empty? <http://stackoverflow.com/a/20905333/2288008>`__
  * `Why CMAKE_SYSTEM_NAME is blank? <http://stackoverflow.com/a/26437667/2288008>`__
  * `Why MSVC is empty? <http://stackoverflow.com/a/31152886/2288008>`__

Also ``project`` is a place where toolchain file will be read.

CMakeLists.txt:

.. literalinclude:: /examples/project-examples/toolchain/CMakeLists.txt
  :language: cmake

toolchain.cmake:

.. literalinclude:: /examples/project-examples/toolchain/toolchain.cmake
  :language: cmake

.. code-block:: shell
  :emphasize-lines: 2-5, 9, 12, 15-17, 20, 23, 26-28, 30

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Htoolchain -B_builds -DCMAKE_TOOLCHAIN_FILE=toolchain.cmake
  Before 'project'
  Processing toolchain
  Processing toolchain
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
  -- Check for working C compiler: /usr/bin/cc
  Processing toolchain
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  Processing toolchain
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  Processing toolchain
  Processing toolchain
  Processing toolchain
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /usr/bin/c++
  Processing toolchain
  -- Check for working CXX compiler: /usr/bin/c++ -- works
  -- Detecting CXX compiler ABI info
  Processing toolchain
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  Processing toolchain
  Processing toolchain
  Processing toolchain
  -- Detecting CXX compile features - done
  After 'project'
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

.. note::

  You may notice that toolchain read several times

.. admonition:: Stackoverflow
  :class: tip

  * `In which Order are Files parsed (Cache, Toolchain, …)? <http://stackoverflow.com/q/30503631/2288008>`__

Languages
=========

If you don't have or don't need support for one of the default languages you can
set language explicitly by ``LANGUAGE`` sub-option. This is how to setup
C-only project:

.. literalinclude:: /examples/project-examples/c-compiler/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7

There is no checks for C++ compiler and variable with path to C++ compiler
is empty now:

.. code-block:: shell
  :emphasize-lines: 2, 8, 15

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Hc-compiler -B_builds
  Before 'project':
    C: ''
    C++: ''
  -- The C compiler identification is GNU 4.8.4
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  After 'project':
    C: '/usr/bin/cc'
    C++: ''
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

Of course you will not be able to build C++ targets anymore. Since CMake
thinks that ``*.cpp`` extension is for C++ sources (by default) there will
be error reported if C++ is not listed in ``LANGUAGES`` (discovering of C++
tools will not be triggered):

.. literalinclude:: /examples/project-examples/cpp-not-found/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 2, 4

.. code-block:: shell
  :emphasize-lines: 2, 11-12

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Hcpp-not-found -B_builds
  -- The C compiler identification is GNU 4.8.4
  -- Check for working C compiler: /usr/bin/cc
  -- Check for working C compiler: /usr/bin/cc -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Configuring done
  CMake Error: Cannot determine link language for target "foo".
  CMake Error: CMake can not determine linker language for target: foo
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

.. admonition:: Stackoverflow
  :class: tip

  * `Detect project language in cmake <http://stackoverflow.com/a/32390852/2288008>`__

Variables
=========

Command ``project`` declare ``*_{SOURCE,BINARY}_DIR`` variables. Since version
``3.0`` you can add ``VERSION`` which additionally declare
``*_VERSION_{MAJOR,MINOR,PATCH,TWEAK}`` variables:

.. literalinclude:: /examples/project-examples/variables/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 1, 9

.. code-block:: shell
  :emphasize-lines: 2, 4-7, 23-26

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Hvariables -B_builds
  Before project:
    Source:
    Binary:
    Version:
    Version (alt): ..
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
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
  After project:
    Source: /.../project-examples/variables
    Binary: /.../project-examples/_builds
    Version: 1.2.7
    Version (alt): 1.2.7
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

You can use alternative ``foo_{SOURCE,BINARY}_DIRS``/
``foo_VERSION_{MINOR,MAJOR,PATCH}`` synonyms. This is useful
when you have hierarchy of projects:

.. literalinclude:: /examples/project-examples/hierarchy/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6-8

.. literalinclude:: /examples/project-examples/hierarchy/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6-9

.. code-block:: shell
  :emphasize-lines: 22

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Hhierarchy -B_builds
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
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
  From top level:
    Source (general): /.../project-examples/hierarchy
    Source (foo): /.../project-examples/hierarchy
  From subdirectory 'boo':
    Source (general): /.../project-examples/hierarchy/boo
    Source (foo): /.../project-examples/hierarchy
    Source (boo): /.../project-examples/hierarchy/boo
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

As you can see we are still able to use ``foo_*`` variables even if new
command ``project(boo)`` called.

When not declared
=================

CMake will implicitly declare ``project`` in case there is no such command
in top-level CMakeLists.txt. This will be equal to calling ``project``
before any other commands. It means that ``project`` will be called **before**
``cmake_minimum_required`` so can lead to problems described in
:ref:`previous section <cmake_minimum_required should be first>`:

.. literalinclude:: /examples/project-examples/not-declared/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. literalinclude:: /examples/project-examples/not-declared/boo/CMakeLists.txt
  :language: cmake

.. code-block:: shell
  :emphasize-lines: 17

  [project-examples]> rm -rf _builds
  [project-examples]> cmake -Hnot-declared -B_builds
  -- The C compiler identification is GNU 4.8.4
  -- The CXX compiler identification is GNU 4.8.4
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
  Before 'cmake_minimum_required'
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../project-examples/_builds

Summary
=======

* You must have ``project`` command in your top-level ``CMakeLists.txt``
* Use ``project`` to declare nondivisible monolithic hierarchy of targets
* Try to minimize the number of instructions before ``project`` and verify
  that variables are declared in such block of CMake code

.. admonition:: Stackoverflow
  :class: tip

  * `What is the project? <http://stackoverflow.com/a/26882812/2288008>`__
