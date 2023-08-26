import os

from rich.console import Console
from rich.table import Table
from rich.text import Text

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.services.get_path_application_service import (
    GetPathApplicationService,
)


class ListAliasCommand(CommandInterface):
    """List alias command."""

    def execute(self):
        """List alias command."""

        console = Console()

        pathApp = GetPathApplicationService().execute()

        if not os.path.exists(pathApp):
            console.print(Text('Config not found', 'red'))
            return

        pathAlias = pathApp + '/aliases'

        # check file exists
        if not os.path.exists(pathAlias):
            console.print(Text('Alias not exists', 'red'))
            return

        table = Table(show_header=True, header_style='bold magenta')

        table.add_column('Name')
        table.add_column('Description')
        table.add_column('Command')

        # get files in folder and sub folder
        for root, dirs, files in os.walk(pathAlias):
            for file in files:
                with open(os.path.join(root, file), 'r') as f:
                    line = f.readline()

                    # alias test='echo test' # test
                    strAlias = line[6:]
                    aliasName = strAlias.split('=')[0]
                    aliasCommand = (
                        strAlias.split('=')[1]
                        .split('#')[0]
                        .strip()[1:-1]
                        .replace('\\"', '"')
                    )
                    aliasComment = strAlias.split('#')[1].strip()

                    table.add_row(aliasName, aliasComment, aliasCommand)

        console.print(table)
