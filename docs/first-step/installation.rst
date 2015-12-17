Installation
------------

.. epigraph::

  | That's it, ground.
  | I wonder if it will be friends with me?
  | Hello, ground!
  | -- `Whale <https://www.youtube.com/watch?v=GOyalYaBlpU>`_

Obviously to use some tool you need to install it first. CMake can be installed
using default system package manager or by getting binaries from
`Download page <https://cmake.org/download/>`_.

Ubuntu
======

CMake can be installed by ``apt-get``:

.. code-block:: bash

  > sudo apt-get -y install cmake
  > which cmake
  /usr/bin/cmake
  > cmake --version
  cmake version 2.8.12.2

Installing CMake GUI is similar:

.. code-block:: bash

  > sudo apt-get -y install cmake-qt-gui
  > which cmake-gui
  /usr/bin/cmake-gui
  > cmake-gui --version
  cmake version 2.8.12.2

Binaries can be downloaded and unpacked manually to any location:

.. code-block:: bash

  > wget https://cmake.org/files/v3.4/cmake-3.4.1-Linux-x86_64.tar.gz
  > tar xf cmake-3.4.1-Linux-x86_64.tar.gz
  > export PATH="`pwd`/cmake-3.4.1-Linux-x86_64/bin:$PATH" # save it in .bashrc if needed
  > which cmake
  /.../cmake-3.4.1-Linux-x86_64/bin/cmake
  > which cmake-gui
  /.../cmake-3.4.1-Linux-x86_64/bin/cmake-gui

Version:

.. code-block:: bash

  > cmake --version
  cmake version 3.4.1

  CMake suite maintained and supported by Kitware (kitware.com/cmake).
  > cmake-gui --version
  cmake version 3.4.1

  CMake suite maintained and supported by Kitware (kitware.com/cmake)

OS X
====

CMake can be installed on Mac using `brew <http://brew.sh>`_:

.. code-block:: bash

  > brew install cmake
  > which cmake
  /usr/local/bin/cmake
  > cmake --version
  cmake version 3.4.1

  CMake suite maintained and supported by Kitware (kitware.com/cmake)

Binaries can be downloaded and unpacked manually to any location:

.. code-block:: bash

  > wget https://cmake.org/files/v3.4/cmake-3.4.1-Darwin-x86_64.tar.gz
  > tar xf cmake-3.4.1-Darwin-x86_64.tar.gz
  > export PATH="`pwd`/cmake-3.4.1-Darwin-x86_64/CMake.app/Contents/bin:$PATH"
  > which cmake
  /.../cmake-3.4.1-Darwin-x86_64/CMake.app/Contents/bin/cmake
  > which cmake-gui
  /.../cmake-3.4.1-Darwin-x86_64/CMake.app/Contents/bin/cmake-gui

Version:

.. code-block:: bash

  > cmake --version
  cmake version 3.4.1

  CMake suite maintained and supported by Kitware (kitware.com/cmake).
  > cmake-gui --version
  cmake version 3.4.1

  CMake suite maintained and supported by Kitware (kitware.com/cmake).

Windows
=======

Download ``cmake-*.exe`` installer from
`Download page <https://cmake.org/download/>`_ and run it.

Click ``Next``:

.. image:: /first-step/windows-screens/installer-01.png
  :align: center

Click ``I agree``:

.. image:: /first-step/windows-screens/installer-02.png
  :align: center

Check one of the ``Add CMake to the system PATH ...`` if you want to have
CMake in ``PATH``. Check ``Create CMake Desktop Icon`` to create icon on
desktop:

.. image:: /first-step/windows-screens/installer-03.png
  :align: center

Choose installation path. Add suffix with version in case you want to have
several versions installed simultaneously:

.. image:: /first-step/windows-screens/installer-04.png
  :align: center

Shortcut in Start Menu folder:

.. image:: /first-step/windows-screens/installer-05.png
  :align: center

Installing...

.. image:: /first-step/windows-screens/installer-06.png
  :align: center

Click Finish:

.. image:: /first-step/windows-screens/installer-07.png
  :align: center

Desktop icon created:

.. image:: /first-step/windows-screens/desktop-icon.png
  :align: center

If you set ``Add CMake to the system PATH ...`` checkbox then CMake can be
accessed via
`terminal <http://smallbusiness.chron.com/open-terminal-session-windows-7-56627.html>`_
(otherwise you need to add ``...\bin`` to
`PATH environment variable <http://www.computerhope.com/issues/ch000549.htm>`_):

.. code-block:: batch

  > where cmake
  C:\soft\develop\cmake\3.4.1\bin\cmake.exe

  > where cmake-gui
  C:\soft\develop\cmake\3.4.1\bin\cmake-gui.exe

  > cmake --version
  cmake version 3.4.1

  CMake suite maintained and supported by Kitware (kitware.com/cmake).

.. seealso::

  - `Installing CMake <https://cmake.org/install/>`_
  - `How to install cmake 3.2 on ubuntu 14.04? <http://askubuntu.com/questions/610291/how-to-install-cmake-3-2-on-ubuntu-14-04>`_
