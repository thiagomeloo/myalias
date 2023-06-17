import importlib
import os

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.interfaces.service_interface import ServiceInterface


class GetAllCommandsService(ServiceInterface):
    """Get all commands tool."""

    def execute(self):
        """
        Get all commands file in path myalias/commands.

        Returns:
            List of commands.

        """

        commands = []

        for root, dirs, files in os.walk('myalias/commands'):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    module_name = os.path.splitext(file_path)[0].replace(
                        '/', '.'
                    )
                    try:
                        module = importlib.import_module(module_name)
                        for attr_name in dir(module):
                            attr = getattr(module, attr_name)
                            if (
                                isinstance(attr, type)
                                and issubclass(attr, CommandInterface)
                                and attr != CommandInterface
                            ):
                                name = attr_name.replace('Command', '')
                                name = ''.join(
                                    x if x.islower() else '-' + x.lower()
                                    for x in name
                                ).lstrip('-')

                                description = attr.__doc__
                                objCommand = {
                                    'name': name,
                                    'description': description,
                                    'args': attr.execute.__code__.co_varnames,
                                    'instance': attr,
                                }
                                commands.append(objCommand)
                    except ImportError:
                        pass

        return commands
