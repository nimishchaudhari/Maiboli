#In this version, I'm trying to fit a TKinter based gui
#Input in TKinter window and Output in the same

import os,sys,json
import dix
from io import StringIO  # Python3
import tkinter as tk
global marathi_input
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    marathi_input = inputValue
    print(inputValue)

def final_run():
        eng = open('op.py','r')
        ip = eng.read()
        exec(ip)
        os.remove('op.py')

old_stdout = sys.stdout

#input filename in command line
#arg1 = sys.argv[1]
#arg1 = str(arg1)

#open a new file and allow write access
eng=open('op.py','w')


total_dictionary_items = len(dix.en)
#Read the input file

""" TKinter Input text area """

#Tkinter main window (container)
master = tk.Tk()
master.title('मायबोली')


#trying button

textBox=tk.Text(master, height=2, width=10)
textBox.pack()
buttonExec=tk.Button(master, height=1, width=10, text="चालवा",command=lambda: retrieve_input)
    #command=lambda: retrieve_input() >>> just means do this when i press the button
buttonExec.pack()
tk.mainloop()

#Add tkinter widgets here
run_button = tk.Button(master,text='Print', command=master.destroy)
run_button.pack()


inputtext  =Text(master, option=value)


master.mainloop()

tk.Label(master, text="Input your marathi text").grid(row=2)
e1 = tk.Entry(master)
e1.grid(row=2, column=2)

entry.bind("<Return>", evaluate)


arr = ['x']             #= file.readlines()
i = len(arr)

for y in arr:
        for x in dix.en:
                count = dix.en.index(x)
                y = y.replace(dix.mar[count],dix.en[count])
        eng.write(y)


eng.close()
result = StringIO()
 
sys.stdout = result
#Do stuff here
final_run()
#End of stuff
 
sys.stdout = old_stdout
 
# Then, get the stdout like a string and process it!
 
result_string = result.getvalue()
#result_string has the output you need
print(result_string)

tk.mainloop()