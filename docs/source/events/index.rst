events commands
===============

The ``events`` commands wait for a device or worker to reach a target state
and/or health. They poll the relevant detail endpoint until the target
condition is met or a timeout elapses, printing each state transition as it
is observed.

This is useful in scripts that need to block until, for example, a device
returns to a ``Good`` health after maintenance.

.. toctree::
   :maxdepth: 1

   wait
