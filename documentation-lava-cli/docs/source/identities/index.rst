identities commands
====================

The ``identities`` commands manage the CLI's local configuration profiles.
A profile (or *identity*) maps a name to a LAVA subscription, so you can
select a subscription with ``--identity <name>`` instead of typing a
subscription ID on every command.

Profiles are stored in ``~/.config/lava-cli/config.yaml``. See
:ref:`configuration` for details on the file format and how a profile is
selected.

These commands manage local configuration only and, with the exception of
``add`` and ``list --discover``, do not contact the API.

.. toctree::
   :maxdepth: 1

   add
   list
   show
   delete
