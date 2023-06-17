from abc import ABC, abstractmethod


class CommandInterface(ABC):
    """Interface for commands to cli."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute command."""
        pass
