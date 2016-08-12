.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

What can't be done with CMake
-----------------------------

.. epigraph::

  | *Good judgement comes from experience.*
  | *Experience comes from bad judgement.*
  | *-- Mulla Nasrudin* (`? <https://en.wikiquote.org/wiki/Jim_Horning>`_)

.. Can't find good reference. Let me know if you've found a better link.

Like any kind of software (well, like anything in human life) :ref:`CMake <CMake>`
is not something perfect and has it's strengths and weaknesses. Before we
start I want to mention that **nothing in this list** is a showstopper for me.
Though I think some limitations should be fixed, some I'll be happy to see
improved. Most of the drawbacks can be kind of workarounded by using approaches
that may differs from your normal workflow but reach the end goal. Try to look
at them from another angle, think of the picture in a whole and remember
that advantages definitely outweigh the disadvantages :)

Language/syntax
===============

That is probably the first thing you will hit with, you need to accept syntax
and live with it. :ref:`CMake <CMake>` language is not something you can
compare with what you have probably used before. There are no classes, no
maps, no virtual functions or lambdas. Even parsing functions input arguments
and returning results is something quite tricky for the beginners.
:ref:`CMake <CMake>` is definitely not a language you want to try to experiment
with implementation of red-black tree or processing JSON response from server.
**But it does** handle regular development very efficiently and it is much better
then native XML files, autotools configs or `JSON-like syntax of GYP`_. Think
about it in this way: if you want to do some nasty non-standard things probably
you should stop. If you think it is something important and useful, then it
might be quite useful for other :ref:`CMake <CMake>` users too. In this case
you need to think about implementing new feature **in CMake itself**.
:ref:`CMake <CMake>` is open-source project written in C++, I hope this
language has enough power for you :) Also you can discuss this problem in
`CMake mailing-list <https://cmake.org/mailman/listinfo/cmake-developers>`_
to see how you can help with improving current state.

.. admonition:: CMake mailing list

  * `Wrapping CMake functionality with another language <http://www.mail-archive.com/cmake-developers%40cmake.org/msg15199.html>`_

.. _JSON-like syntax of GYP: https://gyp.gsrc.io/docs/LanguageSpecification.md#Example

.. _affecting workflow:

Affecting workflow
==================

This might sounds contradictory to the statement that you can
:ref:`keep using your favorite tools <keep using your favorite tools>` but it's
not. Yes, you still can work with your favorite IDE but you must remember that
:ref:`CMake <CMake>` now in charge. Imagine you have C++ header ``version.h``
generated automatically by some script from template ``version.h.in``. You see
``version.h`` file in your IDE, you can update it and run build and new variables
from ``version.h`` will be used in binary, but you **should never** do it since
you know that source is ``version.h.in`` in fact. Quite the same happens when
you use :ref:`CMake <CMake>` - you should never update build configuration in
IDE as you usually do, you have to remember that IDE files generated
from ``CMakeLists.txt`` and all your updates will be lost next time you run
:ref:`CMake <CMake>`.

Wrong workflow:

.. image:: /overview/images/bad-workflow.png
  :align: center

Correct workflow:

.. image:: /overview/images/good-workflow.png
  :align: center

That said, it's not enough to know that if you want to add new library to your
``Visual Studio`` solution you can do:

* :menuselection:`Add --> New Project ... --> Visual C++ --> Static Library`

You have to know that this must be done by adding new
``add_library`` command to ``CMakeLists.txt``.

Incomplete functionality coverage
=================================

There are some missing features in :ref:`CMake <CMake>`. That is, mapping of
CMake functionality <-> :ref:`native build tool <Native build tool>` functionality
is not always bijective. Often this can be workarounded by generating different
native tool files from the same CMake code. For example it's possible using
autotools create two versions of library (shared + static) by one run. However
this may affect performance or even not possible for other
platforms (e.g. on Windows). With :ref:`CMake <CMake>` you can generate two
versions of project from one ``CMakeLists.txt`` file: one for shared and one
for static variant, effectively running generate/build twice. This will be
covered later :doc:`in depth </tutorials/libraries/static-shared>`.

With ``Visual Studio`` you can have two variants x86 and x64 in one solution
file. With :ref:`CMake <CMake>` you have to generate project twice:
once with ``Visual Studio`` generator and one more time with ``Visual Studio Win64``
generator.

Same with ``Xcode``. In general :ref:`CMake <CMake>` can't mix two different
toolchains (at least for now) so it's not possible to generate ``Xcode``
project with ``iOS`` and ``OSX`` targets - again, just generate code for each
platform independently.

.. admonition:: Stackoverflow

  * `CMake Multiarchitecture Compilation <http://stackoverflow.com/q/5334095/2288008>`__

.. note::

  * :doc:`Building universal iOS libraries </platforms/ios/universal>`

.. _unrelocatable projects:

Unrelocatable projects
======================

Internally :ref:`CMake <CMake>` save full paths to the sources so it's not
possible to generate project and then share it between several developers.
It means you can't be CMake-guy who will generate different projects for
Xcode-guys and VisualStudio-guys. All developers in team at least should be
aware of how to generate projects using CMake. On practice it means they have
to know CMake arguments to use, literally it's
``cmake -H. -B_builds -GXcode``/``cmake -H. -B_builds "-GVisual Studio 12 2013"``,
plus remember workflow notes from the section above.
Next logic can be applied here: if you're working with developer then developer
should learn tools you've used, if you're working with users then it's your
responsibility to create user-friendly installers like ``*.msi`` instead of
projects (will be covered later in this document).

.. admonition:: CMake documentation

  * `CMAKE_USE_RELATIVE_PATHS removed since CMake 3.4 <https://cmake.org/cmake/help/latest/release/3.4.html#deprecated-and-removed-features>`__

Even if relative paths feature will be implemented (re-implemented) developers
should still have :ref:`CMake <CMake>` installed since it was used in fact:

* When you do change ``CMakeLists.txt`` :ref:`CMake <CMake>` detects it
  automatically and run regenerating
* Obviously in case if you have some custom build steps with ``cmake -E`` (command line mode) or
  ``cmake -P`` (scripting mode)
* For doing internal stuff like searching for installed dependent packages

.. admonition:: TODO

  Link to relocatable packages
