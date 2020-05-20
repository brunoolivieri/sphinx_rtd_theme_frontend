# -*- coding: utf-8 -*-
"""`sphinx_rtd_theme` lives on `Github`_.

.. _github: https://www.github.com/brunoolivieri/sphinx_rtd_theme_frontend

"""
from setuptools import setup
from sphinx_rtd_theme_frontend import __version__


setup(
    name='sphinx_rtd_theme_frontend',
    version=__version__,
    url='https://github.com/brunoolivieri/sphinx_rtd_theme_frontend/',
    license='MIT',
    author='Dave Snider',
    author_email='dave.snider@gmail.com',
    description='ReadTheDocs.org theme for Sphinx, updated from DaveSnider version to have a site toolbar version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_rtd_theme_frontend'],
    package_data={'sphinx_rtd_theme_frontend': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
