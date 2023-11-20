from typing import Annotated

import typer
from rich import print
from rich.panel import Panel
from rich.padding import Padding

import keks


app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode='rich')


def version_callback(show: bool):
    if show:
        panel = Panel.fit(
            f'[bold][red]{keks.__title__}[/red] [dim]─[/dim] [blue]{keks.__version__}[/]',
            padding=(1, 4),
            border_style='dim'
        )
        wrap = Padding(panel, (1, 0))

        print(wrap)
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            '--version',
            help='Show keks version and exit.',
            is_eager=True,
            callback=version_callback
        )
    ] = False
):
    pass


if __name__ == '__main__':
    app()