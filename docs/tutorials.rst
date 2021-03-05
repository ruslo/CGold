.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _tutorials:

Tutorials
=========

If you reached this section it means you can handle
:doc:`basic configuration </first-step>`. It's time to see everything in detail
and add more features.

.. note::

  In provided examples:

  * CMake will be run in command-line format but CMake-GUI will work in similar
    way, if behavior differs it will be noted explicitly
  * For the host platform ``Linux`` is chosen, use analogous commands
    if you use another host. E.g. use ``dir _builds`` on Windows instead of
    ``ls _builds``
  * ``Unix Makefiles`` will be used as a generator. On \*nix platforms this is
    default one. Peculiarities of other generators will be described explicitly

.. toctree::
  :maxdepth: 2

  /tutorials/cmake-stages
  /tutorials/out-of-source
  /tutorials/workflow
  /tutorials/version-policies
  /tutorials/project
  /tutorials/variables
  /tutorials/cmake-sources
  /tutorials/control-structures
  /tutorials/executables
  /tutorials/tests
  /tutorials/libraries
  /tutorials/pseudo-targets
  /tutorials/collecting-sources
  /tutorials/usage-requirements
  /tutorials/build-types
  /tutorials/configure-file
  /tutorials/install
  /tutorials/toolchain
  /tutorials/generator-expressions
  /tutorials/properties
  /tutorials/packing
  /tutorials/continuous-integration
