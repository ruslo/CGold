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

Example of using an ``if`` command with ``NO``/``YES`` constants and variables
with ``NO``/``YES`` values:

.. literalinclude:: /examples/control-structures/if-simple/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 8, 15, 19

.. code-block:: none
  :emphasize-lines: 2-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sif-simple -B_builds
  Condition 1
  Condition 3
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Adding ``else``/``elseif``:

.. literalinclude:: /examples/control-structures/if-else/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 9, 15, 24, 35

.. code-block:: none
  :emphasize-lines: 2-6

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sif-else -B_builds
  Condition 1
  Condition 4
  Condition 6
  Condition 10
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

CMP0054
~~~~~~~

Some of the ``if`` commands accept ``<variable|string>`` arguments. This may
lead to quite surprising behavior.

For example if we have a variable ``A`` and it is set to an empty string we can
check it with:

.. code-block:: cmake

  set(A "")
  if(A STREQUAL "")
    message("Value of A is empty string")
  endif()

You can save the name of the variable in another variable and do the same:

.. code-block:: cmake

  set(A "")
  set(B "A") # save name of the variable
  if(${B} STREQUAL "")
    message("Value of ${B} is an empty string")
  endif()

If a CMake policy ``CMP0054`` is set to ``OLD`` or not present at all
(before CMake 3.1), this operation ignores quotes:

.. code-block:: cmake

  set(A "")
  set(B "A") # save name of the variable
  if("${B}" STREQUAL "") # same as 'if(${B} STREQUAL "")'
    message("Value of ${B} is an empty string")
  endif()

It means an operation depends on the context: is a variable with the name ``${B}``
present in current scope or not?

.. literalinclude:: /examples/control-structures/cmp0054-confuse/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7, 10

.. code-block:: none
  :emphasize-lines: 2-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Scmp0054-confuse -B_builds
  A = Jane Doe
  A is empty
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Try fix
~~~~~~~

Since CMake accepts any names of the variables you can't filter out
``<variable>`` from ``<variable|string>`` by adding "reserved" symbols:

.. literalinclude:: /examples/control-structures/try-fix/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13, 17, 21

.. code-block:: none
  :emphasize-lines: 2-6

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Stry-fix -B_builds
  A = Jane Doe
  A is empty (1)
  A is empty (2)
  A is empty (3)
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Fix
~~~

To avoid such issues you should use CMake 3.1 and a ``CMP0054`` policy:

.. literalinclude:: /examples/control-structures/cmp0054-fix/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 1

.. code-block:: none
  :emphasize-lines: 2-3

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Scmp0054-fix -B_builds
  A = Jane Doe
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Workaround
~~~~~~~~~~

For CMake before 3.1 as a workaround you can use a ``string(COMPARE EQUAL ...)``
command:

.. literalinclude:: /examples/control-structures/cmp0054-workaround/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 13

.. code-block:: none
  :emphasize-lines: 2-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Scmp0054-workaround -B_builds
  A = Jane Doe
  A is not empty
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Loops
-----

foreach
~~~~~~~

.. admonition:: CMake documentation

  * `foreach <https://cmake.org/cmake/help/latest/command/foreach.html>`__

Example of a ``foreach(<variable> <list>)`` command:

.. literalinclude:: /examples/control-structures/foreach/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5, 11, 16, 22, 27, 33, 39

.. code-block:: none
  :emphasize-lines: 2, 4-6, 8-10, 11, 12, 14, 16-17, 19-24

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sforeach -B_builds
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

As you may notice ``foreach(x "${mylist}" "x;y;z")`` is not treated as a
single list but as a list with two elements: ``${mylist}`` and ``x;y;z``.
If you want to merge two lists you should do it explicitly
``set(combined_list "${mylist}" "x;y;z")`` or use
``foreach(x ${mylist} x y z)`` form.

foreach with range
~~~~~~~~~~~~~~~~~~

Example of usage of a ``foreach(... RANGE ...)`` command:

.. literalinclude:: /examples/control-structures/foreach-range/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5, 10, 15

.. code-block:: none
  :emphasize-lines: 2, 4-14, 16-21, 23-25

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sforeach-range -B_builds
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

