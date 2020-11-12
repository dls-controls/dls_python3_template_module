{{ cookiecutter.project_name }}
===========================

|build_status| |coverage| |pypi_version| |readthedocs| |license|

This is where you should write a short paragraph that describes what your module does,
how it does it, and why people should use it.

============== ==============================================================
PyPI           ``pip install {{ cookiecutter.project_name }}``
Source code    https://github.com/dls-controls/{{ cookiecutter.project_name }}
Documentation  http://{{ cookiecutter.project_name }}.readthedocs.io
============== ==============================================================

This is where you should put some images or code snippets that illustrate
some relevant examples. If it is a library then you might put some
introductory code here:

.. code:: python

    from {{ cookiecutter.project_name }} import HelloClass

    hello = HelloClass("me")
    print(hello.format_greeting())

Or if it is a commandline tool then you might put some example commands here::

    {{ cookiecutter.project_name }} person --times=2


.. |build_status| image:: https://travis-ci.com/dls-controls/{{ cookiecutter.project_name }}.svg?branch=master
    :target: https://travis-ci.com/dls-controls/{{ cookiecutter.project_name }}
    :alt: Build Status

.. |coverage| image:: https://coveralls.io/repos/github/dls-controls/{{ cookiecutter.project_name }}/badge.svg?branch=master
    :target: https://coveralls.io/github/dls-controls/{{ cookiecutter.project_name }}?branch=master
    :alt: Test Coverage

.. |pypi_version| image:: https://badge.fury.io/py/{{ cookiecutter.project_name }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.project_name }}
    :alt: Latest PyPI version

.. |readthedocs| image:: https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest
    :target: http://{{ cookiecutter.project_name }}.readthedocs.io
    :alt: Documentation

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License
