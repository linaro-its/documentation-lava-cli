``lava-cli utils logs``
=======================

Format a LAVA log YAML file for display. This applies the same formatting and
level-based colouring as :doc:`../jobs/logs`, but reads from a local file
instead of the API. It is handy for viewing logs you saved earlier with
``lava-cli jobs logs --raw``.

Usage
-----

.. code-block:: text

   lava-cli utils logs <file> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<file>``
     - Path to a LAVA log YAML file. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--raw``
     - Output the raw YAML as-is instead of the formatted view.
   * - ``--filters``
     - Comma-separated list of log levels to show (for example
       ``target,debug``).

Examples
--------

.. code-block:: bash

   # Save then view later
   lava-cli jobs logs 412122 --no-follow --raw > job.yaml
   lava-cli utils logs job.yaml

   # Only show device console output
   lava-cli utils logs job.yaml --filters target

Output
------

The formatted log lines are printed to standard output. Both the native LAVA
YAML array format and the JSON envelope produced by ``lava-cli jobs logs`` are
accepted; an unrecognised format is printed verbatim.
