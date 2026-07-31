``lava jobs config``
====================

Retrieve the device configuration that was used while a job ran. By default
each configuration document is written to a file in the destination
directory, using the same filenames as the legacy ``lavacli`` tool.

The documents written (when present) are:

* ``definition.yaml`` — the job definition
* ``device.yaml`` — the rendered device dictionary
* ``dispatcher.yaml`` — the dispatcher configuration
* ``env.yaml`` — the dispatcher environment
* ``env.dut.yaml`` — the device-under-test environment

A document that the server returns as null is skipped and no file is written
for it.

Usage
-----

.. code-block:: text

   lava jobs config <job_id> [flags]

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
   * - ``--dest``
     - Output directory for the configuration files. Default ``.`` (the
       current directory). Created if it does not exist.
   * - ``--json``
     - Print all documents as a single JSON object to stdout instead of
       writing files.
   * - ``--yaml``
     - Print all documents as a single YAML document to stdout instead of
       writing files.

Examples
--------

.. code-block:: bash

   # Write config files into ./job-412122/
   lava jobs config 412122 --dest job-412122

   # Print everything as JSON instead of writing files
   lava jobs config 412122 --json

Output
------

When writing files, each file written is reported on its own line. If no
documents are available, a message says so. With ``--json`` or ``--yaml`` the
documents are emitted to stdout and no files are written.
