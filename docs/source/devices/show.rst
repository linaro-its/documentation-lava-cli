``lava-cli devices show``
=========================

Show the full details of a single LAVA device.

Usage
-----

.. code-block:: text

   lava-cli devices show <hostname> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The hostname of the device to display. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   lava-cli devices show qemu-01
   lava-cli devices show qemu-01 --json

Output
------

A key/value listing of the device's properties: ``hostname``,
``device-type``, ``worker``, ``state``, ``health``, ``description``,
``pipeline``, ``has-device-dict``, ``current-job`` (the job currently running
on the device, if any) and ``tags``.

.. note:: **TODO:** Add an example of the key/value output for a device.
