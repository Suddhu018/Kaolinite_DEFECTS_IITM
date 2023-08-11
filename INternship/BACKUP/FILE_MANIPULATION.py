import shutil
import os
import random
import subprocess
import sys
import pandas as pd
import opean_vesta
global name
def calculate(arg1,al_OH_ratio,d1,d2,d3):
    source_file_path = arg1
    counter = 1
    destination_folder= arg1[:-7]
    while True:
        destination_file_path ='/Users/sudhanshushekhar/Desktop/5th Sem/INternship/output_files/'+f"{destination_folder}copy_{counter}.CONFIG"
        if not os.path.exists(destination_file_path):
            shutil.copyfile(source_file_path, destination_file_path)
            name = destination_file_path
            break

        counter += 1
    val=delete_random_line(name, 58, 73)
    if(val==1):
        return 1
    else:
        return 0


def delete_random_line(filename, start_line, end_line):# function to delete the randomly delete line
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Check if the given lines are within the range of the file
    if start_line < 1 or end_line > len(lines):
        print("Invalid line range.")
        return

    # Select a random line between the given range
    selected_lines = list(range(start_line, end_line + 1, 2))
    random.shuffle(selected_lines)

    # Delete the randomly selected line
    deleted_lines = set()

    for line_number in selected_lines:
        if line_number + 1 in deleted_lines:
            continue

        del lines[line_number - 1:line_number + 1]
        deleted_lines.add(line_number)
        deleted_lines.add(line_number + 1)
        break
    # Write the modified contents back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)

    print("Selected lines deleted successfully.")

    # fucntions to open this config file in diffrent default text editor
    def open_file_in_window(file_path):
        try:
            df = pd.read_csv(filename)
            print(df)
            if sys.platform.startswith('win'):  # Windows
                os.startfile(filename)
            elif sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', filename])
            elif sys.platform.startswith('linux'):  # Linux
                subprocess.run(['xdg-open', filename])
            else:
                print("Unsupported operating system.")
                return 0

            print("File opened in default text editor.")
            return 1

        except FileNotFoundError:
            print("File not found.")
            return 0

    ret=open_file_in_window(filename)
    if(ret==1):
        opean_vesta.open_with_vesta(filename)  # function to open this defect file in vesta
        return 1
    else:
        return 0

