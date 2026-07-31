ci commands
===========

The ``ci`` commands support integrating LAVA into a CI pipeline. The core
integration is driven by callback flags on :doc:`../jobs/submit`; the ``ci``
command group provides a helper to print ready-to-use pipeline snippets.

How CI callbacks work
---------------------

When you submit a job from inside a CI pipeline with a callback flag, the CLI
asks the Gateway to notify your CI system when the LAVA job finishes. This
lets a pipeline submit a job, do other work (or pause), and react to the LAVA
result without polling. The CI platform is auto-detected from environment
variables, so no explicit platform flag is needed.

Three callback strategies are supported:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Platform
     - Strategy
     - Detection
   * - GitLab CI
     - ``gitlab``
     - ``GITLAB_CI=true`` and ``--gitlab-wait-job`` given
   * - GitHub Actions
     - ``github-dispatch`` (default)
     - ``GITHUB_ACTIONS=true`` and ``--github-repo`` given
   * - GitHub Actions
     - ``github-environment``
     - as above, plus ``--github-strategy environment``

The relevant ``jobs submit`` flags are ``--gitlab-wait-job``,
``--gitlab-token``, ``--github-repo``, ``--github-strategy`` and
``--github-token``. See :doc:`../jobs/submit` for their definitions.

Tokens
------

.. important:: The short-lived tokens that CI runners provide by default
   (``CI_JOB_TOKEN`` on GitLab, ``GITHUB_TOKEN`` on GitHub Actions) **cannot**
   be used for the callback. They expire when the submitting job ends, but the
   callback fires later when the LAVA job finishes. You must supply a
   longer-lived token:

   * **GitLab:** a project access token with ``api`` scope and the Maintainer
     role, provided via ``--gitlab-token`` or ``LAVA_CLI_GITLAB_TOKEN``.
   * **GitHub (dispatch):** a fine-grained PAT with *Contents — Read and
     Write*, provided via ``--github-token`` or ``LAVA_CLI_GITHUB_TOKEN``.
   * **GitHub (environment):** a fine-grained PAT with *Deployments — Read and
     Write*, from an account listed as a required reviewer on the environment,
     provided via ``--github-token`` or ``LAVA_CLI_GITHUB_TOKEN``.

.. toctree::
   :maxdepth: 1

   examples
