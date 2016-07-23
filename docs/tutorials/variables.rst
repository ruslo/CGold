.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Variables
---------

.. epigraph::

  | *There are only two kinds of languages: the ones people complain about and*
  | *the ones nobody uses.*
  | -- `Bjarne Stroustrup <https://en.wikiquote.org/wiki/Bjarne_Stroustrup>`__

We have touched already some simple syntax like dereferencing variable ``A`` by
``${A}`` in ``message`` command: ``message("This is A: ${A}")``. Cache variables
was mentioned in :doc:`CMake stages </tutorials/cmake-stages>`. Here is an
overview of different types of variables with examples.

.. admonition:: CMake documentation

  * `Language: variables <https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables>`__

.. admonition:: Examples on GitHub

  * `Repository <https://github.com/cgold-examples/usage-of-variables>`__
  * `Latest ZIP <https://github.com/cgold-examples/usage-of-variables/archive/master.zip>`__

.. toctree::
  :maxdepth: 2

  variables/regular
  variables/cache
  variables/environment
