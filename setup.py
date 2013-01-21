import os
from setuptools import setup, find_packages

description = "Query network abuse contacts on the command-line for a given ip address on abuse-contacts.abusix.org"
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.rst')).read()
except:
    long_description = description

setup(name='querycontacts',
      version='0.1.1',
      description=description,
      long_description=long_description,
      author='Dean Ceulic',
      author_email='dc@abusix.com',
      url='http://abusix.com/global-reporting/abuse-contact-db',
      install_requires = ['dnspython', 'pyCLI'],
      scripts=['querycontacts'],
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
