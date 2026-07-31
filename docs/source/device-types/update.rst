``lava device-types update``
============================

Update the metadata of an existing device type. Only the fields you specify
on the command line are changed; any field you leave out is left untouched.

Usage
-----

.. code-block:: text

   lava device-types update <name> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The device type name to update. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--verbose-name``
     - Set the human-readable display name.
   * - ``--description``
     - Set the description.
   * - ``--visibility``
     - Set the visibility setting.
   * - ``--tags``
     - Set the comma-separated list of tags.
   * - ``--doc``
     - Set the documentation text.
   * - ``--img``
     - Set the image reference for the device type.
   * - ``--json``
     - Output the updated device type as JSON.
   * - ``--yaml``
     - Output the updated device type as YAML.

Examples
--------

.. code-block:: bash

   lava device-types update my-board --description "Updated description"
   lava device-types update my-board --tags arm64,ci

Output
------

On success the command confirms the update and prints the device type's
metadata. If the name is not found or you cannot access it, it reports a
"not found or access denied" error before making any change.
