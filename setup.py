from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'Nokia_LCD',
	  version 			= '1.0',
	  author			= 'Coding World',
	  author_email		= 'support@codingworld.io',
	  description		= 'Diese Bibliothek zeigt Inhalte auf einem Nokia 5110 Display mit Python und dem Raspberry Pi an',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/Adafruit_Nokia_LCD/',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.1.0'],
	  install_requires	= ['Adafruit-GPIO>=0.1.0'],
	  packages 			= find_packages())
