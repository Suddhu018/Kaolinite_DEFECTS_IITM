import pandas as pd
def do_manipulation(filename,d1,d2,d3,df):
    a=5.1535000801
    b=8.9418441280
    c=7.1331435844
    d1_x=d1
    d2_x=d2
    d3_x=d3
    a_number=34
    ##growing in x direction
    df2=df.copy()
    while d1 != 1:
        for index, row in df2.iterrows():
            x_c = float(row['x_coordinate'])
            x_c_new = str(format(x_c + (a*(d1_x-1)), '.9f'))
            new_row = pd.Series({'Atom_Name': row['Atom_Name'], 'Atom_Number': a_number+1,
                                 'x_coordinate': x_c_new, 'y_coordinate': row['y_coordinate'],
                                 'z_coordinate': row['z_coordinate']})
            df = df.append(new_row, ignore_index=True)
            a_number = a_number + 1
        d1 = d1 - 1
    ##growing in y direction
    df2 = df.copy()
    while d2 != 1:
        for index, row in df2.iterrows():
            y_c = float(row['y_coordinate'])
            y_c_new = str(format(y_c + (b*(d2_x-1)), '.9f'))
            new_row = pd.Series({'Atom_Name': row['Atom_Name'], 'Atom_Number': a_number+1,
                                 'x_coordinate': row['x_coordinate'], 'y_coordinate': y_c_new,
                                 'z_coordinate': row['z_coordinate']})
            df = df.append(new_row, ignore_index=True)
            a_number = a_number + 1
        d2 = d2 - 1

    ##growing in z direction
    df2 = df.copy()
    while d3 != 1:
        for index, row in df2.iterrows():
            z_c = float(row['z_coordinate'])
            z_c_new = str(format(z_c + (c*(d3_x-1)), '.9f'))
            new_row = pd.Series({'Atom_Name': row['Atom_Name'], 'Atom_Number': a_number+1,
                                 'x_coordinate': row['x_coordinate'], 'y_coordinate': row['y_coordinate'],
                                 'z_coordinate': z_c_new})
            df = df.append(new_row, ignore_index=True)
            a_number = a_number + 1
        d3 = d3 - 1

    ## now sorting the elements so that all the same type of elemet are toegther
    df=df.sort_values(by='Atom_Name')
    df = df.reset_index(drop=True)## this will make sure the rows are numbered sequentially
    ### now renaming the Atomic number
    df['Atom_Number'] = df.apply(lambda row: row.name + 1, axis=1)
    ## writing in the main file
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        file.writelines(lines[:5])
    a_new=a*d1_x
    b_new=b*d2_x
    c_new=c*d3_x
    matrix = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[2:]:  # Exclude the first two lines
            row = [float(num) for num in line.split()]
            matrix.append(row)
    matrix[0][0]=a_new
    matrix[1][1]=b_new
    matrix[2][2]=c_new
    print(matrix)
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        file.writelines(lines[:2])
    with open(filename, 'a') as file:
        for row in matrix:
            file.write('\t'.join('        '+str(num) for num in row))
            file.write('\n')
    with open(filename, 'a') as file:
        for index, row in df.iterrows():
            file.write(f'{row["Atom_Name"]}            {row["Atom_Number"]}\n')
            file.write('     'f'{row["x_coordinate"]}        {row["y_coordinate"]}        {row["z_coordinate"]}\n')
    print(df)
    return df






