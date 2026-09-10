import os
import json
import pandas as pd


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path


    def validate_path(self):
        if not self.file_path:
            raise ValueError("File path cannot be empty.")

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        if not os.path.isfile(self.file_path):
            raise ValueError(
                f"The given path is not a file: {self.file_path}"
            )

        return True




    def get_file_extension(self):
        extension = os.path.splitext(self.file_path)[1].lower()
        return extension
    

    def read_csv(self):
        return pd.read_csv(self.file_path)


    def read_json(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)



    def read_txt(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()



    def load(self):

        # Validate the path first
        self.validate_path()

        # Get extension
        extension = self.get_file_extension()

        # Read based on file type
        if extension == ".csv":
            return self.read_csv()

        elif extension == ".json":
            return self.read_json()

        elif extension == ".txt":
            return self.read_txt()

        else:
            raise ValueError(
                f"Unsupported file format: {extension}"
            )
