.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

General Hints
-------------

Prepare device
==============

You have to prepare your device for debugging. For Android 4.2+
tap ``Build number`` seven times:

* :menuselection:`Settings --> About phone --> Build number`

``Developer options`` appears now:

* :menuselection:`Settings --> Developer options`

.. seealso::

  * `Enabling On-device Developer Options <https://developer.android.com/studio/run/device.html#developer-device-options>`__

.. note::

  * On practice instructions may differ for different devices. E.g. it may be
    ``Android version`` or ``MIUI version`` instead of ``Build number``
    (http://en.miui.com/thread-24025-1-1.html)

Go to ``Developer options`` and turn it ``ON``:

* :menuselection:`Settings --> Developer options --> Developer options`

Also turn ``ON`` debug mode when USB is connected. Otherwise ``adb`` will not
be able to discover the device:

* :menuselection:`Settings --> Developer options --> USB debugging`

Get Android NDK
===============

.. admonition:: Polly

  * Script `install-ci-dependencies.py`_ will install Android NDK if environment
    variable ``TOOLCHAIN`` set to ``android-*`` (`.travis.yml example`_).

`Android NDK`_ contains compilers and other tools for C++ development.

.. _install-ci-dependencies.py: https://github.com/ruslo/polly/blob/d71cc9ad1c68f78b12a33ad91e171f5b82fcc65b/bin/install-ci-dependencies.py
.. _.travis.yml example: https://github.com/forexample/hunter-simple/blob/989d83359ccd73b4f3a544d02d10895c24ccce3f/.travis.yml#L123-L130
.. _Android NDK: https://developer.android.com/ndk/downloads/index.html

Get Android SDK
===============

.. admonition:: Hunter

  * Android SDK will be downloaded automatically, no need to install it.

`Android SDK`_ tools used for development on Android platform:
adb, android, emulator, etc.

.. _Android SDK: https://developer.android.com/studio/index.html#downloads

Verify
======

Connect device with USB and verify it's visible by ``adb`` service:

.. code-block:: shell
  :emphasize-lines: 3

  > adb devices
  List of devices attached
  MTPxxx device

If service is not started there will be extra messages:

.. code-block:: shell
  :emphasize-lines: 3-4

  > adb devices
  List of devices attached
  * daemon not running. starting it now on port 5037 *
  * daemon started successfully *
  MTPxxx device

SDK version on device
=====================

The needed version of SDK can be get by reading ``ro.build.version.sdk``:

.. code-block:: shell

  > adb -d shell getprop ro.build.version.sdk
  19

Means you need to use API 19.

.. note::

  * ``-d`` is for real device
  * ``-e`` is for emulator

.. admonition:: Stackoverflow

  * `Getting Android SDK version of a device from command line <http://stackoverflow.com/questions/8063461/>`__

CPU architecture
================

Run next command to determine CPU architecture of emulator:

.. code-block:: shell

  > adb -e shell getprop ro.product.cpu.abi
  x86

And this one for device:

.. code-block:: shell

  > adb -e shell getprop ro.product.cpu.abi
  armeabi-v7a

Log
===

.. seealso::

  * `logcat <https://developer.android.com/studio/command-line/logcat.html>`__

Clear log:

.. code-block:: shell

  > adb logcat -c

Filter only Info (``I``) messages from ``SimpleApp``, ignore others and exit:

.. code-block:: shell
  :emphasize-lines: 4

  > adb logcat -d SimpleApp:I *:S
  --------- beginning of /dev/log/main
  --------- beginning of /dev/log/system
  I/SimpleApp( 9015): Hello from Android! (Not debug)
  >
