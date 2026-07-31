``lava-cli devices maintenance``
================================

Set a device's health to ``Maintenance`` or back to ``Good``. Putting a
device into maintenance stops LAVA from scheduling new jobs onto it.

Usage
-----

.. code-block:: text

   lava-cli devices maintenance <hostname> [--health Maintenance|Good]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The hostname of the device. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--health``
     - Target health value: ``Maintenance`` (default) or ``Good``. Any other
       value is rejected.

Examples
--------

.. code-block:: bash

   # Take a device out of service
   lava-cli devices maintenance qemu-05

   # Explicitly return it to service
   lava-cli devices maintenance qemu-05 --health Good

Output
------

On success the command confirms the device's new health value.
