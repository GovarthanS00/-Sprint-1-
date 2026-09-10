import os


class ConfigManager:
    """Manage application configuration."""

    def __init__(self):
        self.__config = {
            "PROJECT_1": os.getenv("PROJECT_1", "localhost"),
            "root": os.getenv("root", "root"),
            "Cyntheiya123#": os.getenv("Cyntheiya123#", ""),
            "sprint1_db": os.getenv(
                "sprint1_db",
                "sprint1_db"
            )
        }

    @classmethod
    def create_default(cls):
        """Create default configuration."""
        return cls()

    def get(self, key: str) -> str:
        """Get configuration value."""
        return self.__config.get(key, "")