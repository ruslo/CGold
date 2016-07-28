.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

General Hints
-------------

Verify
======

Verify device is visible by service:

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
