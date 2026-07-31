``lava-cli jobs queue``
=======================

List the queued and scheduled jobs for the current subscription, optionally
filtered to a single device type.

Usage
-----

.. code-block:: text

   lava-cli jobs queue [device-type] [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``[device-type]``
     - Optional. A device type slug to filter by. Equivalent to the
       ``--device-type`` flag (accepted positionally for ``lavacli``
       compatibility).

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--device-type``
     - Filter by device type slug.
   * - ``-c``, ``--count``
     - Number of jobs to return. Default ``25``.
   * - ``--offset``
     - Skip the first N jobs (paging). Default ``0``.
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   # All queued jobs in the subscription
   lava-cli jobs queue

   # Queued jobs for a single device type
   lava-cli jobs queue qemu

   # Same, using the flag form
   lava-cli jobs queue --device-type qemu --count 50

Output
------

A table of ``JOB ID``, ``DEVICE``, ``STATE`` and ``DESCRIPTION``. If nothing
is queued for the selected device type, a message says so.
