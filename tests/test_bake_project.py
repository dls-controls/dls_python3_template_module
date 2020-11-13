from contextlib import contextmanager
import shlex
import os
import subprocess
from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies

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
def bake_in_temp_dir(cookies: Cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies:
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        if result.project:
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
    my_extra_context={
        'full_name': 'fakename',
        'email': 'email@email.com',
        'project_name': 'myproj'
    }
    with bake_in_temp_dir(cookies, extra_context=my_extra_context) as result:
        assert not result.exception
        assert result.project.isdir()
        install = run_inside_dir('pipenv install --dev', str(result.project))
        assert install.returncode == 0
        test = run_inside_dir('pipenv run tests', str(result.project))
        assert test.returncode == 1
        out = test.stdout.decode()
        print(out)
        assert "5 failed" in out
        assert "Please change ./README.rst" in out
        assert "Please change description in ./setup.cfg" in out
        assert "Please change ./docs/reference/api.rst" in out
        assert "Please delete ./docs/how-to/accomplish-a-task.rst" in out
        assert "Please delete ./docs/explanations/why-is-something-so.rst" in out
