from setuptools import setup, find_packages


# Calculate the version based on pycard.VERSION
version = '.'.join([str(v) for v in __import__('pycard').VERSION])

setup(
    name='pycard',
    description='A simple library for payment card validation',
    version=version,
    author='Michael Angeletti - John Moscoso - Manuel Vega',
    author_email='manuel [dot] vega [at] manexware [dot] com',
    url='https://github.com/eudoro/pycard/',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 5',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
)
