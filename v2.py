#Version 2 - using a dictionary list python file to replace the phrases

import os,sys,json
import dix
#import tkinter as tk


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
#file = open('Test.py','r')

total_dictionary_items = len(dix.en)
#Read the input file
arr = file.readlines() # Grabbing the IP file's lines and putting them all together as an array item per line
i = len(arr)

for y in arr:
        for x in dix.en:
                count = dix.en.index(x)
                y = y.replace(dix.mar[count],dix.en[count])
        eng.write(y)
"""
for y in arr:
    for x in dix.en:
        count = dix.en.index(x)
#Here, I'm supposed to add a logic to exclude the ddictionary translation of open and close of quote marks,
#This is to avoid bloody replacing of words from inside statements.
        y = y.replace(dix.mar[count],dix.en[count])        

"""
file.close()
eng.close()
def final_run():
        eng = open('op.py','r')
        ip = eng.read()
        exec(ip)
        #os.remove('op.py')
final_run()