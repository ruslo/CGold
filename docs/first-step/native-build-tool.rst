Native build tool
=================

As already mentioned CMake *can't* do the build itself - it *generates files*
which can be used by real native build tool, hence you need to choose such
tool(s) and install it if needed. Option `-G \<generator-name>`_ can be used to
specify what type of generator will be run. If no such option present CMake
will use default generator (e.g. ``Unix Makefiles`` on \*nix platforms).

List of available `generators`_ depends on the host OS (e.g. ``Visual Studio``
family generators not available on ``Linux``). You can get this list by running
``cmake --help``:

.. code-block:: bash

  > cmake --help
  ...
  Generators

  The following generators are available on this platform:
    Unix Makefiles              = Generates standard UNIX makefiles.
    Ninja                       = Generates build.ninja files (experimental).
    Watcom WMake                = Generates Watcom WMake makefiles.
    CodeBlocks - Ninja          = Generates CodeBlocks project files.
    ...

.. toctree::
  :maxdepth: 1

  native-build-tool/unix-makefiles.rst
  native-build-tool/ninja.rst

.. seealso::

  * `CMake Generators <https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html>`_

.. _generators: https://cmake.org/cmake/help/v3.5/manual/cmake-generators.7.html
.. _-G \<generator-name>: https://cmake.org/cmake/help/v3.5/manual/cmake.1.html#options