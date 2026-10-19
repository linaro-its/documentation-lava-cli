MCP tools
=========

This page enumerates every tool exposed by ``lava-cli mcp``, grouped by
area (jobs, devices, device-types, workers, documentation), along with
whether each tool is read-only or changes LAVA state. It is kept in sync
with the shipped tool registrations in ``lava-cli``'s
``cmd/mcp_tools_*.go`` files.

Every tool is scoped to the single subscription the server was started
with (see :doc:`index`). Tools marked **Write** change LAVA state and are
annotated so that MCP clients which support confirmation prompts can gate
them before running.

Example: investigating a failed job
------------------------------------

A typical investigation starts with a prompt like:

    "Job 412122 failed, can you tell me why?"

An LLM connected to ``lava-cli mcp`` can work through this without any
further help:

#. Call ``job_show`` with ``job_id: "412122"`` to see the job's state,
   health, device type and device.
#. Call ``job_find_errors`` with the same ``job_id`` to pull just the
   error-level log entries, or ``job_logs`` (with a ``start``/``limit``
   window) if it needs more surrounding context than the error lines
   alone provide.
#. Call ``job_config`` if it needs the exact device, dispatcher or
   environment configuration that ran, to rule out a device-specific
   misconfiguration.
#. Call ``job_definition`` if it needs to check the originally submitted
   job YAML against what actually ran.

None of these tools change anything in LAVA. If the investigation turns
up a transient failure, the model might then offer to call
``job_resubmit``, which does change state and would be flagged to you as
such by your MCP client before it runs.

Jobs
----

.. list-table::
   :header-rows: 1
   :widths: 18 32 32 18

   * - Tool
     - Description
     - Parameters
     - Read-only/Write
   * - ``jobs_list``
     - List jobs in this subscription. Equivalent to ``lava-cli jobs
       list``.
     - ``device`` (optional), ``count`` (optional, default 25), ``start``
       (optional), ``ordering`` (optional), ``health`` (optional),
       ``state`` (optional), ``since`` (optional)
     - Read-only
   * - ``job_show``
     - Show details for one job: id, description, state, health, device
       type, device, and timings.
     - ``job_id`` (required), ``device`` (optional)
     - Read-only
   * - ``job_definition``
     - Return the job definition YAML as originally submitted.
     - ``job_id`` (required), ``device`` (optional)
     - Read-only
   * - ``job_config``
     - Return the device/dispatcher configuration documents
       (``definition``, ``device``, ``dispatcher``, ``env``, ``env_dut``)
       used while running one job, directly (nothing written to disk).
     - ``job_id`` (required), ``device`` (optional)
     - Read-only
   * - ``job_logs``
     - Fetch a bounded page of a job's structured log entries (``dt``,
       ``lvl``, ``msg``). Does not fetch the entire log by default.
     - ``job_id`` (required), ``device`` (optional), ``start`` (optional,
       default 0), ``limit`` (optional, default 2000)
     - Read-only
   * - ``job_find_errors``
     - Return the error-level log entries for one job. Equivalent to
       ``lava-cli jobs find-errors``.
     - ``job_id`` (required), ``device`` (optional)
     - Read-only
   * - ``job_results``
     - Fetch test results (suites and cases) for one job, optionally
       filtered to a suite and/or case.
     - ``job_id`` (required), ``device`` (optional), ``suite`` (optional),
       ``case`` (optional)
     - Read-only
   * - ``jobs_queue``
     - List queued and scheduled jobs for a device type. Equivalent to
       ``lava-cli jobs queue``.
     - ``device_type`` (optional), ``count`` (optional, default 25),
       ``offset`` (optional)
     - Read-only
   * - ``job_submit``
     - Submit a job definition. Equivalent to ``lava-cli jobs submit
       --no-follow`` with a single definition and no CI-callback flags.
       Returns the submitted job id(s) without streaming logs.
     - ``definition`` (required), ``device`` (optional)
     - Write
   * - ``job_cancel``
     - Cancel a running or queued job. Equivalent to ``lava-cli jobs
       cancel <job_id>``.
     - ``job_id`` (required), ``device`` (optional)
     - Write
   * - ``job_resubmit``
     - Resubmit a completed or failed job. Equivalent to ``lava-cli jobs
       resubmit --no-follow <job_id>``. Returns the new job id(s) without
       streaming logs.
     - ``job_id`` (required), ``device`` (optional)
     - Write

Devices
-------

