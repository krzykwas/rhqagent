#-*- coding: utf-8 -*-
#
# Krzysztof „krzykwas” Kwaśniewski
# Gdańsk, 28-07-2012
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup
from setuptools import find_packages

setup(
	name = "pyagent",
	packages = find_packages(),
	package_data = {
		"pyagent.settings" : [
			"sample_settings.xml",
			"settings.xsd",
		],
	},
	scripts = [
		"pyagent.py",
	],
	data_files = [
		("/etc/init.d", ["run-pyagent.sh"])
	],
	version = "1.0",
	author = "Krzysztof Kwaśniewski",
	author_email = "krzykwas@gmail.com",
	url = "http://rhqagent.blogspot.com/",

	description = "RHQ agent gathering data from CIM servers",
	long_description = """\
RHQ agent gathering data from CIM servers
-----------------------------------------

	With a single agent instance you can simultaneously gather data
from many CIM instances and send them to many RHQ servers. You can even
compute so called artificial metrics on your own by defining and using
callbacks. This way you can combine several CIM metrics and create
a brand new one on your own.

	If you wish, you can quite easily extend the agent so that it
was able to communicate with different protocols as well - for that you
have to implement a suitable data provider and/or sender. As a simple
example, you might want to send data to a flat file or a database
or get it from such a source.

	The agent includes an interactive configuration file generator.

	This version depends on a python-wbem library to be able to
communicate with CIM servers using a CIM-XML protocol. This library is
Python 2.x-only and unless you'll implement a provider for another data
source, you are bound to Python 2.x. Nevertheless there should be few
changes needed to make the agent work with Python 3 if any at all.
""",

	classifiers = [
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: System Administrators",
		"Topic :: System :: Monitoring",
		"Topic :: System :: Networking :: Monitoring",
		"Topic :: System :: Systems Administration",
	],
)
