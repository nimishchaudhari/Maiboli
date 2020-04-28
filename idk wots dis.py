def star(x):
	for i in range(0,x):
		for j in range(0,i+1):
			print('*', end='')
		print('')
x = 5
print(star(x))
