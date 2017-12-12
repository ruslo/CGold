.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _developer command prompt:

Developer Command Prompt
------------------------

Developer Command Prompt is a Command Prompt with Visual Studio development
tools available in environment:

.. code-block:: none

  > where msbuild
  C:\Program Files (x86)\MSBuild\14.0\Bin\MSBuild.exe
  C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe

  > where cl
  ...\msvc\2015\VC\bin\cl.exe

  > where dumpbin
  ...\msvc\2015\VC\bin\dumpbin.exe

Similar test on regular Command Prompt ``cmd.exe``:

.. code-block:: none

  > where msbuild
  INFO: Could not find files for the given pattern(s).

  > where cl
  INFO: Could not find files for the given pattern(s).

  > where dumpbin
  INFO: Could not find files for the given pattern(s).

.. note::

  There is no need to use Developer Command Prompt for running CMake with
  ``Visual Studio`` generators, corresponding environment will be loaded
  automatically by CMake. But for other generators like ``NMake`` or ``Ninja``
  you should start CMake from Developer Command Prompt.

.. seealso::

  * :doc:`Visual Studio </first-step/native-build-tool/visual-studio>`
  * `Developer Command Prompt for Visual Studio <https://msdn.microsoft.com/en-us/library/ms229859(v=vs.110).aspx>`__
