# AppSalesGraph: AppStore Sales Graphing
# Copyright (c) 2010 by Max Klein (maximusklein@gmail.com)
#
# GNU General Public Licence (GPL)
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#


"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import matplotlib
import glob

img = ("images", glob.glob("images/*.*"))
DATA_FILES = matplotlib.get_py2exe_datafiles()
DATA_FILES.append(img)
DATA_FILES.append("currencies.key")
DATA_FILES.append("glass.wav")
DATA_FILES.append("key.ico")

APP = ['salesgraph.py']

OPTIONS = {'argv_emulation': True,
 'iconfile': 'key.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
	name = "SalesGraph",
    description = "Software Sales Plotting Tool",
    version = "1.0",
)
