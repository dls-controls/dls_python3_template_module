{{ cookiecutter.project_name }}
===========================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

This is where you should write a short paragraph that describes what your module does,
how it does it, and why people should use it.

============== ==============================================================
PyPI           ``pip install {{ cookiecutter.project_name }}``
Source code    https://github.com/dls-controls/{{ cookiecutter.project_name }}
Documentation  https://dls-controls.github.io/{{ cookiecutter.project_name }}
Changelog      https://github.com/dls-controls/{{ cookiecutter.project_name }}/blob/master/CHANGELOG.rst
============== ==============================================================

This is where you should put some images or code snippets that illustrate
some relevant examples. If it is a library then you might put some
introductory code here:

.. code:: python

    from {{ cookiecutter.project_name }}.hello import HelloClass

    hello = HelloClass("me")
    print(hello.format_greeting())

Or if it is a commandline tool then you might put some example commands here::

    {{ cookiecutter.project_name }} person --times=2


.. |code_ci| image:: https://github.com/dls-controls/{{ cookiecutter.project_name }}/workflows/Code%20CI/badge.svg?branch=master
    :target: https://github.com/dls-controls/{{ cookiecutter.project_name }}/actions?query=workflow%3A%22Code+CI%22
    :alt: Code CI

.. |docs_ci| image:: https://github.com/dls-controls/{{ cookiecutter.project_name }}/workflows/Docs%20CI/badge.svg?branch=master
    :target: https://github.com/dls-controls/{{ cookiecutter.project_name }}/actions?query=workflow%3A%22Docs+CI%22
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/dls-controls/{{ cookiecutter.project_name }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dls-controls/{{ cookiecutter.project_name }}
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg
    :target: https://pypi.org/project/{{ cookiecutter.project_name }}
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://dls-controls.github.io/{{ cookiecutter.project_name }} for more detailed documentation.
