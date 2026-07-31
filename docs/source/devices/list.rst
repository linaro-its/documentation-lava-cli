``lava devices list``
=====================

List the LAVA devices in the current subscription.

The command resolves devices in two phases. First it queries SPIRE for the
device-under-test resources in your subscription to obtain hostnames. Then it
enriches each hostname with live health, state and device-type information
from the Gateway. The ``--fast`` flag skips the second phase and shows
hostnames only, which is quicker when you only need the list of names.

Usage
-----

.. code-block:: text

   lava devices list [flags]

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
   lava devices list

   # Just the hostnames, fast
   lava devices list --fast

   # Include retired devices
   lava devices list --all

Output
------

The default table shows ``HOSTNAME``, ``DEVICE TYPE``, ``WORKER``,
``HEALTH`` and ``STATE``. With ``--fast`` only ``HOSTNAME`` is shown.

If some devices cannot be accessed (the Gateway returns "access denied" for
them), those devices are omitted and a count of hidden devices is printed to
stderr. If the subscription has no devices, a message says so.

.. note:: **TODO:** Add example table output for the default and ``--fast``
   listings.
