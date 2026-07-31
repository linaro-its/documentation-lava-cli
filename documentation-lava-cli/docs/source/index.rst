Linaro LAVA CLI
###############

``lava-cli`` is a command line tool for interacting with Linaro's LAVA
Gateway REST API. It submits and manages test jobs, inspects devices and
workers, manages device types, and integrates LAVA into CI pipelines.

The CLI authenticates against SPIRE using an email address and personal
access token (PAT), then exchanges those credentials for a
subscription-scoped `Biscuit <https://www.biscuitsec.org/>`_ token that
authorises every subsequent call to the Gateway. A subscription determines
which devices, workers and jobs you can see and act on.

.. note:: The CLI only allows the operations that are permitted by the
   permissions held in your authorisation token. If a command returns a
   permission error, your subscription does not grant that capability.

.. note:: The documented commands always reference ``lava``. Depending on
   which build you have installed this may instead be ``staging-lava``
   (staging) or ``lava-cli`` (a local development build). Substitute the name
   of your binary where appropriate.

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
   utils/index
   ci/index
