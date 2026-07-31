.. _getting-started:

Getting started
===============

This section covers everything you need to start using the LAVA CLI:
installing the binary, authenticating against SPIRE, storing reusable
configuration profiles, and the global options that apply to every command.

.. toctree::
   :maxdepth: 1

   installation
   authentication
   configuration
   global-options

A typical first session looks like this:

.. code-block:: bash

   # Provide your credentials (once per shell session)
   export LAVA_CLI_USER="you@example.com"
   export LAVA_CLI_PAT="<your-personal-access-token>"

   # Discover which subscriptions you can use with LAVA
   lava identities list --discover

   # Save a subscription as a named profile
   lava identities add

   # Confirm who you are and what you can access
   lava system whoami

   # List the devices in your subscription
   lava devices list
