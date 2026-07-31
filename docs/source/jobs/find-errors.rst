``lava-cli jobs find-errors``
=============================

Fetch just the error-level log entries for a job. This is a quick way to see
what went wrong without scrolling through the full log.

Usage
-----

.. code-block:: text

   lava-cli jobs find-errors <job_id> [flags]

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
     - Fetch via a specific device instead of at the subscription level.
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   lava-cli jobs find-errors 412122
   lava-cli jobs find-errors 412122 --json

Output
------

The matching error log entries, rendered in the same formatted style as
:doc:`logs`. If the job has no error entries, a message says so.
