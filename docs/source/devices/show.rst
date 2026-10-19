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
``device-type``, ``worker``, ``appliance-name``, ``state``, ``health``,
``description``, ``pipeline``, ``has-device-dict``, ``current-job`` (the job
currently running on the device, if any) and ``tags``.

``worker`` is the LAVA worker hostname (e.g. ``laa-00046``) that runs the
device. ``appliance-name`` is the LMS display name of the Linaro Automation
Appliance backing that worker (e.g. ``laa-46-remi-starterkv260``) — the two
are independent identifiers assigned in different systems and are not
derived from one another. The ``appliance-name`` row is only shown for
devices backed by a dedicated appliance; it is omitted entirely for devices
on a shared LAVA worker.
