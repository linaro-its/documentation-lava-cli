MCP client setup
================

This page shows how to point an MCP client at ``lava-cli mcp``, using
Kiro and Claude Desktop as examples. See :doc:`index` for the command
itself (flags, transports, and the "one server, one subscription" model)
and :doc:`tools` for the full tool inventory. For credential and
subscription setup, see :ref:`authentication` and :ref:`configuration`;
this page assumes you already have a working identity profile and does
not repeat that setup.

Both examples below launch the server with ``--identity <name>``, which
determines which subscription the server session is scoped to for its
whole lifetime. If you omit it, the ``default`` profile is used instead.
See :doc:`index`'s "One server, one subscription" section for details.

Kiro
----

Kiro stores MCP server configuration as JSON, either per-workspace
(``.kiro/settings/mcp.json`` in the project) or per-user (applies to
every workspace). Open either file from the Command Palette: "Kiro: Open
workspace MCP config (JSON)" or "Kiro: Open user MCP config (JSON)".
Workspace entries take precedence over user entries when a server name
collides.

stdio
~~~~~

Kiro launches the server itself and talks to it over stdio, so no port
management is needed:

.. code-block:: json

   {
     "mcpServers": {
       "lava-cli": {
         "command": "lava-cli",
         "args": ["--identity", "team-a", "mcp"],
         "disabled": false,
         "autoApprove": []
       }
     }
   }

streamable-http
~~~~~~~~~~~~~~~

To connect to an already-running server instead, start it with
``--transport streamable-http`` and point Kiro at its URL:

.. code-block:: bash

   lava-cli --identity team-a mcp --transport streamable-http --port 8001

.. code-block:: json

   {
     "mcpServers": {
       "lava-cli-team-a": {
         "url": "http://127.0.0.1:8001",
         "disabled": false,
         "autoApprove": []
       }
     }
   }

Since ``lava-cli mcp`` binds to ``127.0.0.1`` by default (loopback only,
no TLS), the plain ``http://`` form is used here; Kiro only allows
unencrypted HTTP for localhost endpoints like this one.

Claude Desktop
--------------

stdio
~~~~~

Claude Desktop also supports launching local stdio servers, configured
in ``claude_desktop_config.json`` (opened via Settings > Developer > Edit
Config in the app; ``~/Library/Application Support/Claude/claude_desktop_config.json``
on macOS, ``%APPDATA%\Claude\claude_desktop_config.json`` on Windows):

.. code-block:: json

   {
     "mcpServers": {
       "lava-cli": {
         "command": "lava-cli",
         "args": ["--identity", "team-a", "mcp"]
       }
     }
   }

Claude Desktop launches this process without sourcing your shell
profile, so if ``lava-cli`` is not on the PATH visible to GUI
applications, use an absolute path in ``command`` instead of relying on
PATH lookup.

streamable-http
~~~~~~~~~~~~~~~

Unlike Kiro, ``claude_desktop_config.json`` has no field for a remote
server URL; adding one does not do anything. Instead, start the server
with ``--transport streamable-http`` and add it through the app's UI:
Settings > Connectors > Add connector > "Remote", then enter the
server's URL (for example ``http://127.0.0.1:8000``) and choose
"Streamable HTTP" under the connector's advanced settings. Claude
Desktop's Connectors feature is primarily meant for genuinely remote,
networked servers, so pointing it at a local ``lava-cli mcp`` instance
this way is a less common setup than stdio.

Which transport to use
----------------------

Start with stdio: the client launches and manages the process for you,
so there is no port to pick or server to keep running separately. Reach
for ``streamable-http`` instead when you need a single running server
shared by more than one client, or when a client can only connect over
HTTP rather than launching subprocesses itself.
