dls_python3_template_module
===========================



Getting started
---------------

This template can be used either via Cookiecutter_::

    cookiecutter https://gitlab.diamond.ac.uk/controls/templates/dls_python3_template_module

or via dls-start-new-module.py::

    dls-start-new-module.py -a python3 <module_name>

When you have your module you can create the pipenv::

    cd <module_name>
    pipenv install --dev

Now you are ready to start writing code

What to edit
------------

Your code lives in ``<module_name>``, and the tests in ``tests/test_<module_name>.py``

There is a ``main()`` function in ``<module_name>/cli.py`` that is exposed as a console
script. You can remove this fron ``setup.cfg`` if your module doesn't have a commandline interface.

Running the tests will tell you which bits of boilerplate need replacing::

    pipenv run tests

The test output will tell you what documentation needs updating::

    ___________________________________________________________________________________ test_changed_README ___________________________________________________________________________________
    Traceback (most recent call last):
    File "/path/to/my_module/tests/test_boilerplate_removed.py", line 45, in test_changed_README
        "Please change ./README.rst "
    AssertionError: Please change ./README.rst to include a paragraph on what your module does
    _________________________________________________________________________________ test_module_description _________________________________________________________________________________
    Traceback (most recent call last):
    File "/path/to/my_module/tests/test_boilerplate_removed.py", line 54, in test_module_description
        "Please change description in ./setup.cfg "
    AssertionError: Please change description in ./setup.cfg to be a one line description of your module
    _________________________________________________________________________________ test_docs_index_changed _________________________________________________________________________________
    Traceback (most recent call last):
    File "/path/to/my_module/tests/test_boilerplate_removed.py", line 63, in test_docs_index_changed
        "Please change the documentation in docs/index.rst "
    AssertionError: Please change the documentation in docs/index.rst to describe how to use your module
    ________________________________________________________________________________ test_docs_ref_api_changed ________________________________________________________________________________
    Traceback (most recent call last):
    File "/path/to/my_module/tests/test_boilerplate_removed.py", line 71, in test_docs_ref_api_changed
        "Please change the documentation in docs/reference/api.rst "
    AssertionError: Please change the documentation in docs/reference/api.rst to introduce the API for your module

When you have done this you can safely delete tests/test_boilerplate_removed.py

What's included
---------------

Some tools have been included and configured to make this module work out of the box. They are briefly described below.

pipenv_
~~~~~~~

This manages the dependencies to make a reproducable environment for the module to run in. The Pipfile is used to:

- Declare loosely defined module dependencies
- Declare loosely defined development time dependencies
- Declare custom commands as "scripts"

When a dependency is installed its actual pinned version is stored in the Pipfile.lock.

The scripts declared by this module are:

- ``pipenv run tests``: Run all the unit tests, linting, and static type analysis, with coverage
- ``pipenv run docs``: Build the docs using sphinx_

See https://confluence.diamond.ac.uk/display/CNTRLS/Python+3 for more details on the usage of pipenv.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _pipenv: https://pipenv.pypa.io/en/latest/
.. _sphinx: https://www.sphinx-doc.org/en/master/