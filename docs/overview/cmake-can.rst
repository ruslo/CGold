.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

What CMake can do
-----------------

:ref:`CMake <CMake>` is a meta build system. It can generate real
:ref:`native build tool <Native build tool>` files from abstracted text configuration.
Usually such code lives in ``CMakeLists.txt`` files.

What does it mean and how it can be useful?

.. note::

  If you already decide to use :ref:`CMake <CMake>` and want to give it a try
  you can go straight to the :ref:`"First step" <first step>`.

Cross-platform development
==========================

Let's assume you have some cross-platform project with C++ code shared along
different platforms/IDEs. Say you use ``Visual Studio`` on Windows, ``Xcode``
on OSX and ``Makefile`` for Linux:

.. image:: /overview/images/native-build.png
  :align: center

What you will do if you want to add new target/source files? You have to add
them to every tool you use:

.. image:: /overview/images/native-build-add.png
  :align: center

To keep the environment consistent you have to do the similar update several
times. And the most important thing is that you have to do it **manually**. Of
course such approach is error prone and not flexible.

.. _cmake generate native build tool:

CMake solve this design flaw by adding extra step in development process. You
can describe your project in ``CMakeLists.txt`` file and use :ref:`CMake <CMake>` to
generate tools you currently interested in using cross-platform :ref:`CMake <CMake>` code:

.. image:: /overview/images/generate-native-files.png
  :align: center

Same action - adding new target/file, will be done in **one step** now:

.. image:: /overview/images/generate-native-files-add.png
  :align: center

.. _keep using your favorite tools:

Note that the right part of the diagram **was not changed**. I.e. you still can
keep using your favorite tools like ``Visual Studio/msbuild``, ``Xcode/xcodebuild`` and ``Makefile/make``!

VCS friendly
============

When you work in team on your code you probably want to share and save the
history of changes, that's what usually :ref:`VCS <VCS>` used for. How does
storing of IDE files like ``*.sln`` works on practice? Here is the diff after
adding ``bar`` executable with ``bar.cpp`` source file to the ``Visual Studio``:

.. literalinclude:: /overview/snippets/foo-new.sln
  :diff: /overview/snippets/foo-old.sln

And new ``bar.vcxproj`` of 150 lines of code. Here are some parts of it:

.. literalinclude:: /overview/snippets/bar.vcxproj
  :language: xml
  :lines: 2-11

.. literalinclude:: /overview/snippets/bar.vcxproj
  :language: xml
  :lines: 27,41-61

.. literalinclude:: /overview/snippets/bar.vcxproj
  :language: xml
  :lines: 127-142

.. literalinclude:: /overview/snippets/bar.vcxproj
  :language: xml
  :lines: 144-149

When using ``Xcode``:

.. literalinclude:: /overview/snippets/project-new.pbxproj
  :diff: /overview/snippets/project-old.pbxproj

As you can see there are a lot of magic happens while doing quite simple
task like adding new target with one source file. Looking at the diffs above
try to answer next questions:

* Are you sure that all XML sections added on purpose and was not the result
  of accidental clicking?
* Are you sure all this x86/x64/Win32, Debug/Release configurations connected
  together in right order and you haven't break something while debugging?
* Are you sure all that magic numbers was not read from your environment while
  you have done non-trivial scripting and is in fact some private key,
  token or password?
* Can you imaging resolving conflicts in such file?

Luckily we have :ref:`CMake <CMake>` which helps us in a neat way. We haven't
touched any :ref:`CMake <CMake>` syntax yet but I'm pretty sure it's quite
obvious what's happening here :)

.. literalinclude:: /overview/snippets/CMakeLists-new.txt
  :diff: /overview/snippets/CMakeLists-old.txt

What a relief! Having such human-readable form of build system commands
actually make sense to use :ref:`CMake <CMake>` even if development targeted
only for one platform.

Experimenting
=============

Even if your team has no plans to work with some :ref:`native tools <Native build tool>`
originally this may be changed in future. E.g. you have worked with ``Makefile`` and
want to try ``Ninja``. What you will do? Convert manually? Find the converter?
Write converter from scratch? Write new ``Ninja`` configuration from scratch?
With :ref:`CMake <CMake>` you can change ``cmake -G 'Unix Makefiles'`` to
``cmake -G Ninja`` - done!

This helps developers of new IDEs also. Instead of putting your IDE users into
situations when they have to decide should they use your ``SuperDuperIDE``
instead of their favorite one and probably writing endless number of
``SuperDuperIDE`` <-> ``Xcode``, ``SuperDuperIDE`` <-> ``Visual Studio``, etc.
convertes, all you have to do is to add new generator ``-G SuperDuperIDE`` to
:ref:`CMake <CMake>`.

Summary
=======

* Human-readable configuration
* Single configuration for all tools
* Cross-platform/cross-tools friendly development
* Doesn't force you to change your favorite build tool/IDE
* :ref:`VCS <VCS>` friendly development
* Easy experimenting
* Easy development of new IDEs

.. note::

  This section is not intended to cover all funtionality but only give
  brief review. Testing, packing, installing, distributing, dependency
  discovering, scripting etc. will be described fully in :ref:`Tutorials <tutorials>`.
