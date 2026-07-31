``lava workers env``
====================

Manage a worker's environment.

.. warning:: These commands are **not implemented yet**. They are present so
   that the command surface matches the legacy ``lavacli`` tool, but invoking
   them returns a "not implemented" error and makes no network calls.

Subcommands
-----------

``lava workers env get <hostname>``
   Intended to retrieve a worker's environment.

``lava workers env set <hostname> <file>``
   Intended to set a worker's environment from a file.

.. note:: **TODO:** Document the behaviour, flags and output once these
   commands are implemented.
