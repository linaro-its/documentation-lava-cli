``lava identities add``
=======================

Add a new configuration profile, or update an existing one, that ties a
profile name to a LAVA subscription.

The command has two modes:

**Interactive mode** (no ``--subscription`` flag)
   The CLI authenticates, discovers every subscription your account has LAVA
   permissions for, and presents them in a picker. Subscriptions already
   saved in another profile are shown but cannot be selected again.

**Non-interactive mode** (``--subscription`` provided)
   The CLI validates that the given subscription ID has LAVA permissions and
   then saves it without prompting. This is suitable for scripting.

Both modes require credentials via ``--email``/``--pat`` or the
``LAVA_CLI_USER``/``LAVA_CLI_PAT`` environment variables.

Usage
-----

.. code-block:: text

   lava identities add [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-n``, ``--name``
     - Profile name to create or update. Defaults to ``default``. In
       interactive mode you are prompted for this if it is not given.
   * - ``--subscription``
     - Subscription ID in the form ``sub:<uuid>``. Providing this switches the
       command into non-interactive mode.

Examples
--------

.. code-block:: bash

   # Interactive: pick a subscription from a list and save it as "default"
   lava identities add

   # Interactive: save the chosen subscription under a specific profile name
   lava identities add --name staging-team

   # Non-interactive: validate and save a known subscription ID
   lava identities add --name ci --subscription sub:464ef0f9-e987-4f48-a065-cb6719915747

Notes
-----

* A subscription ID must start with ``sub:``. In non-interactive mode, the
  command errors if the prefix is missing.
* If the target subscription is already stored in another profile, the
  command refuses to save a duplicate and reports which profile holds it.
* If a subscription has no LAVA permissions, it cannot be saved.

.. note:: **TODO:** Add a captured transcript of the interactive picker
   (subscription list and prompts) and the confirmation message printed on a
   successful save.
