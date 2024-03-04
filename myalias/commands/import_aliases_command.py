from rich.console import Console
from rich.text import Text

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.interfaces.service_interface import ServiceInterface
from myalias.core.services.transform_file_into_tuples_list_service import (
    TransformFileIntoTuplesListService,
)


class ImportAliasesCommand(CommandInterface):
    """Import alias command."""

    __add_alias_command: CommandInterface
    __transform_file_into_tuples_list_service: ServiceInterface

    def __init__(self, add_alias_command: CommandInterface):
        self.__add_alias_command = add_alias_command
        self.__transform_file_into_tuples_list_service = (
            TransformFileIntoTuplesListService()
        )

    def execute(self, file_path):
        """
        Import a list of aliases command.

        Args:
            file_path (str): Path to aliases list file.

        Returns:
            Config not found.
            Aliases imported successfully.
        """

        console = Console()

        list_alias = self.__transform_file_into_tuples_list_service.execute(
            file_path
        )

        if not list_alias:
            console.print(Text('Config not found', 'red'))
            return

        for alias in list_alias:
            name = alias[0]
            console.print(Text(f'Adding alias {name}', 'yellow'))
            self.__add_alias_command.execute(alias[0], alias[1], alias[2])
            console.print(Text('\n'))

        return
