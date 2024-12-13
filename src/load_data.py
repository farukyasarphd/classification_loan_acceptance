import os
import pandas as pd

def load_excel(data_path, file, sheet_name):
    file_path = os.path.join(data_path, file)
    try:
        data = pd.read_excel(file_path, sheet_name)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
