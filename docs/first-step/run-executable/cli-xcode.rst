.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CLI: Xcode
----------

To build an Xcode project from the command line, ``xcodebuild`` can be used.
Check it can be found:

.. code-block:: none

  > which xcodebuild
  /usr/bin/xcodebuild

Go to the ``_builds`` directory and run the build tool:

.. code-block:: none

  > cd _builds
  [cgold-example/_builds]> xcodebuild
  ...

  echo Build\ all\ projects
  Build all projects

  ** BUILD SUCCEEDED **

But CMake offers a cross-tool way to do exactly the same by running ``cmake --build _builds``:

.. code-block:: none

  [cgold-example]> cmake --build _builds
  ...

  echo Build\ all\ projects
  Build all projects

  ** BUILD SUCCEEDED **

By default the Debug variant of ``foo`` will be built, you can run it by:

.. code-block:: none

  [cgold-example]> ./_builds/Debug/foo
  Hello from CGold!

Done!
