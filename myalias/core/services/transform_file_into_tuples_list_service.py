import os
import re

from myalias.core.interfaces.service_interface import ServiceInterface


class TransformFileIntoTuplesListService(ServiceInterface):
    """Transform a file into a list fo tuples."""

    def execute(self, file_path: str):
        """
        Transform a file into a list fo tuples.

        Args:
            file_path (str): Typer app.

        Returns:
            list: List of tuples.
        """

        tuples_list = []

        if not os.path.exists(file_path):
            return tuples_list

        with open(file_path, 'r') as file:
            for line in file:
                values = re.findall(r'"(.*?)"', line)

                if len(values) != 3:
                    continue

                alias, description, command = values

                command = command.replace("'", '"')

                tuples_list.append((alias, description, command))

        return tuples_list
