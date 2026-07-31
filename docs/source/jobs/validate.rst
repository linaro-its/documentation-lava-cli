``lava-cli jobs validate``
==========================

Validate a job definition without submitting it. LAVA checks that the
definition is well-formed and schedulable and returns a message describing the
result.

Usage
-----

.. code-block:: text

   lava-cli jobs validate <definition-file> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``<definition-file>``
     - Path to the LAVA job definition (YAML) to validate. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Validate against a specific device hostname. Omit to validate against
       the device type named in the definition.

Examples
--------

.. code-block:: bash

   lava-cli jobs validate my-test.yaml
   lava-cli jobs validate my-test.yaml --device qemu-01

Output
------

The validation message returned by LAVA is printed to standard output.

.. note:: **TODO:** Add an example of the validation message for both a valid
   and an invalid definition.
