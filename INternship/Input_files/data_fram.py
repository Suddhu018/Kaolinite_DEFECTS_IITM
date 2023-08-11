from io import StringIO
import pandas as pd
def open_file_as_dataframe(filename, start_line, end_line ,df2):
    lines_to_read = range(start_line, end_line + 1)

    with open(filename, 'r') as file:
        lines = file.readlines()

        # Remove newline characters
        lines = [line.rstrip('\n') for line in lines]

        # Filter lines between start_line and end_line
        selected_lines = [line for line_number, line in enumerate(lines, start=1) if line_number in lines_to_read]
        j = 0
        while (j < len(selected_lines)):
            buffer = StringIO(selected_lines[j])
            content = buffer.getvalue()
            result1 = content.split()
            buffer = StringIO(selected_lines[j + 1])
            content = buffer.getvalue()
            result2 = content.split()
            new_data = pd.DataFrame({'Atom_Name': [result1[0]], 'Atom_Number': [result1[1]], 'x_coordinate': [result2[0]],
                                     'y_coordinate': [result2[1]], 'z_coordinate': [result2[2]]})
            df2 = df2.append(new_data, ignore_index=True)
            j = j + 2
    return df2