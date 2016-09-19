.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. spelling::

  foreach

Control structures
==================

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/control-structures>`__
  * `Latest ZIP <https://github.com/cgold-examples/control-structures/archive/master.zip>`__

Conditional blocks
------------------

Simple examples
~~~~~~~~~~~~~~~

.. literalinclude:: /examples/control-structures/if-simple/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 8, 15, 19

.. code-block:: shell
  :emphasize-lines: 2-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hif-simple -B_builds
  Condition 1
  Condition 3
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

.. literalinclude:: /examples/control-structures/if-else/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 9, 15, 24, 35

.. code-block:: shell
  :emphasize-lines: 2-6

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hif-else -B_builds
  Condition 1
  Condition 4
  Condition 6
  Condition 10
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

CMP0054
~~~~~~~

.. literalinclude:: /examples/control-structures/cmp0054-confuse/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7, 10

.. code-block:: shell
  :emphasize-lines: 2-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hcmp0054-confuse -B_builds
  A = Jane Doe
  A is empty
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Try fix
~~~~~~~

.. literalinclude:: /examples/control-structures/try-fix/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13, 17, 21

.. code-block:: shell
  :emphasize-lines: 2-6

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Htry-fix -B_builds
  A = Jane Doe
  A is empty (1)
  A is empty (2)
  A is empty (3)
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Fix
~~~

.. literalinclude:: /examples/control-structures/cmp0054-fix/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 1

.. code-block:: shell
  :emphasize-lines: 2-3

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hcmp0054-fix -B_builds
  A = Jane Doe
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Workaround
~~~~~~~~~~

.. literalinclude:: /examples/control-structures/cmp0054-workaround/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13

.. code-block:: shell
  :emphasize-lines: 2-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hcmp0054-workaround -B_builds
  A = Jane Doe
  A is not empty
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

.. admonition:: Stackoverflow

  * `CMake compare to empty string with STREQUAL failed <http://stackoverflow.com/questions/19982340>`__

Loops
-----

foreach
~~~~~~~

.. literalinclude:: /examples/control-structures/foreach/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5, 11, 16, 22, 27, 33, 39

.. code-block:: shell
  :emphasize-lines: 2, 4-6, 8-10, 11, 12, 14, 16-17, 19-24

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hforeach -B_builds
  Explicit list:
    A
    B
    C
  Dereferenced list:
    foo
    boo
    bar
  Empty list
  Dereferenced empty list
  List with empty element:
    ''
  Separate lists:
    a;b;c
    x;y;z
  Combined list:
    a
    b
    c
    x
    y
    z
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

foreach with range
~~~~~~~~~~~~~~~~~~

.. literalinclude:: /examples/control-structures/foreach-range/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5, 10, 15

.. code-block:: shell
  :emphasize-lines: 2, 4-14, 16-21, 23-25

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hforeach-range -B_builds
  Simple range:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
  Range with limits:
    3
    4
    5
    6
    7
    8
  Range with step:
    10
    12
    14
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

while
~~~~~

.. literalinclude:: /examples/control-structures/while/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8, 17

.. code-block:: shell
  :emphasize-lines: 2, 4-8, 10-14

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hwhile -B_builds
  Loop with condition as variable:
    a = x
    a = xx
    a = xxx
    a = xxxx
    a = xxxxx
  Loop with explicit condition:
    a = x
    a = xx
    a = xxx
    a = xxxx
    a = xxxxx
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

break
~~~~~

.. literalinclude:: /examples/control-structures/break/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 11, 19

.. code-block:: shell
  :emphasize-lines: 2, 4-6, 8-12

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hbreak -B_builds
  Stop 'while' loop:
    x
    xx
    xxx
  Stop 'foreach' loop:
    0
    1
    2
    3
    4
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

continue
~~~~~~~~

.. literalinclude:: /examples/control-structures/continue/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 1, 8

.. code-block:: shell
  :emphasize-lines: 2, 6, 9

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hcontinue -B_builds
  Loop with 'continue':
    process 0
    process 1
    skip 2
    process 3
    process 4
    skip 5
    process 6
    process 7
    process 8
    process 9
    process 10
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

.. admonition:: CMake documentation

  * `CMake 3.2 release notes <https://cmake.org/cmake/help/v3.2/release/3.2.html#commands>`__

.. _cmake functions:

Functions
---------

.. admonition:: CMake documentation

  * `function <https://cmake.org/cmake/help/latest/command/function.html>`__

Simple
~~~~~~

.. literalinclude:: /examples/control-structures/simple-function/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-6

