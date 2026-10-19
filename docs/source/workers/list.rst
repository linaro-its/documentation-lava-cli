``lava-cli workers list``
=========================

List the LAVA workers accessible to the current subscription. This
includes both shared LAVA workers and workers backed by a Linaro
Automation Appliance (LAA) — LAVA itself makes no distinction between the
two (every device has a worker, whichever kind runs it), so this one
command covers both.

Usage
-----

.. code-block:: text

   lava-cli workers list [flags]

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

   lava-cli workers list
   lava-cli workers list --json

Output
------

A table of ``HOSTNAME``, ``APPLIANCE``, ``STATE`` and ``HEALTH``. If no
workers are available, a message says so.

``HOSTNAME`` is the LAVA worker hostname (e.g. ``laa-00046``). ``APPLIANCE``
is the LMS display name of the Linaro Automation Appliance behind that
worker (e.g. ``laa-46-remi-starterkv260``) — a separate identifier assigned
in a different system, not derived from the hostname — and is blank for
shared workers that have no dedicated appliance.
