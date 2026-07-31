``lava tags show``
==================

Show a single tag configured on a device.

Usage
-----

.. code-block:: text

   lava tags show <tag> --device <hostname> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<tag>``
     - The name of the tag to show. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Hostname of the device the tag belongs to. **Required.**
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   lava tags show arm64 --device qemu-01

Output
------

A table with the tag ``NAME`` and ``DESCRIPTION``. If the tag is not present
on the device, the command reports that the tag was not found and exits with a
non-zero status.
