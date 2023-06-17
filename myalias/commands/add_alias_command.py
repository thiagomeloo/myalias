import os

from rich.console import Console
from rich.text import Text

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.services.get_path_application_service import (
    GetPathApplicationService,
)


class AddAliasCommand(CommandInterface):
    """Add alias command."""

    def execute(self, name, description, command):
        """
        Add alias command.

        Args:
            name (str): Name of command.
            description (str): Description of command.
            command (str): Command to execute.

        Returns:
            Config not found.
            Alias already exists.
            Alias created successfully.
        """

        console = Console()

        pathApp = GetPathApplicationService().execute()

        if not os.path.exists(pathApp):
            console.print(Text('Config not found', 'red'))
            return

        if name.find(' ') != -1:
            console.print(Text('Alias name can not have spaces', 'red'))
            return

        if name.find("'") != -1:
            console.print(Text("Alias name can not have '", 'red'))
            return

        if name.find('"') != -1:
            console.print(Text('Alias name can not have "', 'red'))
            return

        pathAlias = pathApp + '/aliases' + '/' + name

        # check file exists
        if os.path.exists(pathAlias):
            console.print(Text('Alias already exists', 'red'))
            return

        # sanitize command replace ' for \"
        command = command.replace("'", '\\"')

        alias = 'alias ' + name + "='" + command + "' # " + description + '\n'

        # create file
        with open(pathAlias, 'w') as f:
            f.write(alias)

        console.print(Text('Alias created successfully', 'green'))
