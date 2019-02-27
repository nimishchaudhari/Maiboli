#Maiboli.py

#with open('sample.txt') as file:
#    file_contents = file.read()
#   print(file_contents)
eng=open('op.py','a')
file = open('Test.py','r')
for line in file:
	file_line = file.readline()
	print(line)
	#x+=1
	eng_line = file_line.replace('छापा','print')
	eng.write(eng_line+'1')
file.close()
eng.close()