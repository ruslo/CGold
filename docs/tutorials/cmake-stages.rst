.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

CMake stages
------------

We start with a theory. Let's introduce some terminology about
:ref:`CMake <CMake>` commands we have executed :doc:`before </first-step>`.

.. _configure:

Configure step
==============

On this step CMake will parse top level :ref:`CMakeLists.txt <cmakelists.txt>`
of :ref:`source tree <source tree>` and create
:ref:`CMakeCache.txt <cmakecache.txt>` file with
:ref:`cache variables <cache variables>`. Different types of variables will be
described further in details. For CMake-GUI this step triggered by clicking
on ``Configure`` button. For CMake command-line this step is combined with
generate step so terms configure and generate will be used interchangeably.
The end of this step expressed by ``Configuring done`` message from CMake.

.. terminology discussion:
.. * http://www.mail-archive.com/cmake%40cmake.org/msg55116.html

GUI + Xcode example
~~~~~~~~~~~~~~~~~~~

.. _generate:

Generate step
=============

On this step CMake will generate :ref:`native build tool <native build tool>`
files using information from CMakeLists.txt and variables from CMakeCache.txt.
For CMake-GUI this step triggered by clicking on ``Generate`` button.
For CMake command-line this step is combined with configure step.
The end of this step expressed by ``Generating done`` message from CMake.

.. _build:

Build step
==========

This step is orchestrated by native build tool. On this step targets of your
project will be build.
