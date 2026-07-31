``lava-cli ci examples``
========================

Print ready-to-use CI pipeline snippets for the supported callback strategies.
The snippets are generated to match your installed binary — they use the
correct binary name, release version and download URL — so they can be copied
straight into a pipeline.

Usage
-----

.. code-block:: text

   lava-cli ci examples [flags]

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``--gitlab``
     - Print only the GitLab CI example.
   * - ``--github-dispatch``
     - Print only the GitHub Actions ``repository_dispatch`` example.
   * - ``--github-environment``
     - Print only the GitHub Actions environment-gate example.

With no flags, all three examples are printed.

Examples
--------

.. code-block:: bash

   # Print every example
   lava-cli ci examples

   # Just the GitLab example
   lava-cli ci examples --gitlab

   # Save the GitHub dispatch example to a file
   lava-cli ci examples --github-dispatch > lava-workflow.yml

What each example does
----------------------

GitLab CI
~~~~~~~~~

The GitLab example defines two jobs. ``lava-submit`` installs the CLI, submits
the job and registers a callback that targets a manual job named
``lava-complete``. When the LAVA job finishes, the Gateway plays
``lava-complete`` and injects a ``LAVA_JOB_STATUS`` variable (``success`` or
``failure``) that the job checks.

GitHub Actions — dispatch
~~~~~~~~~~~~~~~~~~~~~~~~~~

The dispatch example provides two workflows. The submitter workflow submits
the LAVA job; when it finishes the Gateway fires a ``repository_dispatch``
event of type ``lava-job-complete``. A separate receiver workflow listens for
that event and reads the result from
``github.event.client_payload.lava_job_status`` (and ``lava_job_id``).

GitHub Actions — environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The environment example keeps everything in one workflow run. The submit job
starts the LAVA job, then a ``gate`` job pauses on a protected environment
(``lava-gate``) until the Gateway approves or rejects the pending deployment
based on the LAVA result. Downstream jobs (for example ``deploy``) depend on
the gate.

.. seealso:: The :doc:`ci overview <index>` explains the token requirements
   for each strategy. The callback flags themselves are documented on
   :doc:`../jobs/submit`.
