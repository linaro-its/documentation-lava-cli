``lava-cli workers show``
=========================

Show the full details of a single LAVA worker, identified by its worker
hostname. This works for both a shared LAVA worker and a worker backed by
a Linaro Automation Appliance (LAA) — pass the hostname shown as
``worker``/``WORKER`` by ``lava-cli devices show`` or ``lava-cli devices
list``.

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

A key/value listing of ``hostname``, ``appliance-name``, ``state``,
``health``, ``description``, ``last-ping`` (when the worker last contacted
the server) and ``version``.

``hostname`` is the LAVA worker hostname (e.g. ``laa-00046``).
``appliance-name`` is the LMS display name of the Linaro Automation
Appliance behind that worker (e.g. ``laa-46-remi-starterkv260``) — a
separate identifier assigned in a different system, not derived from the
hostname. The ``appliance-name`` row is only shown for LAA-backed workers;
it is omitted entirely for shared workers.
