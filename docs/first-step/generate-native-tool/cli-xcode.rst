.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Xcode
----------

Open terminal and go to the directory with sources:

.. code-block:: none

  > cd cgold-example
  [cgold-example]> ls
  CMakeLists.txt foo.cpp

Generate Xcode project using CMake. Use
:ref:`-S. <-S>` :ref:`-B_builds <-B>` for specifying paths
and ``-GXcode`` for the generator:

.. code-block:: none
  :emphasize-lines: 1, 18

  [cgold-example]> cmake -S. -B_builds -GXcode
  -- The C compiler identification is AppleClang 7.3.0.7030031
  -- The CXX compiler identification is AppleClang 7.3.0.7030031
  -- Check for working C compiler: /.../Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang
  -- Check for working C compiler: /.../Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Check for working CXX compiler: /.../Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++
  -- Check for working CXX compiler: /.../Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /Users/ruslo/cgold-example/_builds

You can start IDE by ``open _builds/foo.xcodeproj`` (add ``-a`` to set
the version of Xcode you need:
``open -a /Applications/develop/ide/xcode/6.4/Xcode.app _builds/foo.xcodeproj``)
and :doc:`run example from IDE </first-step/run-executable/ide-xcode>`
or :doc:`keep using command line </first-step/run-executable/cli-xcode>`.
