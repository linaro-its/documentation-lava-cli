``lava-cli device-types list``
==============================

List the LAVA device types available to the current subscription, along with
how many devices of each type exist.

Usage
-----

.. code-block:: text

   lava-cli device-types list [flags]

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

   lava-cli device-types list
   lava-cli device-types list --json

Output
------

A table of ``DEVICE TYPE`` and the number of ``DEVICES`` of that type. If no
device types are available, a message says so.

.. note:: **TODO:** Add example table output.
