import os

from rich.console import Console
from rich.prompt import Prompt

from myalias.core.interfaces.command_interface import CommandInterface
from myalias.core.services.create_folders_app_service import (
    CreateFoldersAppService,
)

console = Console()


class SetupCommand(CommandInterface):
    """Setup command."""

    def execute(self):
        """
        Setup initial to config myalias.
        """
        try:
            pathApp = Prompt.ask('Enter app path', default='~/.myalias')
            pathApp = os.path.expanduser(pathApp)

            if pathApp:
                console.print('Path app: ', pathApp, style='bold green')

            if os.path.exists(pathApp):
                console.print('Path app exists', style='bold yellow')
                overwrite = Prompt.ask(
                    'Do you want to replace? this action will delete everything currently existing.',
                    choices=['y', 'n'],
                    default='n',
                )
                if overwrite == 'y':
                    console.print('Overwrite', style='bold green')
                    CreateFoldersAppService().execute(pathApp)
                else:
                    console.print('Not overwrite', style='bold')
                    return
            else:
                console.print('Path app not exists', style='bold yellow')
                CreateFoldersAppService().execute(pathApp)

            if not os.path.exists(os.path.expanduser('~/.config/myalias')):
                os.mkdir(os.path.expanduser('~/.config/myalias'))

            with open(
                os.path.expanduser('~/.config/myalias/config'), 'w'
            ) as f:
                f.write('pathApp=' + pathApp)

            console.print('Select terminal to use', style='bold green')
            terminal = Prompt.ask(
                'Select terminal to use',
                choices=['bash', 'zsh'],
                default='bash',
            )

            shellPath = ''
            source = '\nsource ' + pathApp + '/aliases/*'
            match terminal:
                case 'bash':
                    console.print('bash selected', style='bold green')
                    shellPath = os.path.expanduser('~/.bashrc')
                case 'zsh':
                    console.print('zsh selected', style='bold green')
                    shellPath = os.path.expanduser('~/.zshrc')
                case _:
                    console.print('Not found terminal', style='bold red')

            strContent = 'if [ "$(ls -A ' + pathApp + '/aliases/)" ]; then'
            strContent += '\n\tfor file in ' + pathApp + '/aliases/*; do'
            strContent += '\n\t\t if [ -f "$file" ]; then'
            strContent += '\n\t\t\tsource "$file"'
            strContent += '\n\t\t fi'
            strContent += '\n\t done'
            strContent += '\nfi'

            if (
                os.path.exists(shellPath)
                and strContent not in open(shellPath).read()
            ):
                with open(shellPath, 'a') as f:
                    f.write('\n' + strContent)
                    console.print(
                        'source added in ' + shellPath, style='bold green'
                    )

            console.print('setup created', style='bold green')
        except KeyboardInterrupt:
            console.print('\nInterrupted', style='bold red')
