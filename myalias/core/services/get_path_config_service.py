import os

from myalias.core.interfaces.service_interface import ServiceInterface


class GetPathConfigService(ServiceInterface):
    """Get path config."""

    def execute(self):
        """
        Get path config.

        Returns:
            Path config.
        """

        pathConfig = os.path.expanduser('~/.config/myalias/config')

        return pathConfig
