import os
from setuptools import setup, find_packages

name = 'querycontacts'
description = "Query network abuse contacts on the command-line for a given ip address on abuse-contacts.abusix.zone"
cur_dir = os.path.abspath(os.path.dirname(__file__))

# Read Version
version_file = '%s/querycontacts/_version.py' % (cur_dir)
with open(version_file) as f:
    code = compile(f.read(), version_file, 'exec')
    exec(code)

with open(os.path.join(cur_dir, 'README.md')) as f:
    long_description = f.read()

with open('%s/requirements.txt' % cur_dir) as f:
    requires = f.readlines()

setup(
    name=name,
    version=__version__,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ['contact', 'query', 'dns', 'abuse contact', 'abuse', 'abusix', 'network'],
    author='abusix',
    author_email='fp@abusix.com',
    python_requires='>=3',
    url='https://github.com/abusix/querycontacts',
    install_requires=requires,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    scripts=['scripts/querycontacts'],
    license="GNU General Public License v3 (GPLv3)",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Customer Service',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security',
    ],
    project_urls={
        'Source': 'https://github.com/abusix/querycontacts',
        'Company': 'https://www.abusix.com/'
    },
)
