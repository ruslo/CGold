.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Control structures
==================

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
  Condition 7
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

Functions
---------

Macro
-----