.. list-table::
   :header-rows: 1
   :widths: 18 32 32 18

   * - Tool
     - Description
     - Parameters
     - Read-only/Write
   * - ``devices_list``
     - List devices in this subscription: hostname, device type, worker,
       appliance name, health, and state. Equivalent to ``lava-cli devices
       list``.
     - ``all`` (optional, include retired devices)
     - Read-only
   * - ``device_show``
     - Show details for one device: device type, worker, appliance name,
       health, state, description, and tags. Equivalent to ``lava-cli
       devices show <hostname>``.
     - ``hostname`` (required)
     - Read-only
   * - ``device_tags``
     - List the tags configured on a device. Equivalent to ``lava-cli
       tags list --device <hostname>``.
     - ``device`` (required)
     - Read-only
   * - ``device_maintenance``
     - Set a device's health to ``Maintenance`` or ``Good``. Equivalent to
       ``lava-cli devices maintenance <hostname> --health <value>``.
     - ``hostname`` (required), ``health`` (required, ``Maintenance`` or
       ``Good``)
     - Write

``worker`` and ``appliance_name`` are distinct identifiers: ``worker`` is
the LAVA worker hostname (e.g. ``laa-00046``), assigned when the dispatcher
was registered with LAVA. ``appliance_name`` is the LMS display name of the
Linaro Automation Appliance behind that worker (e.g.
``laa-46-remi-starterkv260``), and is ``null`` for devices on a shared LAVA
worker rather than a dedicated appliance. The two names are not derived
from each other.

Device types
------------

.. list-table::
   :header-rows: 1
   :widths: 18 32 32 18

   * - Tool
     - Description
     - Parameters
     - Read-only/Write
   * - ``device_types_list``
     - List device types available to this subscription, with the devices
       of each type. Equivalent to ``lava-cli device-types list``.
     - *(none)*
     - Read-only
   * - ``device_type_show``
     - Show metadata for a device type: verbose name, uuid, visibility,
       description, tags, and the caller's effective permissions.
       Equivalent to ``lava-cli device-types show <name>``.
     - ``name`` (required)
     - Read-only
   * - ``device_type_template``
     - Return the latest device dictionary template revision for a
       device type. Equivalent to ``lava-cli device-types template get
       <name>``.
     - ``name`` (required)
     - Read-only
   * - ``device_type_health_check``
     - Return the latest health-check revision for a device type.
       Equivalent to ``lava-cli device-types health-check get <name>``.
     - ``name`` (required)
     - Read-only
   * - ``device_type_template_set``
     - Create a new device dictionary template revision for a device
       type, preserving the existing health-check content unchanged.
       Equivalent to ``lava-cli device-types template set <name>
       <file>``.
     - ``name`` (required), ``content`` (required), ``message``
       (optional)
     - Write
   * - ``device_type_health_check_set``
     - Create a new health-check revision for a device type, preserving
       the existing device dictionary template unchanged. Equivalent to
       ``lava-cli device-types health-check set <name> <file>``.
     - ``name`` (required), ``content`` (required), ``message``
       (optional)
     - Write

Workers
-------

.. list-table::
   :header-rows: 1
   :widths: 18 32 32 18

   * - Tool
     - Description
     - Parameters
     - Read-only/Write
   * - ``workers_list``
     - List workers accessible to this subscription: hostname, appliance
       name, state, health, description. Covers both shared LAVA workers
       and LAA-backed workers (Linaro Automation Appliances) in one list
       — there is no separate tool for appliances. Equivalent to
       ``lava-cli workers list``.
     - *(none)*
     - Read-only
   * - ``worker_show``
     - Show details for one worker, identified by its worker hostname
       (shared worker or LAA-backed worker): appliance name, state,
       health, description, last ping, version. Equivalent to
       ``lava-cli workers show <hostname>``.
     - ``hostname`` (required)
     - Read-only

``hostname`` is the LAVA worker hostname (e.g. ``laa-00046``).
``appliance_name`` is the LMS display name of the Linaro Automation
Appliance behind that worker (e.g. ``laa-46-remi-starterkv260``) — a
separate identifier assigned in a different system, not derived from the
hostname — and is ``null`` for shared workers that have no dedicated
appliance.

Documentation
-------------

These two tools read directly from the ``lava/lava`` GitLab repository and
do not touch the resolved subscription, Gateway, SPIRE, or LMS at all.

.. list-table::
   :header-rows: 1
   :widths: 18 32 32 18

   * - Tool
     - Description
     - Parameters
     - Read-only/Write
   * - ``documentation_list``
     - List the official LAVA documentation pages as a map of page name to
       title.
     - *(none)*
     - Read-only
   * - ``documentation_fetch``
     - Fetch one documentation page's markdown content, with snippet
       includes resolved and links rewritten to page names. Use
       ``documentation_list`` first to find a page name.
     - ``page`` (required)
     - Read-only
