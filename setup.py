#!/usr/bin/env python

# Volatility
# 
# Authors:
# AAron Walters <awalters@4tphi.net>
# Mike Auty <mike.auty@gmail.com>
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#
from setuptools import setup

setup(
    name="volatility"
    version="2.6.2"
    description="Volatility -- Volatile memory framework"
    author="AAron Walters"
    author_email="awalters@4tphi.net"
    url="http://www.volatilityfoundation.org"
    license= "GPL"
    scripts= ["vol.py"]
    packages=["volatility",
        "volatility.win32",
        "volatility.renderers",
        "volatility.plugins",
        "volatility.plugins.addrspaces",
        "volatility.plugins.overlays",
        "volatility.plugins.overlays.windows",
        "volatility.plugins.overlays.linux",
        "volatility.plugins.overlays.mac",
        "volatility.plugins.gui",
        "volatility.plugins.gui.vtypes",
        "volatility.plugins.linux",
        "volatility.plugins.registry",
        "volatility.plugins.malware", 
        "volatility.plugins.mac",
    ]
    install_requires=['socket', 'ctypes', 'Crypto.Cipher', 'urllib', 'distorm3', 'yara', 'xml.etree.ElementTree']
)
