.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

.. _odr:

One Definition Rule (ODR)
-------------------------

ODR is a rule for C++ programs that forbids declarations of the entities
with same name but by different C++ code. Better/exact description is out of
the scope of this document, please visit the links below for details if needed.

As a brief overview you can't do things like:

.. code-block:: cpp
  :emphasize-lines: 4

  // Boo.hpp

  class Foo {
    int a;
  };

.. code-block:: cpp
  :emphasize-lines: 4

  // Bar.hpp

  class Foo {
    double a; // ODR violation, defined differently!
  };

Though this code looks trivial and violation is obvious, there are scenarios
when it's no so easy to detect such kind of errors, e.g. see examples from
:doc:`Library Symbols </tutorials/libraries/symbols>` section.

.. seealso::

  * `One Definition Rule <http://en.cppreference.com/w/cpp/language/definition>`__

.. admonition:: Stackoverflow

  * `Library headers and #define <http://stackoverflow.com/q/20833226/2288008>`__
