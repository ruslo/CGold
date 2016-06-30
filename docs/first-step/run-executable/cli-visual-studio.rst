.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Visual Studio
------------------

To build Visual Studio solution from command line ``MSBuild.exe`` can be used.
You must add ``MSBuild.exe`` location to PATH or open Visual Studio Developer
Prompt instead of ``cmd.exe`` (run ``where msbuild`` to check)  and run
``msbuild _builds\foo.sln``

But CMake offer cross-tool way to do exactly the same: ``cmake --build _builds``
(no need to have ``MSBuild.exe`` in PATH).

.. code-block:: shell

  [cgold-example]> cmake --build _builds

  ...

  Build succeeded.
      0 Warning(s)
      0 Error(s)

  Time Elapsed 00:00:01.54

By default Debug variant of ``foo.exe`` will be build, you can run it by:

.. code-block:: shell

  [cgold-example]> .\_builds\Debug\foo.exe
  Hello from CGold!

Done!
