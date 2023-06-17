from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    """Interface for services."""

    @staticmethod
    @abstractmethod
    def execute(self):
        """Execute services."""
        pass
