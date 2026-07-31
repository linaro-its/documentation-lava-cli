.. _configuration:

Configuration profiles
=======================

The LAVA CLI stores named *configuration profiles* (also called *identities*)
so that you do not have to type a subscription ID on every command. Each
profile maps a name to a subscription.

Where the config lives
----------------------

Profiles are stored in a YAML file at:

.. code-block:: text

   ~/.config/lava-cli/config.yaml

The file is created automatically the first time you save a profile. Writes
are atomic (a temporary file is written and then renamed) so the config is not
corrupted if a write is interrupted.

A profile file looks like this:

.. code-block:: yaml

   default:
     subscription_id: sub:464ef0f9-e987-4f48-a065-cb6719915747
     subscription_name: Example Team
   staging-team:
     subscription_id: sub:0f9e987e-4f48-a065-cb6719915747aabb
     subscription_name: Staging Team

Each top-level key (``default``, ``staging-team``) is the **profile name** you
choose and pass to ``--identity``. The ``subscription_name`` underneath is the
human-readable name of the subscription as returned by SPIRE, which typically
contains spaces; it is stored for display only and is never used to select a
profile.

.. note:: The profile name is used both as the ``--identity`` value and as the
   key in the config file. It must start with a letter or digit and may then
   contain only letters, digits, hyphens (``-``), underscores (``_``) and dots
   (``.``); spaces and other characters are rejected. This keeps names usable
   unquoted on the command line. Examples of valid names are ``default``,
   ``staging-team`` and ``ci``.

Selecting a profile
-------------------

Use the global ``-i`` / ``--identity`` flag to choose which profile a command
uses. When omitted, the profile named ``default`` is used.

.. code-block:: bash

   # Uses the "default" profile
   lava-cli devices list

   # Uses the "staging-team" profile
   lava-cli --identity staging-team devices list

The subscription stored in a profile can always be overridden for a single
command with ``--subscription`` or the ``LAVA_CLI_SUBSCRIPTION`` environment
variable. See :ref:`authentication` for the full precedence order.

Managing profiles
-----------------

Profiles are created, listed, inspected and removed with the
:doc:`../identities/index` commands:

* :doc:`../identities/add` — add or update a profile.
* :doc:`../identities/list` — list saved profiles, or discover available
  subscriptions with ``--discover``.
* :doc:`../identities/show` — show a single profile.
* :doc:`../identities/delete` — remove a profile.
