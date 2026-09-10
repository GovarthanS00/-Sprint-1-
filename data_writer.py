import os
import json
import pickle
import pandas as pd


class DataWriter:

    def __init__(self, file_path):
        self.file_path = file_path


        directory = os.path.dirname(file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)



    def get_file_extension(self):
        extension = os.path.splitext(self.file_path)[1].lower()
        return extension


    def save_csv(self, data):

        if isinstance(data, pd.DataFrame):
            data.to_csv(self.file_path, index=False)

        else:
            df = pd.DataFrame(data)
            df.to_csv(self.file_path, index=False)

        print(f"CSV file saved successfully: {self.file_path}")


    def save_json(self, data):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"JSON file saved successfully: {self.file_path}")


    def save_pickle(self, data):

        with open(
            self.file_path,
            "wb"
        ) as file:

            pickle.dump(data, file)

        print(f"Pickle file saved successfully: {self.file_path}")


    def save_txt(self, data):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(str(data))

        print(f"TXT file saved successfully: {self.file_path}")


    def write(self, data):

        extension = self.get_file_extension()

        if extension == ".csv":
            self.save_csv(data)

        elif extension == ".json":
            self.save_json(data)

        elif extension in [".pkl", ".pickle"]:
            self.save_pickle(data)

        elif extension == ".txt":
            self.save_txt(data)

        else:
            raise ValueError(
                f"Unsupported file format: {extension}"
            )