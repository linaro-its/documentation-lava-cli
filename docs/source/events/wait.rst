``lava events wait``
====================

Poll a device or worker until it reaches a target state and/or health, or a
timeout elapses. This command has two subcommands: ``device`` and ``worker``.

The waiting options are shared by both subcommands and are given between
``wait`` and the subcommand, or after the hostname.

Shared flags
------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--state``
     - Target state to wait for. An empty value (the default) matches any
       state.
   * - ``--health``
     - Target health to wait for. An empty value (the default) matches any
       health.
   * - ``--timeout``
     - Maximum time to wait. Default ``5m``.
   * - ``--interval``
     - Polling interval. Default ``5s``.

If both ``--state`` and ``--health`` are left empty, the very first
observation satisfies the condition.

``lava events wait device``
---------------------------

Wait for a device to reach the target state/health.

.. code-block:: text

   lava events wait device <hostname> [flags]

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The device hostname to poll. Required.

Example:

.. code-block:: bash

   # Wait up to 10 minutes for a device to come back to Good health
   lava events wait device qemu-01 --health Good --timeout 10m

``lava events wait worker``
---------------------------

Wait for a worker to reach the target state/health.

.. code-block:: text

   lava events wait worker <hostname> [flags]

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The worker hostname to poll. Required.

Example:

.. code-block:: bash

   lava events wait worker worker-01 --state Online

Output and exit codes
---------------------

Each observed ``state=… health=…`` transition is printed. When the target
condition is met, a summary line is printed and the command exits ``0``. If
the timeout elapses first, the last-observed state is printed to stderr and
the command exits ``1``.

.. note:: **TODO:** Confirm and document the full set of valid ``--state`` and
   ``--health`` values for devices and workers.
