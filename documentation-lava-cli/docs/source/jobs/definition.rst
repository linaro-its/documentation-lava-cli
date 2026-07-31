``lava jobs definition``
========================

Print the job definition YAML exactly as it was submitted to LAVA. This is
useful for reproducing a job or for inspecting what was actually run.

Usage
-----

.. code-block:: text

   lava jobs definition <job_id> [flags]

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

Examples
--------

.. code-block:: bash

   # Print the definition
   lava jobs definition 412122

   # Save it to a file to resubmit later
   lava jobs definition 412122 > job.yaml

Output
------

The raw job definition YAML is printed to standard output.
