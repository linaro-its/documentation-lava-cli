device-types commands
======================

The ``device-types`` commands query and manage LAVA device types. A device
type describes a class of hardware (for example a particular board), and
carries the *device dictionary template* and *health-check* definitions used
by every device of that type.

Listing and showing device types is available to anyone with access to the
subscription. Creating and updating device types, and changing templates or
health-checks, require separate permissions. Visiting https://hub.linaro.com/device-types
or https://staging-hub.linaro.com/device-types will display an informational banner
if you do not have those additional permissions.

.. toctree::
   :maxdepth: 1

   list
   show
   add
   update
   template
   health-check
