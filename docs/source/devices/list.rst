``lava-cli devices list``
=========================

List the LAVA devices in the current subscription.

The command resolves devices in two phases. First, the devices in your subscription
are determined. Second, for each device, the live health, state and device type
information is retrieved. The ``--fast`` flag skips the second phase and shows
device names only, which is quicker when you only need the list of names.

Usage
-----

.. code-block:: text

   lava-cli devices list [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--fast``
     - Skip the per-device detail lookup and print hostnames only.
   * - ``-a``, ``--all``
     - Include retired devices in the listing.
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   # Full listing with health and state
   lava-cli devices list

   # Just the hostnames, fast
   lava-cli devices list --fast

   # Include retired devices
   lava-cli devices list --all

Output
------

The default table shows ``HOSTNAME``, ``DEVICE TYPE``, ``WORKER``,
``APPLIANCE``, ``HEALTH`` and ``STATE``. With ``--fast`` only ``HOSTNAME``
is shown.

``WORKER`` is the LAVA worker hostname (e.g. ``laa-00046``) that runs the
device. ``APPLIANCE`` is the LMS display name of the Linaro Automation
Appliance backing that worker (e.g. ``laa-46-remi-starterkv260``) — the two
are independent identifiers assigned in different systems and are not
derived from one another. ``APPLIANCE`` is blank for devices on a shared
LAVA worker, since those are not backed by a dedicated appliance.

If some devices cannot be accessed (the Gateway returns "access denied" for
them), those devices are omitted and a count of hidden devices is printed to
stderr. If the subscription has no devices, a message says so.
