``lava-cli devices add``
========================

Add a new device to the current subscription.

Usage
-----

.. code-block:: text

   lava-cli devices add --hostname <name> --device-type <slug> --worker <host> [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--hostname``
     - Hostname for the new device. **Required.**
   * - ``--device-type``
     - Device type slug the device belongs to. **Required.**
   * - ``--worker``
     - Hostname of the shared worker that will manage the device.
       **Required.**
   * - ``--description``
     - Free-text description of the device.
   * - ``--health``
     - Initial health state. One of ``GOOD``, ``UNKNOWN``, ``LOOPING``,
       ``BAD``, ``MAINTENANCE`` or ``RETIRED``.

Examples
--------

.. code-block:: bash

   lava-cli devices add \
     --hostname qemu-05 \
     --device-type qemu \
     --worker worker-01 \
     --description "QEMU test instance" \
     --health GOOD

Output
------

On success the command confirms that the device was created.

Notes
-----

The legacy ``lavacli`` ``--user`` and ``--group`` flags are **not supported**.
Device ownership is managed through subscriptions in this system, so passing
either flag results in a clear error rather than being silently ignored.
