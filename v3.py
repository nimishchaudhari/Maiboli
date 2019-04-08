#Version 3 - Dictionary works, now trying to grab the output from console
#and sending it to a variable.

import os,sys,json
import dix
from io import StringIO  # Python3
#import tkinter as tk

old_stdout = sys.stdout
"""
# This variable will store everything that is sent to the standard output
 
result = StringIO()
 
sys.stdout = result
 
#do bakchodi here
# Run the commands you want to get your output here to

#get the output back
# Redirect again the std output to screen
 
sys.stdout = old_stdout
 
# Then, get the stdout like a string and process it!
 
result_string = result.getvalue()
#result_string has the output you need
print(result_string)
"""

# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

#input filename in command line
arg1 = sys.argv[1]
arg1 = str(arg1)

#open a new file and allow write access
eng=open('op.py','w')

#open the input file as read
file = open(arg1,'r')

total_dictionary_items = len(dix.en)
#Read the input file
arr = file.readlines()
i = len(arr)

for y in arr:
        for x in dix.en:
                count = dix.en.index(x)
                y = y.replace(dix.mar[count],dix.en[count])
        eng.write(y)

file.close()
eng.close()
def final_run():
        eng = open('op.py','r')
        ip = eng.read()
        exec(ip)
        os.remove('op.py')


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