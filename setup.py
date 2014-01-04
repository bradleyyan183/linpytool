#!/usr/bin/env python

try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

setup(name='linpytool',
      version='0.1',
      description='A tool for Linux system administration',
      author = 'Liang Yan',
      author_email='flashyan83@gmail.com',
      url='https://github.com/bradleyyan183/linpytool',
      packages=['linpytool'],
     )
