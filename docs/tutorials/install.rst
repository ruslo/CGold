.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Install
=======

The next step in chain of
:menuselection:`Configure --> Generate --> Build --> Test` stages is
**install**: final step of development process which often require
privilege escalation (``make`` vs ``sudo make install``).  Installation is an
important part of the ecosystem: results of the project installation allows to
integrate it into another project using ``find_package`` and unlike
``add_subdirectory`` doesn't pollute current scope with unnecessary targets and
variables. :doc:`packing` use install procedure under the hood.

.. seealso::

  * :doc:`cmake-stages`
  * :ref:`Stages diagram <stages diagram>`

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/install-examples>`__
  * `Latest ZIP <https://github.com/cgold-examples/install-examples/archive/master.zip>`__

.. toctree::
  :maxdepth: 2

  install/library
  install/header-only
  install/with-dependencies
  install/optional-dependencies
  install/cmake-modules
  install/export-header
  install/rpath
  install/version
  install/install-prefix
  install/layout
  install/samples
  install/managing-dependencies
