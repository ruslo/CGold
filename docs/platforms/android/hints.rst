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

Verify
======

Connect device with USB and verify it's visible by ``adb`` service:

.. code-block:: shell
  :emphasize-lines: 3

  > adb devices
  List of devices attached
  MTPxxx unauthorized

If service is not started there will be extra messages:

.. code-block:: shell
  :emphasize-lines: 3-4

  > adb devices
  List of devices attached
  * daemon not running. starting it now on port 5037 *
  * daemon started successfully *
  MTPxxx unauthorized

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
