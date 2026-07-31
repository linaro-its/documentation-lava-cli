``lava jobs cancel``
====================

Cancel one or more running or queued jobs. Multiple job IDs may be given; each
is cancelled independently and failures are reported per job.

Usage
-----

.. code-block:: text

   lava jobs cancel <job_id> [job_id...] [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<job_id>``
     - One or more numeric job IDs to cancel. At least one is required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Cancel via a specific device instead of at the subscription level.

Examples
--------

.. code-block:: bash

   # Cancel a single job
   lava jobs cancel 412122

   # Cancel several at once
   lava jobs cancel 412122 412123 412124

Output
------

For each job a "cancel requested" line is printed. If any job ID is invalid or
its cancellation fails, an error is printed to stderr for that job and the
command exits non-zero, reporting how many cancellations failed. Jobs that
cancelled successfully are unaffected by failures on other jobs.
