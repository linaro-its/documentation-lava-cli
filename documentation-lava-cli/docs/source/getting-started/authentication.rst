.. _authentication:

Authentication
==============

Every command that talks to the LAVA Gateway must be authenticated. The CLI
does not maintain a login session or cache tokens: it authenticates fresh on
each invocation.

How authentication works
------------------------

When you run a command that calls the API, the CLI performs a three-step
flow:

#. It exchanges your **email address** and **personal access token (PAT)**
   with SPIRE for a *full* Biscuit token.
#. It reads the LAVA subscription rights out of that token.
#. It exchanges the full token for a *subscription-scoped* Biscuit token,
   which authorises every call the command makes to the Gateway.

Because tokens are always fetched fresh and never written to disk, there is no
``login`` or ``logout`` command.

Providing credentials
---------------------

Your email and PAT can be supplied either as flags or as environment
variables. Environment variables are usually more convenient because they
apply to every command in the shell session and keep secrets out of your
command history.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Flag
     - Environment variable
     - Purpose
   * - ``-e``, ``--email``
     - ``LAVA_CLI_USER``
     - The email address of your Linaro account.
   * - ``-p``, ``--pat``
     - ``LAVA_CLI_PAT``
     - A personal access token issued for your account.

.. code-block:: bash

   # Using environment variables (recommended)
   export LAVA_CLI_USER="you@example.com"
   export LAVA_CLI_PAT="<your-personal-access-token>"
   lava devices list

   # Using flags
   lava --email you@example.com --pat <token> devices list

If neither the flags nor the environment variables are set for a command that
needs to reach the API, the CLI stops with an error explaining that an email
and PAT are required.

.. note:: **TODO:** Document where and how a user obtains a personal access
   token (the SPIRE / Solutions Hub portal URL and the steps to create one),
   and any required token scopes.

Choosing a subscription
-----------------------

A LAVA subscription scopes what you can access. The subscription used for a
command is resolved in the following order of precedence:

#. The ``-s`` / ``--subscription`` flag.
#. The ``LAVA_CLI_SUBSCRIPTION`` environment variable.
#. The ``subscription_id`` stored in the selected configuration profile (see
   :ref:`configuration`).

If no subscription can be resolved, the CLI stops with an error. Subscription
IDs have the form ``sub:<uuid>``, for example
``sub:464ef0f9-e987-4f48-a065-cb6719915747``.

To discover which subscriptions your account can use with LAVA, run:

.. code-block:: bash

   lava identities list --discover

Commands that do not require authentication
-------------------------------------------

A few commands run entirely locally and do not authenticate:

* ``lava identities`` (managing configuration profiles)
* ``lava system version`` and ``lava system api``
* ``lava utils`` (local log formatting)
* ``lava ci examples`` (printing CI pipeline snippets)

Debugging authentication
------------------------

Add the global ``--debug`` flag to any command to print the resolved Gateway,
SPIRE and subscription details, plus token expiry times, to stderr. This is
useful when diagnosing authentication or permission problems.

.. code-block:: bash

   lava --debug devices list
