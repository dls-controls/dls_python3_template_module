from {{cookiecutter.project_name}} import cli, {{ cookiecutter.project_name }}


def test_hello_class_formats_greeting() -> None:
    inst = {{ cookiecutter.project_name }}.HelloClass("person")
    assert inst.format_greeting() == "Hello person"


def test_hello_lots_defaults(capsys) -> None:
    {{ cookiecutter.project_name }}.say_hello_lots()
    captured = capsys.readouterr()
    assert captured.out == "Hello me\n" * 5
    assert captured.err == ""


def test_cli(capsys) -> None:
    cli.main(["person", "--times=2"])
    captured = capsys.readouterr()
    assert captured.out == "Hello person\n" * 2
    assert captured.err == ""
