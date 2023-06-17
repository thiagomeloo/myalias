import os

from rich.console import Console
from rich.text import Text

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.services.get_path_application_service import (
    GetPathApplicationService,
)


class RemoveAliasCommand(CommandInterface):
    """Remove alias command."""

    def execute(self, name):
        """
        Remove alias command.
        """
        console = Console()

        pathApp = GetPathApplicationService().execute()

        if not os.path.exists(pathApp):
            console.print(Text('Config not found', 'red'))
            return

        pathAlias = pathApp + '/aliases' + '/' + name

        # check file exists
        if not os.path.exists(pathAlias):
            console.print(Text('Alias not exists', 'red'))
            return

        os.remove(pathAlias)
        console.print(Text('Alias removed successfully', 'green'))
