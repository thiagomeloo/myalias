from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.services.get_version_app_service import GetVersionAppService


class AboutCommand(CommandInterface):
    """About command."""

    def execute(self):
        """
        Display information about the application.

        Returns:
            Display information about the application.



        """

        console = Console()

        banner = Text()
        banner.append(
            '    __  ___         ___    ___             \n', 'bold yellow'
        )
        banner.append(
            '   /  |/  /_  __   /   |  / (_)___ _______ \n', 'bold yellow'
        )
        banner.append(
            '  / /|_/ / / / /  / /| | / / / __ \`/ ___/ \n', 'bold yellow'
        )
        banner.append(
            ' / /  / / /_/ /  / ___ |/ / / /_/ (__  )   \n', 'bold green'
        )
        banner.append(
            '/_/  /_/\__, /  /_/  |_/_/_/\__,_/____/    \n', 'bold green'
        )
        banner.append(
            '       /____/                              \n', 'bold green'
        )

        console.print(banner, justify='start')

        version = Text()
        version.append('Version: ', 'yellow')
        version.append(GetVersionAppService().execute(), 'green')
        version.append('\n')

        createBy = Text()
        createBy.append('Created by: ', 'yellow')
        createBy.append('Thiago Melo', 'green')
        createBy.append(' - ', 'bold')
        createBy.append('https://github.com/thiagomeloo')
        createBy.append('\n')

        starProject = Text()
        starProject.append('Star ✨ this project: ', 'yellow')
        starProject.append('https://github.com/thiagomeloo/myalias')
        starProject.append('\n')

        panelText = Text()
        panelText.append(version)
        panelText.append(createBy)
        panelText.append(starProject)

        panelInfo = Panel.fit(
            panelText,
            title='About - MyAlias',
            border_style='green',
            style='bold',
        )
        console.print(panelInfo)
