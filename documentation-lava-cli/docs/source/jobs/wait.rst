``lava jobs wait``
==================

Poll a job until it reaches a terminal state (Complete, Canceled or error),
without streaming its logs. State transitions are reported to stderr as they
happen.

Usage
-----

.. code-block:: text

   lava jobs wait <job_id> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<job_id>``
     - The numeric ID of the job to wait for. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Track the job via a specific device instead of at the subscription
       level.
   * - ``--timeout``
     - Maximum time to wait. Default ``1h``.
   * - ``--interval``
     - Polling interval. Default ``30s``.

Examples
--------

.. code-block:: bash

   lava jobs wait 412122
   lava jobs wait 412122 --timeout 2h --interval 15s

Output and exit codes
---------------------

When the job finishes, a summary line reports its final state and health. The
exit code reflects the job result (``0`` pass, ``1`` fail, ``2`` canceled,
``3`` timeout); see the :doc:`jobs overview <index>` for details. On timeout
the command prints a timeout message to stderr and exits ``3``.
