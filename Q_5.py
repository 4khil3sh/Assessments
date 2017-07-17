print('Enter list of numbers separated by a space: ')
a = [int(x) for x in raw_input().split()]
print(a)
for i in range(1,len(a)):
	if(i != a[i-1]):
		print(i)
		break
	else:
		i= i+1