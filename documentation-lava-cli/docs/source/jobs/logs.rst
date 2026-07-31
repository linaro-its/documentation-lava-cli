``lava jobs logs``
==================

Fetch the logs for a job. By default the command *follows* the job: it polls
its status and streams new log lines until the job reaches a terminal state.
Use ``--no-follow`` to fetch a single snapshot and exit.

Log entries are rendered with a timestamp, level and message, and (on a
terminal) colour-coded by level. Set ``NO_COLOR`` in the environment to
disable colour.

Usage
-----

.. code-block:: text

   lava jobs logs <job_id> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<job_id>``
     - The numeric ID of the job. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Fetch logs via a specific device instead of at the subscription level.
   * - ``--no-follow``
     - Fetch a single snapshot of the logs and exit without polling.
   * - ``--start``
     - Start line offset. Default ``0``.
   * - ``--end``
     - End line (only applies with ``--no-follow``). Defaults to
       ``start + 2000``.
   * - ``--raw``
     - Output the raw YAML log list instead of the formatted view.
   * - ``--filters``
     - Comma-separated list of log levels to show (for example
       ``target,debug``).
   * - ``--polling``
     - Polling interval when following. Default ``5s``.

Log levels
----------

The following log levels appear in LAVA logs and can be used with
``--filters``: ``debug``, ``info``, ``warning``, ``error``, ``input``,
``target`` (device serial console output), ``feedback`` (secondary device
output), ``results``, ``exception`` and ``event``.

Examples
--------

.. code-block:: bash

   # Follow a running job's logs
   lava jobs logs 412122

   # Grab a snapshot of the first 500 lines
   lava jobs logs 412122 --no-follow --start 0 --end 500

   # Only show device console and error output
   lava jobs logs 412122 --filters target,error

   # Raw YAML, for saving to a file
   lava jobs logs 412122 --no-follow --raw > job.yaml

Output
------

Formatted log lines are printed to stdout. When following, pre-running state
transitions (for example queued or scheduling) are printed to stderr.

.. note:: **TODO:** Add an example of the formatted log output.
