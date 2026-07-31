``lava-cli device-types template``
==================================

Manage the *device dictionary template* for a device type. The template is
the jinja2/YAML definition that LAVA uses to render the device dictionary for
every device of that type. Templates are versioned: setting a new template
creates a new configuration revision rather than overwriting the old one.

This command has two subcommands: ``get`` and ``set``.

``lava-cli device-types template get``
--------------------------------------

Print the latest device dictionary template for a device type to standard
output.

.. code-block:: text

   lava-cli device-types template get <name>

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The device type name. Required.

Example:

.. code-block:: bash

   lava-cli device-types template get qemu > qemu.jinja2

If the device type has no configuration revisions, the command reports an
error.

``lava-cli device-types template set``
--------------------------------------

Create a new template revision for a device type from a file. Use ``-`` as the
file to read the new content from standard input. The sibling health-check
definition on the latest revision is preserved on the new revision.

.. code-block:: text

   lava-cli device-types template set <name> <file> [flags]

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The device type name. Required.
   * - ``<file>``
     - Path to the new template file, or ``-`` to read from stdin. Required.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-m``, ``--message``
     - Optional message describing the new configuration revision.

Example:

.. code-block:: bash

   lava-cli device-types template set qemu qemu.jinja2 -m "Bump kernel args"

   # Read from stdin
   cat qemu.jinja2 | lava-cli device-types template set qemu - -m "Piped update"

On success the command reports the revision number of the new configuration.
