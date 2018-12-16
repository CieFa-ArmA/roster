# --------------------------------License Notice----------------------------------
# Roster - A member and community management web application for CieFa-ArmA
# Copyright (C) 2018 Mickaël 'lastmikoi' FALCK <lastmikoi@lastmikoi.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# --------------------------------License Notice----------------------------------

"""Setuptools-backed setup module."""

import codecs
import os

import setuptools


if __name__ == '__main__':
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

    # Use README.rst as source for setuptools.setup's long_description param
    with codecs.open(os.path.join(ROOT_DIR, 'README.rst'),
                     encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()

    setuptools.setup(
        # Distutils parameters
        name='roster',
        description='A member and community management web application for CieFa-ArmA',
        long_description=LONG_DESCRIPTION,
        author="Mickaël 'lastmikoi' FALCK",
        author_email='lastmikoi@lastmikoi.net',
        url='https://github.com/CieFa-ArmA/roster',
        packages=setuptools.find_packages(exclude=['tests']),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        ],
        keywords='ciefa-arma arma web webapp member management',
        # Setuptools parameters
        include_package_data=True,
        install_requires=[
        ],
        extras_require={
            'dev': [
                'ipython>=7.2.0,<8',
            ],
            'test': [
                'tox>=3.5.3,<4',
                'pytest>=4.0.1,<5',
                'pytest-mock>=1.10.0,<2',
            ],
        },
        python_requires='>=3.6,<4',
        setup_requires=['setuptools_scm'],
        # setuptools_scm parameters
        use_scm_version=True,
    )
