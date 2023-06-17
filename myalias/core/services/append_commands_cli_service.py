import typer

from myalias.core.interfaces.service_interface import ServiceInterface
from myalias.core.services.get_all_command_service import GetAllCommandsService


class AppendCommandsCliService(ServiceInterface):
    """Append commands to execute in CLI."""

    def execute(self, app: typer.Typer):
        """
        Append commands in CLI.

        Args:
            app (typer.Typer): Typer app.

        Returns:
            None
        """
        commands = GetAllCommandsService().execute()

        for command in commands:
            app.command(name=command['name'], help=command['description'])(
                command['instance']().execute
            ),
