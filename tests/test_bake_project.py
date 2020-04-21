from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import datetime
from cookiecutter.utils import rmtree

from click.testing import CliRunner

import importlib


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_bake_and_run_tests(cookies):
    my_extra_context={'full_name': 'fakename',
                    'email': 'email@email.com',
                    'project_name': 'myproj',
                    'project_short_description': 'It does this.',
                    'use_github': 'y'}
    with bake_in_temp_dir(cookies, extra_context=my_extra_context) as result:
        assert result.project.isdir()
        assert run_inside_dir('pipenv run tests', str(result.project)) == 0, \
            "Generated module tests failed, did you remember to remove all of the boilerplate?"
        print("test_bake_and_run_tests path", str(result.project))
