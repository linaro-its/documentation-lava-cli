``lava-cli jobs list``
======================

List jobs in the current subscription, or jobs for a specific device.

Usage
-----

.. code-block:: text

   lava-cli jobs list [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Filter to jobs for a single device hostname. When omitted, jobs across
       the whole subscription are listed.
   * - ``-c``, ``--count``
     - Number of jobs to return. Default ``25``.
   * - ``--start``
     - Skip the first N jobs (offset for paging). Default ``0``.
   * - ``--ordering``
     - Field to order the results by.
   * - ``--health``
     - Filter by job health.
   * - ``--state``
     - Filter by job state.
   * - ``--since``
     - Only jobs from the last N minutes.
   * - ``--verbose``
     - Show extra columns (submitter, device, start and finish times).
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   # Most recent 25 jobs in the subscription
   lava-cli jobs list

   # Jobs for one device, most recent 50
   lava-cli jobs list --device qemu-01 --count 50

   # Only running jobs
   lava-cli jobs list --state Running

   # Jobs submitted in the last hour, with extra detail
   lava-cli jobs list --since 60 --verbose

Output
------

By default a table of ``ID``, ``STATE``, ``HEALTH``, ``SUBMITTER``,
``DESCRIPTION`` and ``DEVICE TYPE``. With ``--verbose``, additional
``DEVICE``, ``STARTED`` and ``FINISHED`` columns are shown. If no jobs match,
a message says so.

.. note:: **TODO:** Add example table output and confirm the accepted values
   for ``--ordering``, ``--health`` and ``--state``.
