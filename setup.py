#!/usr/bin/env python

from setuptools import setup, find_packages
import glob

setup(
	name = 'listacs',
	version = '0.0.0',
	description = "ListACS is an ACS disassembler that supports ZDoom's ACS extensions.",
	url = 'https://github.com/alexey-lysiuk/ListACS',
	author = 'Alexey Lysiuk, Jared Stafford',
	author_email = '',
	license = 'BSD',
	classifiers = [
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
	],
	packages = find_packages(),
	scripts = glob.glob("listacs/listacs.py"),
)

