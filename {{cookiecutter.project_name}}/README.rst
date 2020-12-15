{{ cookiecutter.project_name }}
===========================

|build_status| |coverage| |pypi_version| |license|

This is where you should write a short paragraph that describes what your module does,
how it does it, and why people should use it.

============== ==============================================================
PyPI           ``pip install {{ cookiecutter.project_name }}``
Source code    https://github.com/dls-controls/{{ cookiecutter.project_name }}
Documentation  https://dls-controls.github.io/{{ cookiecutter.project_name }}
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


.. |build_status| image:: https://github.com/dls-controls/scanspec/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/dls-controls/scanspec/actions?query=workflow%3A%22Python+CI%22
    :alt: Build Status

.. |coverage| image:: https://dls-controls.github.io/scanspec/coverage.svg
    :target: https://github.com/dls-controls/scanspec/actions?query=workflow%3A%22Python+CI%22
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/scanspec.svg
    :target: https://pypi.org/project/scanspec
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst
