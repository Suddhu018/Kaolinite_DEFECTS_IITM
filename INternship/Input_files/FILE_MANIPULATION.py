import shutil
import os
import random
import subprocess
import sys
import molecular_dynamics
import math
import pandas as pd
import opean_vesta
global name
import data_fram
import matrix_manipulation
def calculate(arg1,al_OH_ratio,d1,d2,d3):
    source_file_path = arg1
    counter = 1
    destination_folder=arg1[:-7]
    while True:
        ## sir you have to change this path
        destination_file_path ='/Users/sudhanshushekhar/Desktop/5th Sem/INternship/output_files/'+f"{destination_folder}copy_{counter}.CONFIG"
        if not os.path.exists(destination_file_path):
            shutil.copyfile(source_file_path, destination_file_path)
            name = destination_file_path
            break

        counter += 1
    val=delete_random_line(name,d1,d2,d3)
    if(val==1):
        return 1
    else:
        return 0


def delete_random_line(filename,d1,d2,d3):# function to delete the randomly delete line
    # fucntions to open this config file as a dataframe
    def open_file_in_dataframe(file_path):
        df2 = pd.DataFrame(columns=['Atom_Name', 'Atom_Number', 'x_coordinate', 'y_coordinate', 'z_coordinate'])
        df = data_fram.open_file_as_dataframe(file_path,6,73,df2)
        new_df = df[df['Atom_Name'].isin(['O', 'H'])]
        start_row_oxygen=8
        endrow_oxygen=25
        start_row_H = 26
        endrow_H = 33
        my_list=[]
        for index, row in new_df.iterrows():
            if start_row_oxygen <= index <= endrow_oxygen:
                x_c_o = float(row['x_coordinate'])
                y_c_o= float(row['y_coordinate'])
                z_c_o = float(row['z_coordinate'])
                row_o=index
                for index, row in new_df.iterrows():
                    if start_row_H <= index <= endrow_H:
                        x_c_h = float(row['x_coordinate'])
                        y_c_h = float(row['y_coordinate'])
                        z_c_h = float(row['z_coordinate'])
                        row_h=index
                        distance = math.sqrt((x_c_o - x_c_h) ** 2 + (y_c_o - y_c_h) ** 2 + (z_c_o - z_c_h) ** 2)
                        if(distance<1):
                            my_pair=(row_o,row_h)
                            my_list.append(my_pair)
        random_tuple = random.choice(my_list)
        index1_O_deleted=random_tuple[0]
        index2_H_deleted=random_tuple[1]
        df = df.drop(index1_O_deleted)
        df = df.drop(index2_H_deleted)
        ## NOW HERE THE CHARGE IS UNBLANCED NOW WRITE THE THE RANDOM FUNCTION TO DELETE ANY HYDROGEN
        ##SO THAT CHARGE CAN BE BALANCED
        random_row = df[df['Atom_Name'] == 'H'].sample()
        index_to_delete = random_row.index
        df = df.drop(index_to_delete)
        print(df)
        ## now wrtitng (changig)/updating  the main file
        lines_to_delete_from_file=[6+(random_tuple[0])*2, 7+(random_tuple[0])*2, 6+(random_tuple[1])*2, 7+(random_tuple[1])*2, 6+(index_to_delete)*2,7+(index_to_delete)*2]
        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = [line for index, line in enumerate(lines, start=1) if index not in lines_to_delete_from_file]

        # Rewrite the remaining lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        modified_final_df=matrix_manipulation.do_manipulation(filename,d1,d2,d3,df)
        molecular_dynamics.perform_fxn("lammps.data", d1, d2, d3, modified_final_df)
        return 1

    ret=open_file_in_dataframe(filename)
    if(ret==1):
        opean_vesta.open_with_vesta(filename)  # function to open this defect file in vesta
        return 1
    else:
        return 0

