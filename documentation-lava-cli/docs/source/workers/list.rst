``lava workers list``
=====================

List the LAVA shared workers accessible to the current subscription.

Usage
-----

.. code-block:: text

   lava workers list [flags]

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

   lava workers list
   lava workers list --json

Output
------

A table of ``HOSTNAME``, ``STATE`` and ``HEALTH``. If no workers are
available, a message says so.

.. note:: **TODO:** Add example table output.
