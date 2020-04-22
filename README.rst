dls_python3_template_module
===========================

This module contains some opinionated defaults for a Python 3 module to be used
at Diamond

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

Your code lives in ``<module_name>``, and the tests in
``tests/test_<module_name>.py``

There is a ``main()`` function in ``<module_name>/cli.py`` that is exposed as a
console script. You can remove this fron ``setup.cfg`` if your module doesn't
have a commandline interface.

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

Some tools have been included and configured to make this module work out of the
box. They are briefly described below.

pipenv_
~~~~~~~

This manages the dependencies to make a reproducable environment for the module
to run in. The Pipfile is used to:

- Declare loosely defined module dependencies
- Declare loosely defined development time dependencies
- Declare custom commands as "scripts"

When a dependency is installed its actual pinned version is stored in the
Pipfile.lock.

The scripts declared by this module are:

- ``pipenv run tests``: Run all the unit tests, linting, and coverage
- ``pipenv run docs``: Build the docs using sphinx_

See https://confluence.diamond.ac.uk/display/CNTRLS/Python+3 for more details on
the usage of pipenv.

sphinx_
~~~~~~~

This tools parses rst files and creates HTML documentation for the module. It
can either be run from the commandline for local testing, or used with the
ReadTheDocs_ service for online hosted documentation

pytest_
~~~~~~~

This tool searches for files that look like tests (test in the filename, or in
the function). It then runs these tests, and any extra tests added by plugins.
The tools providing source code checking below are all added as plugins so that
when pytest is run, any source code failing the checks will be reported in the
results. Key features:

- Bare asserts​ for readable tests
- Test functions rather than classes​ reducing boilerplate
- Fixtures for supporting setUp and tearDown​
- Parameterized tests

flake8_
~~~~~~~

This tool warns about linting type errors​, improving the overall quality of
your code. For example it will warn about:

- Unused imports​
- Unused variables​
- Undefined names

black_
~~~~~~

This opinionated tool reformats code​ to a style guide. This reduces arguments
between developers as to how code should look, and aids code reviews as code
written by any developer will have the same style.

isort_
~~~~~~

This tool sorts imports into sections​. Like black_ it is also opinionated,
and has the same function of reducing arguments between developers. This
module includes some options that make it compatible with black.

mypy_
~~~~~

This tool is a type checker​ that statically analyses your code, warning about the wrong usage of types. It will only check code that is annotated with type hints, so can be
used in only some parts of the code. It is highly recommended for large projects as it helps developers answer the question "what exactly was I passed into this function" without
having to sacrifice Python's flexibility where needed.

versiongit_
~~~~~~~~~~~

This tool gets the version number of a module from a ``git describe​`` command. At release time it takes this version number and puts it in the released egg, wheel or sdist.
It takes the form of a single source file that is stored in the repo, which can be used at runtime or build time. It is inspired by versioneer_ but is much smaller in size and
complexity

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _pipenv: https://pipenv.pypa.io/en/latest/
.. _sphinx: https://www.sphinx-doc.org/en/master/
.. _ReadTheDocs: https://readthedocs.org/
.. _pytest: https://docs.pytest.org/en/latest/​
.. _flake8: https://flake8.pycqa.org/en/latest/​
.. _black: https://black.readthedocs.io/en/stable/​
.. _isort: https://isort.readthedocs.io/en/latest/​
.. _mypy: http://mypy-lang.org/​
.. _versiongit: https://versiongit.readthedocs.io/en/latest/​
.. _versioneer: https://github.com/warner/python-versioneer
