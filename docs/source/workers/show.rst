``lava-cli workers show``
=========================

Show the full details of a single LAVA shared worker.

Usage
-----

.. code-block:: text

   lava-cli workers show <hostname> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The hostname of the worker to display. Required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   lava-cli workers show worker-01
   lava-cli workers show worker-01 --yaml

Output
------

A key/value listing of ``hostname``, ``state``, ``health``, ``description``,
``last-ping`` (when the worker last contacted the server) and ``version``.

.. note:: **TODO:** Add an example of the key/value output for a worker.
