from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import datetime
from cookiecutter.utils import rmtree

from click.testing import CliRunner

import importlib
import pytest


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
        return subprocess.run(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def test_bake_and_run_tests(cookies):
    my_extra_context={'full_name': 'fakename',
                    'email': 'email@email.com',
                    'project_name': 'myproj',
                    'use_github': 'y'}
    with bake_in_temp_dir(cookies, extra_context=my_extra_context) as result:
        assert result.project.isdir()
        install = run_inside_dir('pipenv install --dev', str(result.project))
        assert install.returncode == 0
        test = run_inside_dir('pipenv run tests', str(result.project))
        assert test.returncode == 1
        out = test.stdout.decode()
        print(out)
        assert "4 failed" in out
        assert "Please change ./README.rst" in out
        assert "Please change description in ./setup.cfg" in out
        assert "Please change the documentation in docs/index.rst" in out
        assert "Please change the documentation in docs/reference/api.rst" in out
