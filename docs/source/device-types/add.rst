``lava device-types add``
=========================

Create a new device type. This requires elevated permissions: your token must
hold either ``lms:admin`` or ``lms:create:devicetype``. If neither is present,
the command stops with a permission-denied error before making any change.

Usage
-----

.. code-block:: text

   lava device-types add --name <name> [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--name``
     - Name of the new device type. **Required.**
   * - ``--verbose-name``
     - Human-readable display name.
   * - ``--description``
     - Free-text description of the device type.
   * - ``--visibility``
     - Visibility setting for the device type.
   * - ``--tags``
     - Comma-separated list of tags to associate with the device type.
   * - ``--doc``
     - Documentation text for the device type.
   * - ``--json``
     - Output the created device type as JSON.
   * - ``--yaml``
     - Output the created device type as YAML.

Examples
--------

.. code-block:: bash

   lava device-types add \
     --name my-board \
     --verbose-name "My Board rev B" \
     --description "Internal test board" \
     --tags arm64,internal

Output
------

On success the command confirms the device type was created and prints its
metadata (``name``, ``verbose-name``, ``uuid``, ``visibility``,
``description``, ``tags`` and ``perms``).

.. note:: **TODO:** Document the accepted ``--visibility`` values.
