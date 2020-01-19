.. Copyright (c) 2018, Ruslan Baratov
.. All rights reserved.

Good way
--------

Package manager
~~~~~~~~~~~~~~~

Use system package manager to manage ``a`` and ``b`` dependencies. Install
them to your system and then integrate into CMake using
`find_package <https://cmake.org/cmake/help/latest/command/find_package.html>`__:

.. literalinclude:: /examples/dep-examples/deps-find-package/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 9, 14

.. code-block:: none
  :emphasize-lines: 2

  [examples]> rm -rf _builds
  [examples]> cmake -Hdep-examples/deps-find-package -B_builds -DFOO_WITH_A=ON
  [examples]> cmake --build _builds

Result of running test with module ``a`` enabled:

.. code-block:: none
  :emphasize-lines: 7-8

  [examples]> cd _builds
  [examples/_builds]> ctest -V
  1: Test command: /.../_builds/foo
  1: Test timeout computed to be: 9.99988e+06
  1: Running 'a' module
  1: x say: nice
  1: Running 'b' module
  1: x say: nice
  1/1 Test #1: foo ..............................   Passed    0.00 sec

With module ``a`` disabled:

.. code-block:: none

  [examples]> cmake -Hdep-examples/deps-find-package -B_builds -DFOO_WITH_A=OFF

Third parties remains the same of course, only ``foo`` executable rebuild:

.. code-block:: none

  [examples]> cmake --build _builds
  Scanning dependencies of target foo
  [ 50%] Building CXX object CMakeFiles/foo.dir/foo.cpp.o
  [100%] Linking CXX executable foo
  [100%] Built target foo

Behavior of module ``b`` is the same:

.. code-block:: none
  :emphasize-lines: 7-8

  [examples]> cd _builds
  [examples/_builds]> ctest -V
  1: Test command: /.../_builds/foo
  1: Test timeout computed to be: 9.99988e+06
  1: Running 'a' module
  1: (Module 'a' disabled)
  1: Running 'b' module
  1: x say: nice
  1/1 Test #1: foo ..............................   Passed    0.00 sec

Pros:

* **Locally shareable**. Root directory with libraries can be reused by
  any number of local project.
* **Globally shareable**. Usually dependencies distributed as binaries shared
  across many local machines. You don't have to build all dependencies
  from sources.
* **Option friendly**. Whatever options you've enabled the same set of
  third parties will be used.

Cons:

* **Not much customization** over third party dependencies
* Different system package managers have **different set of packages** and
  available versions
* Usually only **one root** directory

ExternalProject_Add
~~~~~~~~~~~~~~~~~~~

With the help of
`ExternalProject_Add <https://cmake.org/cmake/help/latest/module/ExternalProject.html>`__
module you can create so-called "super-build" project with dependencies:

.. literalinclude:: /examples/dep-examples/deps-super-build/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8-9, 15-16, 23-24

Using such project you can install all dependencies to some custom root
``_ep_install`` directory:

