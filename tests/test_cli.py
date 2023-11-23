from click.utils import strip_ansi
from typer.testing import CliRunner

import keks
from keks.__main__ import app


runner = CliRunner()

def run(*args):
    return runner.invoke(app, args)


def test_help():
    result = run('--help')
    stdout = strip_ansi(result.stdout)

    assert not result.exit_code
    assert 'Usage:' in stdout
    assert '--help' in stdout
    assert 'Show this message and exit.' in stdout


def test_version():
    result = run('--version')

    assert not result.exit_code
    assert keks.__version__ in result.stdout