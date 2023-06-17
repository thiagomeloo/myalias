from myalias import __version__
from myalias.core.interfaces.service_interface import ServiceInterface


class GetVersionAppService(ServiceInterface):
    """Get version app."""

    def execute(self):
        """
        Get version of project in pyproject.toml.

        Returns:
            str: Version of project.
        """

        return __version__
