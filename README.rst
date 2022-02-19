========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-keychain/badge/?style=flat
    :target: https://python-keychain.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/thumdugger/python-keychain/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/thumdugger/python-keychain/actions

.. |version| image:: https://img.shields.io/pypi/v/keychain.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/keychain

.. |wheel| image:: https://img.shields.io/pypi/wheel/keychain.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/keychain

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/keychain.svg
    :alt: Supported versions
    :target: https://pypi.org/project/keychain

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/keychain.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/keychain

.. |commits-since| image:: https://img.shields.io/github/commits-since/thumdugger/python-keychain/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/thumdugger/python-keychain/compare/v0.0.0...master



.. end-badges

A package KeyChain enabled collections.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install keychain

You can also install the in-development version with::

    pip install https://github.com/thumdugger/python-keychain/archive/master.zip


Documentation
=============


https://python-keychain.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
