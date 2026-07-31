``lava jobs results``
=====================

Fetch the test results for a job. Optionally narrow the output to a single
test suite, or a single test case within a suite.

Usage
-----

.. code-block:: text

   lava jobs results <job_id> [test_suite [test_case]] [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<job_id>``
     - The numeric ID of the job. Required.
   * - ``[test_suite]``
     - Optional. Limit output to this test suite.
   * - ``[test_case]``
     - Optional. Limit output to this test case within the suite.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Fetch results via a specific device instead of at the subscription
       level.
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   # All results for a job
   lava jobs results 412122

   # Only the "smoke-tests" suite
   lava jobs results 412122 smoke-tests

   # A single test case within a suite
   lava jobs results 412122 smoke-tests boot

Output
------

A table of ``SUITE``, ``NAME``, ``RESULT``, ``MEASUREMENT`` and ``UNIT``.
Measurement and unit are only present for tests that record a measurement. If
no results match, a message says so.

.. note:: **TODO:** Add example table output.
