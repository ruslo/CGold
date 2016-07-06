.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _source tree:

Source tree
-----------

Hierarchy of directories with source files such as CMake/C++ sources.
:ref:`CMake <CMake>` starts with the :ref:`CMakeLists.txt <CMakeLists.txt>`
from top of the source tree. This directory can be set by :ref:`-H <-H>`
in command line or by ``Browse Source...`` in CMake-GUI.

This directory is mean to be shareable. E.g. probably you should not store
hardcoded paths specific to your local environment in this code. This is
directory that you want to be managed with :ref:`VCS <VCS>`.

.. seealso::

  * :ref:`-H <-H>`
  * :ref:`Build tree <build tree>`
  * :doc:`GUI + Visual Studio </first-step/generate-native-tool/gui-visual-studio>`
  * :doc:`GUI + Xcode </first-step/generate-native-tool/gui-xcode>`
