.. _global-options:

Global options
==============

The following options are *persistent* flags: they can be given on any
command, before or after the subcommand name. They control credentials,
subscription selection and diagnostics.

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Flag
     - Default
     - Description
   * - ``-i``, ``--identity``
     - ``default``
     - Name of the configuration profile to use (see :ref:`configuration`).
   * - ``-s``, ``--subscription``
     -
     - Override the subscription ID (``sub:<uuid>``) for this invocation.
   * - ``-e``, ``--email``
     -
     - Email address for SPIRE authentication (or set ``LAVA_CLI_USER``).
   * - ``-p``, ``--pat``
     -
     - Personal access token (or set ``LAVA_CLI_PAT``).
   * - ``--debug``
     - ``false``
     - Log HTTP and authentication details to stderr.
   * - ``--version``
     -
     - Print the CLI version and exit.
   * - ``-h``, ``--help``
     -
     - Show help for a command.

Environment variables
----------------------

Several options can be supplied through environment variables instead of
flags. This is the recommended approach for credentials and for CI.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Variable
     - Purpose
   * - ``LAVA_CLI_USER``
     - Email address for SPIRE authentication.
   * - ``LAVA_CLI_PAT``
     - Personal access token.
   * - ``LAVA_CLI_SUBSCRIPTION``
     - Subscription ID to use when no ``--subscription`` flag is given.
   * - ``LAVA_CLI_GITLAB_TOKEN``
     - GitLab API token used by the CI callback integration.
   * - ``LAVA_CLI_GITHUB_TOKEN``
     - GitHub token used by the CI callback integration.

Getting help
------------

Every command and subcommand supports ``--help``:

.. code-block:: bash

   lava --help
   lava jobs --help
   lava jobs submit --help
