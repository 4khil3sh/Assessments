a = input('Enter a positive integer:')
b = a
while(a>1):
	if(a%2 == 0):
		a = a/2
	else:
		print (str(b) + ' is not a power of 2')
		break
if(a == 1):
	print (str(b) + ' is a power of 2')