.. code-block:: none
  :emphasize-lines: 2, 8, 12-16, 21, 25-29, 34, 38-42

  [examples]> rm -rf _ep_build
  [examples]> cmake -Hdep-examples/deps-super-build -B_ep_build -DCMAKE_INSTALL_PREFIX=_ep_install
  [examples]> cmake --build _ep_build
  ...
  -- Downloading...
     dst='/.../examples/_ep_build/x-prefix/src/v1.0.tar.gz'
     timeout='none'
  -- Using src='https://github.com/cgold-examples/x/archive/v1.0.tar.gz'
  ...
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../_ep_install/lib/libx.a
  -- Installing: /.../_ep_install/include/x/x.hpp
  -- Installing: /.../_ep_install/lib/cmake/x/xConfig.cmake
  -- Installing: /.../_ep_install/lib/cmake/x/xTargets.cmake
  -- Installing: /.../_ep_install/lib/cmake/x/xTargets-noconfig.cmake
  ...
  -- Downloading...
     dst='/.../examples/_ep_build/a-prefix/src/v1.0.tar.gz'
     timeout='none'
  -- Using src='https://github.com/cgold-examples/a/archive/v1.0.tar.gz'
  ...
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../_ep_install/lib/liba.a
  -- Installing: /.../_ep_install/include/a/a.hpp
  -- Installing: /.../_ep_install/lib/cmake/a/aConfig.cmake
  -- Installing: /.../_ep_install/lib/cmake/a/aTargets.cmake
  -- Installing: /.../_ep_install/lib/cmake/a/aTargets-noconfig.cmake
  ...
  -- Downloading...
     dst='/.../examples/_ep_build/b-prefix/src/v1.0.tar.gz'
     timeout='none'
  -- Using src='https://github.com/cgold-examples/b/archive/v1.0.tar.gz'
  ...
  Install the project...
  -- Install configuration: ""
  -- Installing: /.../_ep_install/lib/libb.a
  -- Installing: /.../_ep_install/include/b/b.hpp
  -- Installing: /.../_ep_install/lib/cmake/b/bConfig.cmake
  -- Installing: /.../_ep_install/lib/cmake/b/bTargets.cmake
  -- Installing: /.../_ep_install/lib/cmake/b/bTargets-noconfig.cmake

Now you can use same ``deps-find-package`` example and inject ``_ep_install``
root directory **with your custom dependencies** instead of system dependencies:

.. code-block:: none
  :emphasize-lines: 2, 5-7

  [examples]> rm -rf _builds
  [examples]> cmake -Hdep-examples/deps-find-package -B_builds -DCMAKE_PREFIX_PATH=/.../examples/_ep_install -DCMAKE_VERBOSE_MAKEFILE=ON
  [examples]> cmake --build _builds
  /usr/bin/c++ ... -o foo
      /.../_ep_install/lib/liba.a
      /.../_ep_install/lib/libb.a
      /.../_ep_install/lib/libx.a

Pros:

* **Locally shareable**. Root directory with libraries can be reused by
  any number of local project.
* **Option friendly**. Whatever options you've enabled the same set of
  third parties will be used.
* **Third party customization**. You have full control over your dependencies.
* **Same set of packages** across all platforms.
* You can create **as many independent root directories as you need**.

Cons:

* Only **build from sources**. There is no built-in mechanism for supporting
  distribution of binaries and meta information. Usually user have to build
  everything from scratch on new machine.
* You have to know everything about your dependencies and carefully manage
  the build order, including implicit dependencies. For example if project ``a``
  depends on ``x`` optionally you have to do something like this:

  .. code-block:: cmake

    option(EP_A_WITH_X "Enable A_WITH_X for 'a' package" ON)

    if(EP_A_WITH_X)
      # We need 'x' project
      ExternalProject_Add(
          x
          ...
      )
      set(a_dependencies x)
    endif()

    ExternalProject_Add(
        a
        ...
        CMAKE_ARGS -DA_WITH_X=${EP_A_WITH_X}
        DEPENDS ${a_dependencies}
    )

  If dependency tree is complex it can be hard to maintain such super-build.
* Writing correct customizable ``ExternalProject_Add`` rules is not a trivial
  task.

Requirements
~~~~~~~~~~~~

Good dependency management system should satisfy next requirements:

* **Locally shareable**. Root directory with libraries should be easily reused
  by any number of local project. CMake has
  `find_package <https://cmake.org/cmake/help/latest/command/find_package.html>`__
  facility for injecting code into project and semi-automatic generation
  of ``XXXConfig.cmake`` configs for consumer (see
  `Creating packages <https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#creating-packages>`__).
  Dependency management system should be friendly to this approach.

* **Globally shareable**. For the performance purposes there should be an
  ability to reuse binaries without building them from sources.
* **Option friendly**. Whatever options you've enabled the same set of
  third parties should be used.
* **Third party customization**. You should have an ability to control the
  way how third party code built: CMake options, CMake build types,
  compiler flags, etc.
