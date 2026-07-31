``lava-cli device-types show``
==============================

Show the metadata for a single device type.

Usage
-----

.. code-block:: text

   lava-cli device-types show <name> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The device type name to display. Required.

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

   lava-cli device-types show qemu
   lava-cli device-types show qemu --yaml

Output
------

A key/value listing of ``name``, ``verbose-name``, ``uuid``, ``visibility``,
``description``, ``tags`` and ``perms`` (the effective permissions your token
holds on this device type).

If the name is not found or you are not allowed to see it, the command
reports a "not found or access denied" error.
