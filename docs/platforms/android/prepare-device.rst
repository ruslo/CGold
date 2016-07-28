.. Copyright (c) 2016, Ruslan Baratov
.. All rights reserved.

Prepare device
--------------

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
