jobs commands
=============

The ``jobs`` commands are the heart of the CLI: they submit LAVA test jobs,
stream their logs, wait for them to finish, and retrieve their results,
definitions and configuration.

Job targeting
-------------

Most job commands accept an optional ``-d`` / ``--device`` flag. When given,
the command operates against a specific device's copy of the job; when
omitted, it operates against the job at the subscription level. For
submission, omitting ``--device`` lets LAVA schedule the job onto any
available device of the type named in the job definition.

Following logs and exit codes
-----------------------------

Several commands can *follow* a job, streaming its logs until the job reaches
a terminal state. Two commands differ in what their exit code means:

* :doc:`submit` exits ``0`` when the *submission* succeeds, regardless of
  whether the job itself passes or fails.
* :doc:`run` exits with a code that reflects the *job result*, which makes it
  suitable for gating a script on job outcome.

Commands that report a job result use these exit codes:

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Code
     - Meaning
   * - ``0``
     - Job finished with health Complete or Unknown (pass).
   * - ``1``
     - Job finished with health Incomplete (fail).
   * - ``2``
     - Job was Canceled.
   * - ``3``
     - Timeout elapsed before the job finished.

.. toctree::
   :maxdepth: 1

   list
   show
   submit
   run
   validate
   wait
   logs
   results
   find-errors
   definition
   config
   resubmit
   cancel
   queue
