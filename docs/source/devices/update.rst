``lava-cli devices update``
===========================

Update the properties of an existing device. At least one field flag must be
given; only the fields you specify are changed.

Usage
-----

.. code-block:: text

   lava-cli devices update <hostname> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The hostname of the device to update. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--device-type``
     - Move the device to a different device type slug.
   * - ``--description``
     - Set a new description.
   * - ``--worker``
     - Reassign the device to a different worker hostname.

Examples
--------

.. code-block:: bash

   lava-cli devices update qemu-05 --description "Retired soon"
   lava-cli devices update qemu-05 --worker worker-02

Output
------

On success the command confirms that the device was updated. If no field
flags are supplied, it errors asking for at least one of ``--device-type``,
``--description`` or ``--worker``.

Notes
-----

The legacy ``lavacli`` visibility and ownership flags (``--public``,
``--private``, ``--user`` and ``--group``) are **not supported**. Device
visibility and ownership are managed through subscriptions, so passing any of
these flags results in a clear error.
