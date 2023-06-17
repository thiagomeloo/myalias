import typer
from rich.console import Console

from myalias.core.commands.about_command import AboutCommand
from myalias.core.commands.setup_command import SetupCommand
from myalias.core.services.append_commands_cli_service import (
    AppendCommandsCliService,
)
from myalias.core.services.update_version_app_service import (
    UpdateVersionAppService,
)

console = Console()

app = typer.Typer(
    name='MyApp',
    add_completion=False,
)


def versionCallback(showVersion: bool):
    """Display information version the application."""
    if showVersion:
        AboutCommand().execute()
        raise typer.Exit()


version = typer.Option(
    None,
    '--version',
    '-v',
    callback=versionCallback,
    is_eager=True,
    help='Show the version and exit.',
)


@app.callback()
def main(version: bool = version):
    pass


@app.command(rich_help_panel='Help and Others')
def about():
    """Display information about the application."""
    AboutCommand().execute()


@app.command(name='setup', rich_help_panel='Help and Others')
def setup():
    """Setup initial to configure application."""
    SetupCommand().execute()


@app.command(name='updateVersion', hidden=True)
def updateVersion():
    """Update version app."""
    UpdateVersionAppService().execute()


AppendCommandsCliService().execute(app)

if __name__ == '__main__':
    app()
