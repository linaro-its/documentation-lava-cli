``lava device-types health-check``
==================================

Manage the *health-check* definition for a device type. A health-check is a
LAVA job definition that is run periodically against devices of the type to
confirm they are working. Like templates, health-checks are versioned:
setting a new one creates a new configuration revision.

This command has two subcommands: ``get`` and ``set``.

``lava device-types health-check get``
--------------------------------------

Print the latest health-check definition for a device type to standard
output.

.. code-block:: text

   lava device-types health-check get <name>

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The device type name. Required.

Example:

.. code-block:: bash

   lava device-types health-check get qemu > qemu-health.yaml

If the device type has no configuration revisions, the command reports an
error.

``lava device-types health-check set``
--------------------------------------

Create a new health-check revision for a device type from a file. Use ``-`` as
the file to read from standard input. The sibling device dictionary template
on the latest revision is preserved on the new revision.

.. code-block:: text

   lava device-types health-check set <name> <file> [flags]

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The device type name. Required.
   * - ``<file>``
     - Path to the new health-check file, or ``-`` to read from stdin.
       Required.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-m``, ``--message``
     - Optional message describing the new configuration revision.

Example:

.. code-block:: bash

   lava device-types health-check set qemu qemu-health.yaml -m "New boot test"

On success the command reports the revision number of the new configuration.
