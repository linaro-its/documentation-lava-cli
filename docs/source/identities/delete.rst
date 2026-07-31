``lava identities delete``
==========================

Remove a saved configuration profile. This only affects the local config
file; it does not change anything on the server.

Usage
-----

.. code-block:: text

   lava identities delete <name>

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<name>``
     - The name of the profile to delete. Required.

Examples
--------

.. code-block:: bash

   lava identities delete staging-team

Output
------

On success the command confirms that the identity was deleted. If the named
profile does not exist, it reports an error and makes no changes.
