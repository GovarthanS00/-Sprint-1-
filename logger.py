
import logging
import os


class LoggerManager:
    """Configure application logging."""

    def __init__(self, log_file: str = "logs/application.log"):
        self.log_file = log_file
        self._create_log_directory()

    def _create_log_directory(self) -> None:
        """Create log directory if it does not exist."""
        directory = os.path.dirname(self.log_file)

        if directory:
            os.makedirs(directory, exist_ok=True)

    def get_logger(self, name: str = "Application") -> logging.Logger:
        """Return configured logger."""
        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger