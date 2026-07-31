``lava-cli tags list``
======================

List the tags configured on a device.

Usage
-----

.. code-block:: text

   lava-cli tags list --device <hostname> [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Hostname of the device whose tags to list. **Required.**
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   lava-cli tags list --device qemu-01
   lava-cli tags list -d qemu-01 --json

Output
------

A table of tag ``NAME`` and ``DESCRIPTION``. Tags without a description show
an empty description column. If the device has no tags, a message says so. If
``--device`` is omitted, the command reports an error.
