``lava workers maintenance``
============================

Put a LAVA shared worker into maintenance mode. While a worker is in
maintenance, LAVA does not schedule new jobs to the devices it manages.

Usage
-----

.. code-block:: text

   lava workers maintenance <hostname>

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``<hostname>``
     - The hostname of the worker. Required.

Examples
--------

.. code-block:: bash

   lava workers maintenance worker-01

Output
------

On success the command confirms that the worker was set to maintenance.

.. note:: **TODO:** Document how a worker is returned from maintenance to
   active service (whether that is via a flag on this command or a separate
   command). The current implementation only sets maintenance mode.
