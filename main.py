from data_loader import DataLoader
from data_writer import DataWriter
from logger import LoggerManager


def main():
    """Run the Sprint 1 application."""

    logger_manager = LoggerManager()
    logger = logger_manager.get_logger()

    logger.info("Application started")

    print("===== Python Data Processing Utility =====")

    file_path = input(
        "Enter file path (CSV/JSON/TXT): "
    )

    try:
        loader = DataLoader(file_path)

        data = loader.load()

        print("\nFile loaded successfully!")
        print(data)

        logger.info(
            f"Successfully loaded file: {file_path}"
        )

        print("\nChoose output format:")
        print("1. CSV")
        print("2. JSON")
        print("3. Pickle")
        print("4. TXT")

        choice = input("Enter your choice: ")
        if choice == "1":
            writer = DataWriter("outputs/result.csv")
            writer.write(data)
        elif choice == "2":
            writer = DataWriter("outputs/result.json")
            writer.write(data)
        elif choice == "3":
            writer = DataWriter("outputs/result.pkl")
            writer.write(data)
        elif choice == "4":
            writer = DataWriter("outputs/result.txt")
            writer.write(data)
        else:
            print("Invalid choice.")

    except Exception as error:
        logger.error(f"Application error: {error}")
        print(f"Error: {error}")

    finally:
        logger.info("Application execution completed")
        print("\nProgram completed.")


if __name__ == "__main__":
    main()