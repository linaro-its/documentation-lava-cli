device-types commands
======================

The ``device-types`` commands query and manage LAVA device types. A device
type describes a class of hardware (for example a particular board), and
carries the *device dictionary template* and *health-check* definitions used
by every device of that type.

Listing and showing device types is available to anyone with access to the
subscription. Creating and updating device types, and changing templates or
health-checks, require additional LMS (LAVA Management Service) permissions
(``lms:admin`` or the relevant ``lms:create``/``lms:update`` right).

.. note:: Device type names are resolved to an internal UUID before any
   detail is fetched. If a name is not found, the CLI reports a combined
   "not found or access denied" error. This is deliberate: it avoids
   revealing whether a device type exists to callers who are not allowed to
   see it.

.. toctree::
   :maxdepth: 1

   list
   show
   add
   update
   template
   health-check
