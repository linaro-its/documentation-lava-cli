``lava-cli jobs show``
======================

Show the details of a single job.

Usage
-----

.. code-block:: text

   lava-cli jobs show <job_id> [flags]

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
     - Look the job up via a specific device instead of at the subscription
       level.
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   lava-cli jobs show 412122
   lava-cli jobs show 412122 --json

Output
------

A key/value listing of ``id``, ``description``, ``state``, ``health``,
``device-type``, ``device``, ``submitted``, ``started`` and ``finished``.
