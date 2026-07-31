``lava jobs submit``
====================

Submit one or more job definitions to LAVA and, by default, stream the logs
of each job until it reaches a terminal state.

The exit code reflects whether the *submission* succeeded (``0``) or failed
(``1``); it does **not** reflect whether the job itself passed. If you need an
exit code that reflects the job result, use :doc:`run` instead.

Usage
-----

.. code-block:: text

   lava jobs submit <definition-file> [definition-file...] [flags]

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``<definition-file>``
     - Path to a LAVA job definition (YAML). One or more may be given. At
       least one is required.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Flag
     - Description
   * - ``-d``, ``--device``
     - Submit to a specific device hostname. Omit to let LAVA schedule onto
       any device of the type named in the definition.
   * - ``--no-follow``
     - Print the job ID and return immediately without streaming logs.
   * - ``--url``
     - Print the full job URL instead of the bare job ID.
   * - ``--polling``
     - Polling interval while following logs. Default ``5s``.
   * - ``--start``
     - Log line offset to start streaming from. Default ``0``.
   * - ``--raw``
     - Output raw YAML log entries instead of the formatted view.
   * - ``--filters``
     - Comma-separated list of log levels to show (for example
       ``target,debug``).
   * - ``--gitlab-wait-job``
     - Name of the manual GitLab job to trigger when the LAVA job completes
       (CI callback). See :doc:`../ci/index`.
   * - ``--gitlab-token``
     - GitLab API token (or ``LAVA_CLI_GITLAB_TOKEN``).
   * - ``--github-repo``
     - GitHub repository (``owner/repo``) to notify when the LAVA job
       completes (CI callback).
   * - ``--github-strategy``
     - GitHub callback strategy: ``dispatch`` (default) or ``environment``.
   * - ``--github-token``
     - GitHub token (or ``LAVA_CLI_GITHUB_TOKEN``).

Examples
--------

.. code-block:: bash

   # Submit and stream logs
   lava jobs submit my-test.yaml

   # Submit to a specific device without following
   lava jobs submit my-test.yaml --device qemu-01 --no-follow

   # Submit several definitions at once
   lava jobs submit test-a.yaml test-b.yaml

   # Submit and print the full job URL
   lava jobs submit my-test.yaml --no-follow --url

CI callbacks
------------

When a CI callback flag (``--gitlab-wait-job`` or ``--github-repo``) is
provided and the CLI detects it is running inside the matching CI system, the
Gateway is asked to notify that CI system when the LAVA job completes. In this
mode ``--no-follow`` is implied automatically, and only a single definition
file may be given. See :doc:`../ci/index` for the full CI integration guide
and ready-to-use pipeline snippets.

Output
------

While following, the submitted job ID (or URL with ``--url``) is written to
stderr and the formatted logs stream to stdout. With ``--no-follow`` the job
ID (or URL) is written to stdout.

.. note:: **TODO:** Add an example of the streamed log output.
