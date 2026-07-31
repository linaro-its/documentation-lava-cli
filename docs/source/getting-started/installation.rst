.. _installation:

Installing the CLI
==================

The LAVA CLI is distributed as a single self-contained binary, built for
Linux on both ``amd64`` and ``arm64`` architectures.

Where to download
-----------------

Release binaries are published to GitHub:

* Production: https://github.com/Linaro/LAVA-CLI/releases
* Staging: https://github.com/Linaro/LAVA-CLI-S-/releases

.. note:: For most users, the production release is the correct one to use.
   Only use the staging build under direct instruction from Linaro. The
   production binary is named ``lava-cli``; the staging binary is named
   ``staging-lava-cli``.

Installing from a release archive
---------------------------------

Each release provides a ``.tar.gz`` archive per architecture (and a ``.zip``
for Windows). A Debian ``.deb`` package is also published. Download the
archive that matches your platform and extract the binary. The archive is
named after the release project and unpacks into a directory of the same
name:

.. code-block:: bash

   curl -sSL "https://github.com/Linaro/LAVA-CLI/releases/download/<version>/LAVA-CLI_<version>_linux_amd64.tar.gz" \
     | tar -xz --strip-components=1 LAVA-CLI_<version>_linux_amd64/lava-cli

For the staging build, substitute the ``LAVA-CLI-S-`` repository and archive
prefix, and the ``staging-lava-cli`` binary name.

This leaves a ``lava-cli`` executable in the current directory. Move it to a
directory on your ``$PATH`` so it can be run from anywhere:

.. code-block:: bash

   sudo mv lava-cli /usr/local/bin/

Installing from the Debian package
----------------------------------

On Debian-based distributions you can install the published ``.deb`` package
instead:

.. code-block:: bash

   sudo dpkg -i lava-cli_<version>_linux_amd64.deb

The package installs the ``lava-cli`` binary onto your ``$PATH``.

Verifying the installation
--------------------------

Check that the CLI runs and reports its version:

.. code-block:: bash

   lava-cli --version

.. note:: **TODO:** Add the expected ``lava-cli --version`` output once a release
   version string is available.

Upgrading
---------

The CLI checks GitHub for newer releases and will notify you on stderr when a
newer version is available. To upgrade, download and replace the binary using
the same steps as the initial installation.

.. note:: **TODO:** Document any dedicated self-update command or flag if one
   is added. At present, upgrading is a manual re-download.
