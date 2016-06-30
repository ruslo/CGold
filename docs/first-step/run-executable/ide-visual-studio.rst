.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

IDE: Visual Studio
------------------

Since we used ``* Win64`` generator target's architecture is ``x64``:

.. image:: visual-studio-screens/01-x64.png
  :align: center

We need to tell Visual Studio that target we want to run is ``foo``. This can
be done by right clicking on ``foo`` target in ``Solution Explorer`` and
choosing ``Set as StartUp Project``:

.. image:: visual-studio-screens/02-startup-project.png
  :align: center

To run executable go to :menuselection:`Debug --> Start Without Debugging`:

.. image:: visual-studio-screens/03-start.png
  :align: center

Visual Studio will build target first then execute it:

.. image:: visual-studio-screens/04-hello.png
  :align: center

Done!
