``lava-cli jobs resubmit``
==========================

Resubmit an existing job. LAVA creates a new job from the original job's
definition and returns the new job ID. By default the new job's logs are
followed until it finishes.

Usage
-----

.. code-block:: text

   lava-cli jobs resubmit <job_id> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<job_id>``
     - The numeric ID of the job to resubmit. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Resubmit via a specific device instead of at the subscription level.
   * - ``--no-follow``
     - Print the new job ID and exit without streaming logs.
   * - ``--url``
     - Print the full job URL instead of the bare ID.
   * - ``--polling``
     - Polling interval while following logs. Default ``5s``.
   * - ``--start``
     - Log line offset to start streaming from. Default ``0``.
   * - ``--raw``
     - Output raw YAML log entries instead of the formatted view.
   * - ``--filters``
     - Comma-separated list of log levels to show (for example
       ``target,debug``).

Examples
--------

.. code-block:: bash

   # Resubmit and follow the new job
   lava-cli jobs resubmit 412122

   # Resubmit and return immediately with the new job ID
   lava-cli jobs resubmit 412122 --no-follow

Output
------

The new job ID (or URL with ``--url``) is printed. When following, the new
job's logs then stream to stdout.
