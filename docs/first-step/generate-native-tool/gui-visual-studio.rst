.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

GUI: Visual Studio
------------------

Open CMake GUI:

.. image:: visual-studio-screens/01-open-cmake-gui.png
  :align: center

Click ``Browse Source...`` and find directory with ``CMakeLists.txt`` and ``foo.cpp``:

.. image:: visual-studio-screens/02-click-browse-source.png
  :align: center

Now we need to choose directory where to put all temporary files. Let's create
separate directory so we can keep our original directory clean.
Click ``Browse Build..``:

.. image:: visual-studio-screens/03-click-browse-build.png
  :align: center

Find directory with ``CMakeLists.txt`` and click ``Make New Folder`` to create
``_builds`` directory:

.. image:: visual-studio-screens/04-create-new-folder.png
  :align: center

Check the resulted layout:

.. image:: visual-studio-screens/05-layout.png
  :align: center

Click on ``Configure`` to process ``CMakeLists.txt``:

.. image:: visual-studio-screens/06-configure.png
  :align: center

:ref:`CMake <CMake>` will ask for the generator you want to use.
Pick Visual Studio you have installed and add ``Win64`` to have x64 target:

.. image:: visual-studio-screens/07-generator.png
  :align: center

After you click ``Finish`` CMake will run internal tests on build tool to
check that everything works correctly. You can see ``Configuring done``
message when finished:

.. image:: visual-studio-screens/08-configuring-done.png
  :align: center

For now there was no native build tool files generated, on this step user
is able to do additional tuning of project. We don't want such tuning now so
will run ``Generate``:

.. image:: visual-studio-screens/09-generate.png
  :align: center

Now if you take a look at ``_builds`` folder you can find generated
Visual Studio solution file:

.. image:: visual-studio-screens/10-open-solution.png
  :align: center

Open ``foo.sln`` and :doc:`run executable </first-step/run-executable/ide-visual-studio>`.
