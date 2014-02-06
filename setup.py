import os
from setuptools import setup, find_packages
from querycontacts._version import __version__

name = 'querycontacts'
description = "Query network abuse contacts on the command-line for a given ip address on abuse-contacts.abusix.org"
long_description = description
cur_dir = os.path.abspath(os.path.dirname(__file__))


with open('%s/README.rst' % cur_dir, 'r') as f:
    long_description = f.read()

with open('%s/requirements.txt' % cur_dir) as f:
    requires = f.readlines()

setup(
    name=name,
    version=__version__,
    description=description,
    long_description=long_description,
    packages=find_packages()
    author='abusix GmbH',
    author_email='info@abusix.com',
    url='http://abusix.com/global-reporting/abuse-contact-db',
    install_requires=requires,
    scripts=['scripts/querycontacts'],
    license="GNU General Public License v3 (GPLv3)",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Customer Service',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ]
)
