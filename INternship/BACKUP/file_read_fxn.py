#function to check that the input file is present or not
import os

def read_text_file(file_path):
    #function to check that file exist or not
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return 0

    # Check that file has extension .CONFIG or not if not then return with an error text
    if not file_path.upper().endswith('.CONFIG'):
        print(f"Error: '{file_path}' is not a config file.")
        return -1


