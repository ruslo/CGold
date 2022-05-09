.. Copyright (c) 2016-2017, Ruslan Baratov
.. All rights reserved.

.. spelling::

  diff
  diffs

What CMake can do
-----------------

:ref:`CMake <CMake>` is a meta build system. It can generate real
:ref:`native build tool <Native build tool>` files from abstracted text configuration.
Usually such code lives in ``CMakeLists.txt`` files.

What does it mean and how it can be useful?

Cross-platform development
==========================

Let's assume you have some cross-platform project with C++ code shared along
different platforms/IDEs. Say you use ``Visual Studio`` on Windows, ``Xcode``
on OSX and ``Makefile`` for Linux:

.. image:: /overview/images/native-build.png
  :align: center

What you will do if you want to add new ``bar.cpp`` source file? You have to add
it to every tool you use:

.. image:: /overview/images/native-build-add.png
  :align: center

To keep the environment consistent you have to do the similar update several
times. And the most important thing is that you have to do it **manually**
(arrow marked with a red color on the diagram in this case). Of course such
approach is error prone and not flexible.

.. _cmake generate native build tool:

CMake solve this design flaw by adding an extra step to the development process. You
can describe your project in a ``CMakeLists.txt`` file and use :ref:`CMake <CMake>` to
generate the cross-platform build tools:

.. image:: /overview/images/generate-native-files.png
  :align: center

Same action - adding new ``bar.cpp`` file, will be done in **one step** now:

.. image:: /overview/images/generate-native-files-add.png
  :align: center

.. _keep using your favorite tools:

Note that the bottom part of the diagram **was not changed**. I.e. you still can
keep using your favorite tools like ``Visual Studio/msbuild``,
``Xcode/xcodebuild`` and ``Makefile/make``!

.. seealso::

  * `KDE moving from autotools to CMake <http://lwn.net/Articles/188693/>`__
  * `Visual C++ Team Blog: Support for Android CMake projects in Visual Studio <https://blogs.msdn.microsoft.com/vcblog/2015/12/15/support-for-android-cmake-projects-in-visual-studio/>`__
  * `Android Studio: Add C and C++ code to Your Project <https://developer.android.com/studio/projects/add-native-code.html>`__


VCS friendly
============

Version Control (:ref:`VCS <VCS>`) is used to share and save your code's
history of changes when you work in a team. However, different IDEs use unique
files to track project files (``*.sln``, ``.pbxproj``, ``.vscode``, ect)
For example, here is the diff after adding ``bar.cpp`` source file to the ``bar`` 
executable in ``Visual Studio``:

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

As you can see, a lot of magic happens while doing a simple
task like adding one new source file to a target. Aditionaly,

* Are you sure that all XML sections added on purpose and was not the result
  of accidental clicking?
* Are you sure all this x86/x64/Win32, Debug/Release configurations connected
  together in right order and you haven't break something while debugging?
* Are you sure all that magic numbers was not read from your environment while
  you have done non-trivial scripting and is in fact some private key,
  token or password?
* Do you think it will be easy to resolve conflict in this file?

Luckily we have :ref:`CMake <CMake>` which helps us in a neat way. We haven't
touched any :ref:`CMake <CMake>` syntax yet but I'm pretty sure it's quite
obvious what's happening here :)

.. literalinclude:: /overview/snippets/CMakeLists-new.txt
  :diff: /overview/snippets/CMakeLists-old.txt

What a relief! Having such human-readable form of build system commands
actually making :ref:`CMake <CMake>` a convenient tool for development even
if you're using only one platform.

Experimenting
=============

Even if your team has no plans to work with some :ref:`native tools <Native build tool>`
originally, this may change in the future. E.g. you have worked with ``Makefile`` and
want to try ``Ninja``. What you will do? Convert manually? Find the converter?
Write converter from scratch? Write new ``Ninja`` configuration from scratch?
With :ref:`CMake <CMake>` you can change ``cmake -G 'Unix Makefiles'`` to
``cmake -G Ninja`` - done!

This helps developers of new IDEs also. Instead of putting your IDE users into
situations when they have to decide should they use your ``SuperDuperIDE``
instead of their favorite one and probably writing endless number of
``SuperDuperIDE`` <-> ``Xcode``, ``SuperDuperIDE`` <-> ``Visual Studio``, etc.
converters, all you have to do is to add new generator ``-G SuperDuperIDE`` to
:ref:`CMake <CMake>`.

Family of tools
===============

.. _stages diagram:

CMake is a family of tools that can help you during all stages of
``sources for developers`` -> ``quality control`` -> ``installers for users``
stack. Next `activity diagram`_ shows CMake, CTest and CPack connections:

.. image:: images/cmake-environment.png
  :align: center

.. _activity diagram: http://yed-uml.readthedocs.io/en/latest/activity-diagram.html


.. note::

  * All stages will be described fully in :ref:`Tutorials <tutorials>`.

.. seealso::

  * :doc:`CMake Workflow </tutorials/workflow>`

Summary
=======

* Human-readable configuration
* Single configuration for all tools
* Cross-platform/cross-tools friendly development
* Doesn't force you to change your favorite build tool/IDE
* :ref:`VCS <VCS>` friendly development
* Easy experimenting
* Easy development of new IDEs
