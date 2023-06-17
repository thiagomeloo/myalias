import os

import toml

from myalias.core.interfaces.service_interface import ServiceInterface


class UpdateVersionAppService(ServiceInterface):
    def execute(self):
        with open('pyproject.toml', 'r') as file:
            content = file.read()
            data = toml.loads(content)
            version = data['tool']['poetry']['version']

            with open('myalias/__init__.py', 'w') as f:
                f.write(f"__version__ = '{version}'\n")
