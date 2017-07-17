print('Enter list of numbers separated by a space: ')
a = [int(x) for x in raw_input().split()]
for i in range(1,len(a)):
	if(i > 1):
		if(a[i] != a[i-1] + a[i-2]):
			print('It is not a additive sequence')
			break
		else:
			i= i+1
	else:
		i = i+1
if(i == len(a)):
	print('You entered a additive sequence')