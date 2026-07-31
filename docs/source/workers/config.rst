``lava-cli workers config``
===========================

Manage a worker's configuration.

.. warning:: These commands are **not implemented yet**. They are present so
   that the command surface matches the legacy ``lavacli`` tool, but invoking
   them returns a "not implemented" error and makes no network calls.

Subcommands
-----------

``lava-cli workers config get <hostname>``
   Intended to retrieve a worker's configuration.

``lava-cli workers config set <hostname> <file>``
   Intended to set a worker's configuration from a file.

.. note:: **TODO:** Document the behaviour, flags and output once these
   commands are implemented.
