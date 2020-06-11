# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in discount_approval/__init__.py
from discount_approval import __version__ as version

setup(
	name='discount_approval',
	version=version,
	description='App for approval of proposed discount',
	author='Quantum Lambs',
	author_email='perkasajob@quantum-laboratories.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