.. code-block:: shell
  :emphasize-lines: 3-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hsimple-function -B_builds
  Calling 'foo' function
  Calling 'foo' function
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

With arguments
~~~~~~~~~~~~~~

.. literalinclude:: /examples/control-structures/function-args/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 11, 19

.. code-block:: shell
  :emphasize-lines: 4-6, 8-11, 13-14

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hfunction-args -B_builds
  Calling function 'foo':
    x = 1
    y = 2
    z = 3
  Calling function 'boo':
    x = 4
    y = 5
    z = 6
    total = 3
  Calling function 'bar':
    All = 7;8;9;10;11
    Unexpected = 10;11
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

CMake style
~~~~~~~~~~~

.. literalinclude:: /examples/control-structures/cmake-style/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 7-9, 19, 21, 44-46, 62, 65, 68, 71

.. code-block:: shell
  :emphasize-lines: 4-13, 15-23, 30-33, 36

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hcmake-style -B_builds
  *** Run (1) ***
  FOO: TRUE
  BOO: FALSE
  X: value
  Y:
  Z:
  L1:
    item1
    item2
    item3
  L2:
  *** Run (2) ***
  FOO: TRUE
  BOO: TRUE
  X:
  Y: abc
  Z: 123
  L1:
  L2:
    item1
    item3
  *** Run (3) ***
  FOO: FALSE
  BOO: FALSE
  X:
  Y:
  Z:
  L1:
    item1
    item2
    item3
  L2:
  *** Run (4) ***
  { param1, param2 } = { 123, 888 }
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

.. admonition:: CMake documentation

  * `cmake_parse_arguments <https://cmake.org/cmake/help/latest/command/cmake_parse_arguments.html>`__

Return value
~~~~~~~~~~~~

.. literalinclude:: /examples/control-structures/return-value/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5, 14

.. code-block:: shell
  :emphasize-lines: 3-4, 6

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hreturn-value -B_builds
  Before 'boo': 333
  After 'boo': 123
  Calling 'bar' with arguments: '123' 'var_out'
  Output: ABC-123-XYZ
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Return
~~~~~~

.. literalinclude:: /examples/control-structures/return/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7, 12, 15

.. code-block:: shell
  :emphasize-lines: 3-5

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hreturn -B_builds
  Exit on A
  Exit on B
  Exit
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

.. _function list dir:

CMAKE_CURRENT_LIST_DIR
~~~~~~~~~~~~~~~~~~~~~~

Value of ``CMAKE_CURRENT_LIST_FILE`` and ``CMAKE_CURRENT_LIST_DIR`` is set
to the file/directory from where function **is called**, not the file where
function **is defined**:

.. literalinclude:: /examples/control-structures/function-location/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8,10,12

.. literalinclude:: /examples/control-structures/function-location/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. literalinclude:: /examples/control-structures/function-location/cmake/Modules/foo_run.cmake
  :language: cmake
  :emphasize-lines: 3-4, 9-11

.. code-block:: shell
  :emphasize-lines: 2, 4-6, 8-10

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Hfunction-location -B_builds
  foo_run(123)
  Called from: /.../control-structures/function-location
  Defined in file: /.../control-structures/function-location/cmake/Modules/foo_run.cmake
  Defined in directory: /.../control-structures/function-location/cmake/Modules
  foo_run(abc)
  Called from: /.../control-structures/function-location/boo
  Defined in file: /.../control-structures/function-location/cmake/Modules/foo_run.cmake
  Defined in directory: /.../control-structures/function-location/cmake/Modules
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

.. admonition:: CMake documentation

  * `CMAKE_CURRENT_LIST_DIR <https://cmake.org/cmake/help/latest/variable/CMAKE_CURRENT_LIST_DIR.html>`__
  * `CMAKE_CURRENT_LIST_FILE <https://cmake.org/cmake/help/latest/variable/CMAKE_CURRENT_LIST_FILE.html>`__

.. _function name recommendation:

Recommendation
~~~~~~~~~~~~~~

To avoid function name clashing with functions from another modules do prefix
name with the project name. In case if function name
will match name of the module you can verify that module used in your code
just by simple in-file search (and of course delete it if not):

.. code-block:: cmake

  include(foo_my_module_1)
  include(foo_my_module_2)

  foo_my_module_1(INPUT1 "abc" INPUT2 123 RESULT result)
  foo_my_module_2(INPUT1 "${result}" INPUT2 "xyz")

.. seealso::

  * :ref:`Module names <module name recommendation>`
  * :ref:`Cache names <cache name recommendation>`
