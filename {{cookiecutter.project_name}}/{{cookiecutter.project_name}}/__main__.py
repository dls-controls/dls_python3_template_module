from {{ cookiecutter.project_name }} import cli

# test with:
#     pipenv run python -m {{ cookiecutter.project_name }}
if __name__ == "__main__":
    cli.main()