Example of usage of a ``while`` command:

.. literalinclude:: /examples/control-structures/while/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8, 17

.. code-block:: none
  :emphasize-lines: 2, 4-8, 10-14

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Swhile -B_builds
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

.. admonition:: CMake documentation

  * `break <https://cmake.org/cmake/help/latest/command/break.html>`__

Exit from a loop with a ``break`` command:

.. literalinclude:: /examples/control-structures/break/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 11, 19

.. code-block:: none
  :emphasize-lines: 2, 4-6, 8-12

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sbreak -B_builds
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

Since CMake 3.2 it's possible to continue the loop:

.. literalinclude:: /examples/control-structures/continue/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 1, 8

.. code-block:: none
  :emphasize-lines: 2, 6, 9

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Scontinue -B_builds
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

Function without arguments:

.. literalinclude:: /examples/control-structures/simple-function/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-6

.. code-block:: none
  :emphasize-lines: 3-4

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Ssimple-function -B_builds
  Calling 'foo' function
  Calling 'foo' function
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

With arguments
~~~~~~~~~~~~~~

Function with arguments and example of ``ARGV*``, ``ARGC``, ``ARGN`` usage:

.. literalinclude:: /examples/control-structures/function-args/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 11, 19

.. code-block:: none
  :emphasize-lines: 4-6, 8-11, 13-14

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sfunction-args -B_builds
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

.. admonition:: CMake documentation

  * `CMakeParseArguments <https://cmake.org/cmake/help/latest/module/CMakeParseArguments.html>`__

``cmake_parse_arguments`` function can be used for parsing:

.. literalinclude:: /examples/control-structures/cmake-style/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 7-9, 19, 21, 44-46, 62, 65, 68, 71

.. code-block:: none
  :emphasize-lines: 4-13, 15-23, 30-33, 36

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Scmake-style -B_builds
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

CMake style limitations
~~~~~~~~~~~~~~~~~~~~~~~

Since it's not possible to create
a :ref:`list with one empty element <list with one empty element>` and because of
internal ``CMakeParseArguments`` limitations next calls will have equivalent
results:

.. literalinclude:: /examples/control-structures/cmake-style-limitations/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8, 13, 26-27, 31, 34, 37

.. code-block:: none
  :emphasize-lines: 2, 4-5, 7-8, 10-11

  [examples]> rm -rf _builds
  [examples]> cmake -Scontrol-structures/cmake-style-limitations -B_builds
  *** Run (1) ***
  X is defined: NO
  X value: ''
  *** Run (2) ***
  X is defined: NO
  X value: ''
  *** Run (3) ***
  X is defined: NO
  X value: ''
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../examples/_builds

Return value
~~~~~~~~~~~~

There is no special command to return a value from a function. You can set
a variable to the :ref:`parent scope <parent scope>` instead:

.. literalinclude:: /examples/control-structures/return-value/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 5, 14

.. code-block:: none
  :emphasize-lines: 3-4, 6

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sreturn-value -B_builds
  Before 'boo': 333
  After 'boo': 123
  Calling 'bar' with arguments: '123' 'var_out'
  Output: ABC-123-XYZ
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../control-structures/_builds

Return
~~~~~~

.. admonition:: CMake documentation

  * `return <https://cmake.org/cmake/help/latest/command/return.html>`__

You can exit from a function using a ``return`` command:

.. literalinclude:: /examples/control-structures/return/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7, 12, 15

.. code-block:: none
  :emphasize-lines: 3-5

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sreturn -B_builds
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
to the file/directory from where the function **is called**, not the file where
the function **is defined**:

.. literalinclude:: /examples/control-structures/function-location/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 8,10,12

.. literalinclude:: /examples/control-structures/function-location/boo/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 3

.. literalinclude:: /examples/control-structures/function-location/cmake/Modules/foo_run.cmake
  :language: cmake
  :emphasize-lines: 3-4, 9-11

.. code-block:: none
  :emphasize-lines: 2, 4-6, 8-10

  [control-structures]> rm -rf _builds
  [control-structures]> cmake -Sfunction-location -B_builds
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
