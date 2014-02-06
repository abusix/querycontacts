import os
from setuptools import setup, find_packages

name = 'querycontacts'
description = "Query network abuse contacts on the command-line for a given ip address on abuse-contacts.abusix.org"
long_description = description
cur_dir = os.path.abspath(os.path.dirname(__file__))

# Read Version
execfile('%s/querycontacts/_version.py' % (cur_dir))

with open('%s/README.rst' % cur_dir, 'r') as f:
    long_description = f.read()

with open('%s/requirements.txt' % cur_dir) as f:
    requires = f.readlines()

setup(
    name=name,
    version=__version__,
    description=description,
    long_description=long_description,
    author='abusix GmbH',
    author_email='info@abusix.com',
    url='http://abusix.com/global-reporting/abuse-contact-db',
    install_requires=requires,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
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
