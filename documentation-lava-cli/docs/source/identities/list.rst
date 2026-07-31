``lava identities list``
========================

List the configuration profiles stored on this machine.

With the ``--discover`` flag, the command instead authenticates, decodes your
Biscuit token and queries SPIRE to show every subscription for which you hold
LAVA rights. This is the easiest way to find a subscription ID to pass to
:doc:`add`.

Usage
-----

.. code-block:: text

   lava identities list [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--discover``
     - List the subscriptions with LAVA rights available to your account,
       rather than the locally saved profiles. Requires credentials via
       ``--email``/``--pat`` or ``LAVA_CLI_USER``/``LAVA_CLI_PAT``.
   * - ``--json``
     - Output as JSON.
   * - ``--yaml``
     - Output as YAML.

Examples
--------

.. code-block:: bash

   # List locally saved profiles
   lava identities list

   # Discover subscriptions your account can use with LAVA
   lava identities list --discover

   # Machine-readable output
   lava identities list --json

Output
------

Without ``--discover``, a table of profile ``NAME`` and ``SUBSCRIPTION`` is
printed. With ``--discover``, a table of ``SUBSCRIPTION ID``, ``NAME`` and
``PLAN`` is printed.

If no profiles are configured, the command suggests running
``lava identities add``.

.. note:: **TODO:** Add example table output for both the default listing and
   the ``--discover`` listing.
