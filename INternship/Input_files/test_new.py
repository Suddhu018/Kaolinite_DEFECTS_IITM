def read_even_lines(filename, start_line, end_line):
    with open(filename, 'r') as file:
        lines = file.readlines()

        # Adjust start and end line indices to consider even numbers
        start_line = start_line if start_line % 2 == 0 else start_line + 1
        end_line = end_line if end_line % 2 == 0 else end_line - 1

        # Ensure start_line is within the file's range
        start_line = max(2, start_line)

        # Read even-numbered lines within the specified range
        even_lines = lines[start_line - 1: end_line: 2]

        return even_lines

x=read_even_lines('try.CONFIG',6,73)
print(x)
print(type(x))
i=0
while(i<len(x)):
    print(x[i])
    i=i+1

text = "Apple,Orange,Mango,Banana"
result = text.split(',')
print(result[0])












