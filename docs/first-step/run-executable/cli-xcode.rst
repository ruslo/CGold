.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Xcode
----------

To build Xcode project from command line ``xcodebuild`` can be used.
Check it can be found:

.. code-block:: shell

  > which xcodebuild
  /usr/bin/xcodebuild

Go to the ``_builds`` directory and run build:

.. code-block:: shell

  > cd _builds
  [cgold-example/_builds]> xcodebuild
  ...

  echo Build\ all\ projects
  Build all projects

  ** BUILD SUCCEEDED **

But CMake offer cross-tool way to do exactly the same by ``cmake --build _builds``:

.. code-block:: shell

  [cgold-example]> cmake --build _builds
  ...

  echo Build\ all\ projects
  Build all projects

  ** BUILD SUCCEEDED **

By default Debug variant of ``foo`` will be build, you can run it by:

.. code-block:: shell

  [cgold-example]> ./_builds/Debug/foo
  Hello from CGold!

Done!
