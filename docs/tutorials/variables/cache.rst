.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Cache variables
---------------

Cache variables saved in :ref:`CMakeCache.txt` file:

.. literalinclude:: /examples/usage-of-variables/cache-cmakecachetxt/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

.. code-block:: shell
  :emphasize-lines: 2, 7

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hcache-cmakecachetxt -B_builds
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> grep -IR abc _builds/CMakeCache.txt
  abc:STRING=687

Double set
==========

If variable is already in cache then command ``set(... CACHE ...)`` will have no
effect - old variable will be used still:

.. literalinclude:: /examples/usage-of-variables/double-set/1/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

.. code-block:: shell
  :emphasize-lines: 1, 3-4, 9

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cp double-set/1/CMakeLists.txt double-set/
  [usage-of-variables]> cmake -Hdouble-set -B_builds
  Variable from cache: 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> grep -IR abc _builds/CMakeCache.txt
  abc:STRING=123

Update :ref:`CMakeLists.txt <cmakelists.txt>` (don't remove cache!):

.. literalinclude:: /examples/usage-of-variables/double-set/2/CMakeLists.txt
  :diff: /examples/usage-of-variables/double-set/1/CMakeLists.txt

.. code-block:: shell
  :emphasize-lines: 2-3, 8

  [usage-of-variables]> cp double-set/2/CMakeLists.txt double-set/
  [usage-of-variables]> cmake -Hdouble-set -B_builds
  Variable from cache: 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> grep -IR abc _builds/CMakeCache.txt
  abc:STRING=123

-D
==

Cache variable can be set by ``-D`` command line option. Unlike
``set(... CACHE ...)`` command, variable that set by ``-D`` option take
priority:

.. code-block:: shell
  :emphasize-lines: 1-2, 7

  [usage-of-variables]> cmake -Dabc=444 -Hdouble-set -B_builds
  Variable from cache: 444
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> grep -IR abc _builds/CMakeCache.txt
  abc:STRING=444

Initial cache
=============

If there are a lot of variables to set it's not so convenient to use ``-D``.
In this case user can define all variables in separate file and load
it by ``-C``:

.. literalinclude:: /examples/usage-of-variables/initial-cache/cache.cmake
  :language: cmake
  :emphasize-lines: 3-5

.. literalinclude:: /examples/usage-of-variables/initial-cache/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 6-8

.. code-block:: shell
  :emphasize-lines: 2, 4-6

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -C initial-cache/cache.cmake -Hinitial-cache -B_builds
  loading initial cache file initial-cache/cache.cmake
  A: 123
  B: 456
  C: 789
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Force
=====

If you want to set cache variable even if it's already present in cache file
you can add ``FORCE``:

.. literalinclude:: /examples/usage-of-variables/force/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4

.. code-block:: shell
  :emphasize-lines: 2-3

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -DA=456 -Hforce -B_builds
  A: 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

This is quite surprising behaviour for user and conflicts with the nature of
cache variables that designed to store variable once and globally.

.. warning::

  ``FORCE`` usually is an indicator of badly designed CMake code.

Force as a workaround
=====================

``FORCE`` can be used to fix the problem that described
:ref:`eariler <cache confusing>`:

.. literalinclude:: /examples/usage-of-variables/no-force-confuse/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

.. code-block:: shell
  :emphasize-lines: 2-3, 7-8

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hno-force-confuse -B_builds
  A: 456
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> cmake -Hno-force-confuse -B_builds
  A: 123
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

With ``FORCE`` variable will be set even it's already present in cache, so
regular variable with the same name will be unset too each time:

.. literalinclude:: /examples/usage-of-variables/force-workaround/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-5

.. code-block:: shell
  :emphasize-lines: 2-3, 7-8

  [usage-of-variables]> rm -rf _builds
  [usage-of-variables]> cmake -Hforce-workaround -B_builds
  A: 456
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds
  [usage-of-variables]> cmake -Hforce-workaround -B_builds
  A: 456
  -- Configuring done
  -- Generating done
  -- Build files have been written to: /.../usage-of-variables/_builds

Cache type
==========

Though type of any variable is **always** string you can add some hints which
will be used by CMake-GUI:

.. literalinclude:: /examples/usage-of-variables/cache-type/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4-7

Run configure:

.. image:: cache-gui/01-generate.png
  :align: center

Variable ``FOO_A`` will be treated as boolean. Uncheck box and run configure:

.. image:: cache-gui/02-bool.png
  :align: center

Variable ``FOO_B`` will be treated as path to the file. Click on ``...``:

.. image:: cache-gui/03-filepath.png
  :align: center

Select file:

.. image:: cache-gui/04-change-filepath.png
  :align: center

Run configure:

.. image:: cache-gui/05-ok-filepath.png
  :align: center

Variable ``FOO_C`` will be treated as path to directory. Click on ``...``:

.. image:: cache-gui/06-path.png
  :align: center

Select directory:

.. image:: cache-gui/07-change-path.png
  :align: center

Run configure:

.. image:: cache-gui/08-ok-path.png
  :align: center

Variable ``FOO_D`` will be treated as string. Click near variable name and
edit:

.. image:: cache-gui/09-string.png
  :align: center

Run configure:

.. image:: cache-gui/10-ok-string.png
  :align: center

Description of variable:

.. literalinclude:: /examples/usage-of-variables/cache-type/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 7

Will pop-up as a hint for users:

.. image:: cache-gui/11-popup-description.png
  :align: center

.. admonition:: CMake documentation

  * `Cache entry <https://cmake.org/cmake/help/latest/command/set.html#set-cache-entry>`__

Enumerate
=========

Selection widget can be created for variable of string type:

.. literalinclude:: /examples/usage-of-variables/cache-enum/CMakeLists.txt
  :language: cmake
  :emphasize-lines: 4, 6

.. image:: cache-gui/12-enum.png
  :align: center

.. admonition:: CMake documentation

  * `STRINGS property <https://cmake.org/cmake/help/latest/prop_cache/STRINGS.html>`__
