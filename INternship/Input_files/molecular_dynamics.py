import shutil
import os
import random

def perform_fxn(filename,d1,d2,d3,df):
    source_file_path = filename
    counter = 1
    destination_folder = filename[:-7]
    while True:
        ## sir you have to change this path
        destination_file_path = '/Users/sudhanshushekhar/Desktop/5th Sem/INternship/output_files/' + f"{destination_folder}copy_{counter}.data"
        if not os.path.exists(destination_file_path):
            shutil.copyfile(source_file_path, destination_file_path)
            name = destination_file_path
            break

        counter += 1
    columns = df.columns.tolist()
    columns = [columns[1]] + columns[:1] + columns[2:]
    df = df[columns]
    insert_index = 1
    df.insert(insert_index, "New Column", 1)
    df = df[[col for col in df.columns if col != 'Atom_Name'] + ['Atom_Name']]
    df['Atom_Name'] = '#' + df['Atom_Name'].astype(str)

    def map_atom_type(element):
        if element == '#Al':
            return 1
        elif element == '#Si':
            return 2
        elif element == '#O':
            return 3
        elif element == '#H':
            return 4
        else:
            return None

    # Insert the "Atom Type" column based on the 3rd column values
    df.insert(2, 'Atom Type', df['Atom_Name'].apply(map_atom_type))
    #to insert the charges of teh element
    def map_atom_type(element):
        if element == '#Al':
            return 3
        elif element == '#Si':
            return 4
        elif element == '#O':
            return -1
        elif element == '#H':
            return 1
        else:
            return None

    # Insert the "charge" column based on the 4th column values
    df.insert(3, 'Charge', df['Atom_Name'].apply(map_atom_type))

    # to add 3 coloum which all contain zero
    df.insert(len(df.columns) - 1, 'New1', 0)
    df.insert(len(df.columns) - 1, 'New2', 0)
    df.insert(len(df.columns) - 1, 'New3', 0)

    print(df)
    with open(destination_file_path, "r") as file:
        existing_content = file.read()

    with open(destination_file_path, "w") as file:
        file.write("    "+str(len(df))+" "+"atoms"+ "\n")
        file.write(existing_content)
    ## for the calculation of xlo,xhi etc
    a = 5.1535000801
    b = 8.9418441280
    c = 7.1331435844
    a_new=a*d1
    b_new=b*d2
    c_new=c*d3
    xlo=str(-1*a_new/2)
    xhi=str(a_new/2)
    ylo =str(-1 * b_new / 2)
    yhi = str(b_new / 2)
    zlo = str(-1 * c_new / 2)
    zhi = str(c_new / 2)


    mylist = ["     "+xlo+" "+xhi+"xlo xhi","       "+ylo+" "+yhi+"ylo yhi" ,"      "+zlo+" "+zhi+"zlo zhi"]

    # Specify the line numbers where you want to append the values
    line_numbers = [11, 12, 13]

    # Specify the path to the text file
    file_path = destination_file_path

    # Read the contents of the text file into a list of lines
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Insert the values of abc at the specified line numbers
    for i, line_number in enumerate(line_numbers):
        lines.insert(line_number - 1 + i, mylist[i] + "\n")

    # Write the updated list of lines back to the text file
    with open(file_path, "w") as file:
        file.writelines(lines)

    with open(destination_file_path, "a") as file:

        for index, row in df.iterrows():

            row_values = [str(value) for value in row.values]

            line = "\t".join(row_values)

            file.write(line + "\n")

