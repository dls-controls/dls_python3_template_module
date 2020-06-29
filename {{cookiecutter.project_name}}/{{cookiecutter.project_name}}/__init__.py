from {{ cookiecutter.project_name }}._version_git import __version__
from {{ cookiecutter.project_name }}.{{ cookiecutter.project_name }} import HelloClass, say_hello_lots

__all__ = ["__version__", "HelloClass", "say_hello_lots"]
