import os
import shutil

from myalias.core.interfaces.service_interface import ServiceInterface


class CreateFoldersAppService(ServiceInterface):
    """Create folders app."""

    def execute(self, pathApp: str):
        """
        Create folders app.
        """

        pathApp = os.path.expanduser(pathApp)

        if os.path.exists(pathApp):
            shutil.rmtree(pathApp)
            os.mkdir(pathApp)
            os.mkdir(pathApp + '/aliases')
        else:
            os.mkdir(pathApp)
            os.mkdir(pathApp + '/aliases')
