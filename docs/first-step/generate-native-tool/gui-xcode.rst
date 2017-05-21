.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

GUI: Xcode
----------

Open CMake GUI:

.. image:: xcode-screens/01-open.png
  :align: center

Click ``Browse Source...`` and find directory with ``CMakeLists.txt`` and ``foo.cpp``:

.. image:: xcode-screens/02-click-browse-source.png
  :align: center

Now we need to choose directory where to put all temporary files. Let's create
separate directory so we can keep our original directory clean.
Click ``Browse Build..``:

.. image:: xcode-screens/03-browse-build.png
  :align: center

Find directory with ``CMakeLists.txt`` and click ``New Folder`` to create
``_builds`` directory:

.. image:: xcode-screens/04-new-folder.png
  :align: center

Enter ``_builds`` and click ``Create``:

.. image:: xcode-screens/05-create-new-folder.png
  :align: center

Check the resulted layout:

.. image:: xcode-screens/06-check-layout.png
  :align: center

Click on ``Configure`` to process ``CMakeLists.txt``:

.. image:: xcode-screens/07-configure.png
  :align: center

:ref:`CMake <CMake>` will ask for the generator you want to use, pick Xcode:

.. image:: xcode-screens/08-generator.png
  :align: center

After you click ``Done`` CMake will run internal tests on build tool to
check that everything works correctly. You can see ``Configuring done``
message when finished:

.. image:: xcode-screens/09-configure-done.png
  :align: center

For now there was no native build tool files generated, on this step user
is able to do additional tuning of the project. We don't want such tuning now so
will run ``Generate``:

.. image:: xcode-screens/10-generate-done.png
  :align: center

Now if you take a look at ``_builds`` folder you can find generated
Xcode project file:

.. image:: xcode-screens/11-project-created.png
  :align: center

Open ``foo.xcodeproj`` and :doc:`run executable </first-step/run-executable/ide-xcode>`.
