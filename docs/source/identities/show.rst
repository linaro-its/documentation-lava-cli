``lava identities show``
========================

Show the details of a single saved configuration profile.

Usage
-----

.. code-block:: text

   lava identities show <name> [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The name of the profile to display. Required.

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

   lava identities show default
   lava identities show staging-team --json

Output
------

A ``FIELD`` / ``VALUE`` table showing the profile name, ``subscription_id``
and, when known, ``subscription_name``. If the named profile does not exist,
the command reports an error.
