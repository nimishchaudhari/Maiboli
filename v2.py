#Version 2 - using a dictionary json file to replace the phrases

import os,sys,json
import dix

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
        #yield(x)
        
    eng.write(y)
file.close()
eng.close()
eng = open('op.py','r')
ip = eng.read()
exec(ip)
os.remove('op.py')