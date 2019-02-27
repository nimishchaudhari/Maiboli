import os
eng=open('op.py','w')
file = open('Test.py','r')
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
	print('error')

os.remove('op.py')


