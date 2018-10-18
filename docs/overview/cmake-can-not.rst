.. Copyright (c) 2016-2017, Ruslan Baratov
.. All rights reserved.

What can't be done with CMake
-----------------------------

.. epigraph::

  | *Good judgement comes from experience.*
  | *Experience comes from bad judgement.*
  | *-- Mulla Nasrudin* (`? <https://en.wikiquote.org/wiki/Jim_Horning>`_)

.. Can't find good reference. Let me know if can find a better link (Ruslo)

:ref:`CMake <CMake>` has it's strengths and weaknesses. Most of the drawbacks
mentioned here can be worked around by using approaches that may differ from
your normal workflow, yet still reach the end goal. Try to look at them from another
angle; think of the picture as a whole and remember that the advantages definitely
outweigh the disadvantages.

Language/syntax
===============

This is probably the first thing you will be hit with. The :ref:`CMake <CMake>`
language is not something you can compare with what you have likely used
before. There are no classes, no maps, no virtual functions or lambdas. Even
parsing the input arguments of each function then returning results is something quite
tricky for the beginners.  :ref:`CMake <CMake>` is definitely not a language
you want to try to experiment with implementation of red-black tree or
processing JSON responses from a server.  **But it does** handle regular
development very efficiently and you probably will find it more attractive than
XML files, autotools configs or `JSON-like syntax`_.

Think about it in this
way: if you want to do some nasty non-standard thing then probably you should
stop.  If you think it is something important and useful, then it might be
quite useful for other :ref:`CMake <CMake>` users too. In this case you need to
think about implementing new feature **in CMake itself**.  :ref:`CMake <CMake>`
is open-source project written in C++, and additional features are always being introduced.
You can also discuss any problems in the `CMake mailing-list
<https://cmake.org/mailman/listinfo/cmake-developers>`_ to see how you can help
with improving the current state.

.. admonition:: CMake mailing list

  * `Wrapping CMake functionality with another language <http://www.mail-archive.com/cmake-developers%40cmake.org/msg15199.html>`_

.. _JSON-like syntax: https://gyp.gsrc.io/docs/LanguageSpecification.md#Example

.. _affecting workflow:

Affecting workflow
==================

This might sound contradictory to the statement that you can
:ref:`keep using your favorite tools <keep using your favorite tools>`, but it's
not. You still can work with your favorite IDE, but you must remember that
:ref:`CMake <CMake>` is now "in charge".

Imagine you have C++ header ``version.h``
generated automatically by some script from template ``version.h.in``. You see
``version.h`` file in your IDE, you can update it and run build and new variables
from ``version.h`` will be used in binary, but you **should never** do it since
you know that source is actually ``version.h.in``.

Similarly, when you use :ref:`CMake <CMake>` - you **should never**
update your build configuration directly in the IDE. Instead, you have to remember that
any target files generated from ``CMakeLists.txt`` and all your project additions made
directly in the IDE will be lost next time you run :ref:`CMake <CMake>`.

Wrong workflow:

.. image:: /overview/images/bad-workflow.png
  :align: center

Correct workflow:

.. image:: /overview/images/good-workflow.png
  :align: center

It's not enough to know that if you want to add a new library to your
``Visual Studio`` solution you can do:

* :menuselection:`Add --> New Project ... --> Visual C++ --> Static Library`

You have to know that this must instead be done by adding a new
``add_library`` command to ``CMakeLists.txt``.

Incomplete functionality coverage
=================================

There are some missing features in :ref:`CMake <CMake>`. Mapping of
CMake functionality <-> :ref:`native build tool <Native build tool>` functionality
is not always bijective. Often this can be worked around by generating different
native tool files from the same CMake code. For example it's possible using
autotools create two versions of library
(:doc:`shared + static </tutorials/libraries/static-shared>`) by one run.
However this may affect performance, or be outright impossible for other platforms
(e.g. on Windows). With :ref:`CMake <CMake>` you can generate two versions of
project from one ``CMakeLists.txt`` file: one each for shared and static
variants, effectively running generate/build twice.

With ``Visual Studio`` you can have two variants, x86 and x64, in one solution
file. With :ref:`CMake <CMake>` you have to generate project twice:
once with ``Visual Studio`` generator and one more time with ``Visual Studio Win64``
generator.

Similarly with ``Xcode``. In general :ref:`CMake <CMake>` can't mix two different
toolchains (at least for now) so it's not possible to generate an ``Xcode``
project with ``iOS`` and ``OSX`` targets—again, just generate code for each
platform independently.

.. note::

  * :doc:`Building universal iOS libraries </platforms/ios/universal>`

.. _unrelocatable projects:

Unrelocatable projects
======================

Internally, :ref:`CMake <CMake>` saves the full paths to each of the sources,
so it's not possible to generate a project then share it between several developers.
In other words, you can't be "the CMake person" who will generate seperate projects for
those who use Xcode and those who use Visual Studio. All developers in the team should be
aware of how to generate projects using CMake. In practice it means they have
to know which CMake arguments to use, some basic examples being
``cmake -H. -B_builds -GXcode`` and ``cmake -H. -B_builds "-GVisual Studio 12 2013"``
for Xcode and Visual Studio, respectively. Additionaly, they must understand the 
[changes they must make in their workflow](https://cgold.readthedocs.io/en/latest/overview/cmake-can-not.html#affecting-workflow). As a general rule, developers should make an effort to learn the tools
used in making the code they wish to utilize. Only when providing an end product to users is it
your responsibility to generate user-friendly installers like ``*.msi`` instead of
simply providing the project files.

.. admonition:: CMake documentation

  * `CMAKE_USE_RELATIVE_PATHS removed since CMake 3.4 <https://cmake.org/cmake/help/latest/release/3.4.html#deprecated-and-removed-features>`__

Even if support for relative paths will be re-implemented in the future each developer
in the team should have :ref:`CMake <CMake>` installed, as there are other tasks which
:ref:`CMake <CMake>` automatically takes care of that may be done incorrectly if done manually.
A few examples are:

* The automatic detection of changes to ``CMakeLists.txt`` and subsequent regeneration of the source tree.
* The inclusion of custom build steps with the built-in scripting mode.
* For doing internal stuff like searching for installed dependent packages

.. admonition:: TODO

  Link to relocatable packages
