``lava-cli system whoami``
==========================

Show the identity in use and the subscriptions your account can access. This
is a quick way to confirm that your credentials and active subscription are
what you expect before running other commands.

Usage
-----

.. code-block:: text

   lava-cli system whoami [flags]

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

   lava-cli system whoami
   lava-cli --identity staging-team system whoami --json

Output
------

A key/value listing of the active ``identity`` (profile name) and
``active-subscription``, followed by a table of all subscriptions your
account can access showing ``SUBSCRIPTION ID``, ``NAME`` and ``PLAN``.

.. note:: **TODO:** Add example output.
