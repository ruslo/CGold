.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  cmake

Scripts
=======

.. admonition:: CMake documentation

  * `CMake options <https://cmake.org/cmake/help/latest/manual/cmake.1.html#options>`__

Example
~~~~~~~

.. literalinclude:: /examples/cmake-sources/script/create-file.cmake
  :language: cmake
  :emphasize-lines: 3

.. code-block:: shell
  :emphasize-lines: 2, 4, 6

  [cmake-sources]> rm -f Hello.txt
  [cmake-sources]> cmake -P script/create-file.cmake
  [cmake-sources]> ls Hello.txt
  Hello.txt
  [cmake-sources]> cat Hello.txt
  Created by script

Minimum required (bad)
~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /examples/cmake-sources/minimum-required-bad/script.cmake
  :language: cmake
  :emphasize-lines: 6, 9

.. code-block:: shell
  :emphasize-lines: 1, 2, 14

  [cmake-sources]> cmake -P minimum-required-bad/script.cmake
  MYNAME: Jane Doe
  CMake Warning (dev) at minimum-required-bad/script.cmake:6 (if):
    Policy CMP0054 is not set: Only interpret if() arguments as variables or
    keywords when unquoted.  Run "cmake --help-policy CMP0054" for policy
    details.  Use the cmake_policy command to set the policy and suppress this
    warning.

    Quoted variables like "Jane Doe" will no longer be dereferenced when the
    policy is set to NEW.  Since the policy is not set the OLD behavior will be
    used.
  This warning is for project developers.  Use -Wno-dev to suppress it.

  MYNAME is empty!

Minimum required (good)
~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /examples/cmake-sources/minimum-required-good/script.cmake
  :language: cmake
  :emphasize-lines: 8, 11

.. code-block:: shell
  :emphasize-lines: 1, 2

  [cmake-sources]> cmake -P minimum-required-good/script.cmake
  MYNAME: Jane Doe

cmake -E
~~~~~~~~

.. admonition:: CMake documentation

  * `Command-Line Tool Mode <https://cmake.org/cmake/help/latest/manual/cmake.1.html#command-line-tool-mode>`__

.. literalinclude:: /examples/cmake-sources/without-command-line/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13, 20

.. literalinclude:: /examples/cmake-sources/command-line/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5
