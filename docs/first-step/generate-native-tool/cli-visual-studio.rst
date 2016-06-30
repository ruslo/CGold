.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Visual Studio
------------------

Run ``cmd.exe`` and go to the directory with sources:

.. code-block:: shell

  > cd C:\cgold-example

  [cgold-example]> dir

  ... CMakeLists.txt
  ... foo.cpp

Generate Visual Studio solution using CMake. Use:

* ``-H.`` for specifying current directory as a directory with ``CMakeLists.txt``
* ``-B_builds`` where should we put generated files
* ``-G "Visual Studio 14 2015 Win64"`` for the generator

.. code-block:: shell

  [cgold-example]> cmake -H. -B_builds -G "Visual Studio 14 2015 Win64"
  -- The C compiler identification is MSVC 19.0.23918.0
  -- The CXX compiler identification is MSVC 19.0.23918.0
  -- Check for working C compiler using: Visual Studio 14 2015 Win64
  -- Check for working C compiler using: Visual Studio 14 2015 Win64 -- works
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Check for working CXX compiler using: Visual Studio 14 2015 Win64
  -- Check for working CXX compiler using: Visual Studio 14 2015 Win64 -- works
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- Configuring done
  -- Generating done
  -- Build files have been written to: C:/cgold-example/_builds

You can start IDE by ``start _builds\foo.sln`` and
:doc:`run example from IDE </first-step/run-executable/ide-visual-studio>`
or :doc:`keep using command line </first-step/run-executable/cli-visual-studio>`.
