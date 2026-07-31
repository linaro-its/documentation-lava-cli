``lava-cli jobs run``
=====================

Submit a single job definition, stream its logs until the job finishes, and
exit with a code that reflects the *job result*.

This is the command to use when scripting something that should only proceed
if a LAVA job passed:

.. code-block:: bash

   lava-cli jobs run my-test.yaml && ./deploy.sh

Unlike :doc:`submit`, whose exit code only reflects submission success, the
exit code here reflects the job outcome (see the table in
:doc:`index`).

Usage
-----

.. code-block:: text

   lava-cli jobs run <definition-file> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``<definition-file>``
     - Path to a single LAVA job definition (YAML). Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Submit to a specific device hostname. Omit to let LAVA schedule onto
       any device of the type named in the definition.
   * - ``--timeout``
     - Maximum time to wait for the job to finish. Default ``1h``. Use ``0``
       for no timeout.
   * - ``--polling``
     - Polling interval while following logs. Default ``5s``.
   * - ``--start``
     - Log line offset to start streaming from. Default ``0``.
   * - ``--raw``
     - Output raw YAML log entries instead of the formatted view.
   * - ``--filters``
     - Comma-separated list of log levels to show (for example
       ``target,debug``).
   * - ``--url``
     - Print the full job URL before streaming logs.

Examples
--------

.. code-block:: bash

   # Gate a deploy on the job passing
   lava-cli jobs run smoke-test.yaml && echo "safe to deploy"

   # Fail the script if the job does not finish within 30 minutes
   lava-cli jobs run long-test.yaml --timeout 30m

Exit codes
----------

See the exit code table in the :doc:`jobs overview <index>`. In short:
``0`` pass, ``1`` fail, ``2`` canceled, ``3`` timeout.
