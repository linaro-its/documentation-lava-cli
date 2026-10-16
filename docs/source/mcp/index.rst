``lava-cli mcp``
================

Start an MCP (Model Context Protocol) server that exposes **exactly the
calling subscription's existing access** as a set of tools for an MCP
client such as Claude Desktop or Kiro: the server does not grant any
rights beyond what the authenticated identity can already see and do
with ``lava-cli`` itself. Most tools are read-only (listing and
inspecting jobs, devices, device-types and workers), but a handful
change LAVA state, including submitting, cancelling or resubmitting
jobs, and setting device maintenance mode, device-type templates or
device-type health checks. These state-changing tools are flagged as
such to the connecting MCP client, but you should know before wiring an
LLM up to this server that it is capable of taking those actions. See
:doc:`tools` for the full tool inventory and which tools are read-only
versus state-changing.

Usage
-----

.. code-block:: text

   lava-cli mcp [flags]

By default the server speaks MCP over stdio, which is what most MCP
clients expect when they launch the server themselves. Use
``--transport streamable-http`` to instead run it as an HTTP server that
clients connect to over the network.

Flags
-----

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Flag
     - Default
     - Description
   * - ``--transport``
     - ``stdio``
     - Transport to serve MCP over: ``stdio`` or ``streamable-http``.
   * - ``--host``
     - ``127.0.0.1``
     - Host to bind to. Only used when ``--transport streamable-http``.
   * - ``--port``
     - ``8000``
     - Port to listen on. Only used when ``--transport streamable-http``.

The usual global flags also apply, in particular ``-i``/``--identity``,
``-s``/``--subscription`` and ``--debug`` (see :ref:`global-options`).

One server, one subscription
-----------------------------

Each ``lava-cli mcp`` process is scoped to a single subscription for its
whole lifetime, resolved the same way as for any other ``lava-cli``
command: via ``--identity``/``--subscription`` and the usual
precedence rules described in :ref:`configuration` and
:ref:`authentication`. The server does not switch subscriptions or
re-authenticate while it is running, and it does not let a client ask
for a different subscription than the one it was started with.

If you need to work with more than one subscription at the same time,
run a separate server process per subscription, each pointed at a
different identity, and give each HTTP server its own port:

.. code-block:: bash

   # Terminal 1: subscription "team-a"
   lava-cli --identity team-a mcp

   # Terminal 2: subscription "team-b", a different local port for HTTP
   lava-cli --identity team-b mcp --transport streamable-http --port 8001

Next steps
----------

* :doc:`tools` lists every tool the server exposes, grouped by area, and
  marks which ones change LAVA state.
* :doc:`clients` walks through configuring specific MCP clients (such as
  Claude Desktop and Kiro) to launch or connect to this server.

.. toctree::
   :maxdepth: 1

   tools
   clients
