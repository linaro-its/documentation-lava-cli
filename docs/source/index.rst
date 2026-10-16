LAVA CLI
########

``lava-cli`` is a command line tool for interacting with LAVA via subscriptions
on Linaro's Solutions Hub. It submits and manages test jobs, inspects devices and
workers, manages device types, and integrates LAVA into CI pipelines.

The CLI authenticates using an email address and personal
access token (PAT). A subscription determines
which devices, workers and jobs you can see and act on.

.. note:: The CLI only allows the operations that are permitted by the
   access granted to you in the subscription. If a command returns a
   permission error, your subscription does not grant that capability.

.. note:: The documented commands always reference ``lava-cli``, which is the
   name of the production binary. If you have installed the staging build, the
   binary is named ``staging-lava-cli`` instead. Substitute the name of your
   binary where appropriate.

Start with the :ref:`getting started <getting-started>` section to install
the CLI and configure your credentials, then explore the command reference
below.

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   getting-started/index
   getting-started/installation
   getting-started/authentication
   getting-started/configuration
   getting-started/global-options

.. toctree::
   :maxdepth: 2
   :caption: Command reference

   identities/index
   devices/index
   device-types/index
   workers/index
   tags/index
   jobs/index
   events/index
   system/index
   mcp/index
   utils/index
   ci/index
