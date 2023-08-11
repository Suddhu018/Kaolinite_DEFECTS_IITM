import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt, copy
from io import StringIO

df2 = pd.DataFrame(columns=['atom', 'Sr_number','x_coordinate','y_coordinate','z_coordinate'])

def read_file_between_lines(filename, start_line, end_line):
    lines_to_read = range(start_line, end_line + 1)

    with open(filename, 'r') as file:
        lines = file.readlines()

        # Remove newline characters
        lines = [line.rstrip('\n') for line in lines]

        # Filter lines between start_line and end_line
        selected_lines = [line for line_number, line in enumerate(lines, start=1) if line_number in lines_to_read]

        return selected_lines
selected_lines=read_file_between_lines('try.CONFIG',6,73)
j=0
while(j<len(selected_lines)):
    buffer = StringIO(selected_lines[j])
    content = buffer.getvalue()
    result1 = content.split()
    buffer = StringIO(selected_lines[j+1])
    content = buffer.getvalue()
    result2 = content.split()
    new_data = pd.DataFrame({'atom': [result1[0]], 'Sr_number': [result1[1]],'x_coordinate':[result2[0]],'y_coordinate':[result2[1]],'z_coordinate':[result2[2]]})
    df2= df2.append(new_data, ignore_index=True)
    j=j+2
print(df2)