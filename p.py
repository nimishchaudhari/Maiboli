import os
import sys

arg1 = sys.argv[1]
arg1 = str(arg1)
eng=open('op.py','w')

try:
	file = open(arg1,'r')
except FileNotFoundError:
	print("Program input file error")
else:
	print("File input successful")
arr = file.readlines()
i = len(arr)
for x in arr:
	x = x.replace('छापा','print')
	x = x.replace('तोपर्यंत','for')
	x = x.replace('जर','if')
	x = x.replace('किंवा','elif')
	x = x.replace('नाहीतर','else')
	x = x.replace('परत','return')
	x = x.replace('माहिती','input')
	#x = x.replace('','')
	#x = x.replace('','')
	#x = x.replace('','')
	eng.write(x)
file.close()
eng.close()
eng = open('op.py','r')
ip = eng.read()
try:
	exec(ip)
except SyntaxError:
	print(' काही तरही टायपिंग चूक आहे ')
else:
	print('प्रोग्रॅम यशस्वीरित्या पूर्ण झाला')

os.remove('op.py')


