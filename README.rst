.. --------------------------------License Notice----------------------------------
.. Roster - A member and community management web application for CieFa-ArmA
.. Copyright (C) 2018 Mickaël 'lastmikoi' FALCK <lastmikoi@lastmikoi.net>
..
.. This program is free software: you can redistribute it and/or modify
.. it under the terms of the GNU Affero General Public License as published
.. by the Free Software Foundation, either version 3 of the License, or
.. (at your option) any later version.
..
.. This program is distributed in the hope that it will be useful,
.. but WITHOUT ANY WARRANTY; without even the implied warranty of
.. MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.. GNU Affero General Public License for more details.
..
.. You should have received a copy of the GNU Affero General Public License
.. along with this program.  If not, see <https://www.gnu.org/licenses/>.
.. --------------------------------License Notice----------------------------------

A member and community management web application for CieFa-ArmA
################################################################

Features
********

Implemented
===========

Upcoming (planned)
==================

* Community member management, with ranks and roles
* Display of community reward ribbons and medals
* Community event registration, scheduling and RSVP
* Community announcements, with delivery tracking
* Main community landing page, with *photos* blogging
* Knowledge document index

Usage
*****

Installation
============

Set up your virtualenv, then install the package in development mode, including the extra
development and testing dependencies::

   pip install -e '.[dev,test]'

Testing
=======

From your virtualenv, you may start the full test suite using the following command::

   tox

You also may only run a subset of the test suite by overriding the default `tox` environments to
create and execute::

   tox -e py36,coverage

Here is a listing of supported `tox` environments that complement the `default ones <https://tox.readthedocs.io/en/latest/example/basic.html#a-simple-tox-ini-default-environments>`_:

* ``coverage``: Merges all default test environments-issues coverage files and generates both a CLI and XML report. Fails if coverage is under 100%
* ``safety``: Runs the `Safety <https://pyup.io/safety/>`_ checker against all project
  dependencies. Fails if any security vulnerability is found.

Licensing
*********

Copyright (C) 2018 Mickaël 'lastmikoi' FALCK <lastmikoi@lastmikoi.net>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

A copy of the GNU Affero General Public License can be found in the
LICENSE.txt file.
