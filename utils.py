import os
import time
from datetime import datetime
from functools import wraps
from typing import Callable, Any


def validate_file_path(file_path: str) -> bool:
    """Validate whether a file exists."""
    if not file_path:
        raise ValueError("File path cannot be empty.")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    return True


def generate_timestamp() -> str:
    """Generate current timestamp."""
    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def execution_time(func: Callable) -> Callable:
    """Decorator to calculate function execution time."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(
            f"{func.__name__} execution time: "
            f"{end_time - start_time:.4f} seconds"
        )

        return result

    return wrapper


def path_validator(path: str) -> str:
    """Return absolute path."""
    return os.path.abspath(path)


class BaseFileHandler:
    """Base class for file handling."""

    def show_message(self):
        print("File handler")


class CSVFileHandler(BaseFileHandler):
    """CSV file handler."""

    def show_csv_message(self):
        print("Handling CSV file")