#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-openfoam',
    version='0.2',
    description='Pygments lexer for C++ + OpenFOAM.',
    long_description=open('README.rst').read(),
    keywords='pygments c++ openfoam lexer',
    license='BSD',

    author='Kasper Linnestad',
    author_email='kasper1301@gmail.com',

    url='https://github.com/kasper1301/pygments-openfoam',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    openfoam=pygments_openfoam:OpenFOAMLexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
