import typer
from rich.console import Console

from myalias.commands.add_alias_command import AddAliasCommand
from myalias.commands.list_alias_command import ListAliasCommand
from myalias.commands.remove_alias_command import RemoveAliasCommand
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


@app.command(name='add-alias', rich_help_panel='Commands')
def add_alias(name, description, command):
    """
    Add alias to the application.
    Args:
        name (str): Name of command.
        description (str): Description of command.
        command (str): Command to execute.

    """
    AddAliasCommand().execute(name, description, command)


@app.command(name='remove-alias', rich_help_panel='Commands')
def remove_alias(name):
    """
    Remove alias to the application.
    Args:
        name (str): Name of command.
    """
    RemoveAliasCommand().execute(name)


@app.command(name='list-alias', rich_help_panel='Commands')
def list_alias():
    """List alias to the application."""
    ListAliasCommand().execute()


if __name__ == '__main__':
    app()
