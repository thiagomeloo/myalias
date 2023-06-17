import os

from myalias.core.interfaces.service_interface import ServiceInterface
from myalias.core.services.get_path_config_service import GetPathConfigService


class GetPathApplicationService(ServiceInterface):
    """Get path application."""

    def execute(self):
        """
        Get path application.
        """

        pathConfig = GetPathConfigService().execute()

        if not os.path.exists(pathConfig):
            return None

        for line in open(pathConfig):
            if line.startswith('pathApp='):
                pathApp = line.split('=')[1]
                pathApp = pathApp.strip()
                pathApp = os.path.expanduser(pathApp)
                return pathApp

        return None
