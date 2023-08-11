import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import file_read_fxn
import FILE_MANIPULATION
def call_read_function():#this is fuction to invoke the other function written in the other pyhton file
    if e1.get().strip() == "":
        output1="PLEASE ENTER THE FILE NAME"
        output_terminal.insert(tk.END, output1 + "\n","red")
        output_terminal.tag_configure("red", foreground="red")
        return
    if e2.get().strip() == "":
        output2 = "PLEASE ENTER THE Al:OH ratio"
        output_terminal.insert(tk.END, output2 + "\n","red")
        output_terminal.tag_configure("red", foreground="red")
        return
    arg1=str(e1.get())
    value=file_read_fxn.read_text_file(arg1)
    if(value==0):
        output2 = "FILE DOES NOT EXIST PLEASE ENTER A VALID FILE NAME"
        output_terminal.insert(tk.END, output2 + "\n","red")
        output_terminal.tag_configure("red", foreground="red")
        return
    elif(value==-1):
        output2 = "FILE IS NOT A CONFIG FILE PLEASE ENTER A VALID FILE NAME "
        output_terminal.insert(tk.END, output2 + "\n","red")
        output_terminal.tag_configure("red", foreground="red")
        return
    else:
        output2 = "FILE READ SUCCESSFULLY"
        output_terminal.insert(tk.END, output2 + "\n","green")
        output_terminal.tag_configure("green", foreground="green")
    arg2=int(e2.get())
    arg3=int(e3.get())
    arg4 = int(e4.get())
    arg5 = int(e5.get())

    val=FILE_MANIPULATION.calculate(arg1,arg2,arg3,arg4,arg5)# calling the function for actual calculations which is in another file
    if(val==1):
        output3 = "DEFECT CREATED SUCCESSFULLY"
        output_terminal.insert(tk.END, output3 + "\n", "green")
        output_terminal.tag_configure("green", foreground="green")
        output4 = "FILE OPENED SUCCESSFULLY AS DATAFRAME"
        output_terminal.insert(tk.END, output4 + "\n", "green")
        output_terminal.tag_configure("green", foreground="green")

    else:
        output3 = "DEFECT WAS NOT CREATED SUCCESSFULLY AND FAILED TO OPEN FILE AS DATAFRAME"
        output_terminal.insert(tk.END, output3 + "\n", "red")
        output_terminal.tag_configure("red", foreground="red")






root = tk.Tk()#tkinter program starts here

root.title("KAOLINITE")# this will show the title of the tab
window_width = 567 # this is to fix the window width when teh GUI is opened
window_height = 430# this is to fix the window height when teh GUI is opened
window_size = f"{window_width}x{window_height}"
root.geometry(window_size)
#here the actual code starts

#1 This is to get the data about the file which we want to read
heading=tk.Label(root, text="KAOLINITE CRYSTELLOGRAPHIC DATA",padx=7,pady=20)
heading.grid(row=0, column=1,columnspan=3)
file_name = tk.Label(root, text="File Name:")
file_name.grid(row=1, column=0)
global e1
e1 = tk.Entry(root, borderwidth=4)
e1.grid(row=1, column=1,columnspan=3)

#2 This is to get the data about the Al to OH ratio which we want to get
Al_OH_ratio = tk.Label(root, text="Al:OH ratio:")
Al_OH_ratio.grid(row=2, column=0)
global e2
e2 = tk.Entry(root, borderwidth=4)
e2.grid(row=2, column=1,pady=10,columnspan=3)

#this is to get the diagonal of the matrix to get the idea about the super cell
matrix_size = 3
matrix_data= tk.Label(root, text="DIagonal Matrix Data:")
matrix_data.grid(row=3, column=0)

global e3
e3 = tk.Entry(root,width=5)
e3.insert(0,"1")
global e4
e4 = tk.Entry(root,width=5)
e4.insert(0,"1")
global e5
e5= tk.Entry(root,width=5)
e5.insert(0,"1")

matrix = [
    [e3.grid(row=3, column=1), 0, 0],
    [0, e4.grid(row=4, column=2), 0],
    [0, 0, e5.grid(row=5, column=3)]
]

# Create labels or entry widgets to display the matrix
for i in range(3):
    for j in range(3):
        if(i==0 and j==0 or i==1 and j==1 or i==2 and j==2):
            continue
        element = matrix[i][j]
        label = tk.Label(root, text=element, width=5, relief=tk.SOLID)
        label.grid(row=i+3, column=1+j, padx=3, pady=5)
button1=tk.Button(root, text="Create Defect",command=call_read_function)
button1.grid(row=7,column=0,pady=10)

#funtion for reset butotn:
def reset_fields():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e3.insert(0, "1")
    e4.insert(0, "1")
    e5.insert(0, "1")
    output_terminal.delete('1.0', tk.END)

reset_button = tk.Button(root, text="Reset Input", command=reset_fields)
reset_button.grid(row=7,column=7,pady=10)

# code for terminal for outputs
output_terminal = scrolledtext.ScrolledText(root, height=10)
output_terminal.grid(row=8, column=0, columnspan=9, sticky=tk.NSEW)
#
root.mainloop()