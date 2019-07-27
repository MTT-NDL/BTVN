a = ['green','blue','red','yellow']
print('Our colour list: ')
for i in range(len(a)):
	print(i+1, a[i], sep = '. ')
b = input('Item to delete: ')
if b.isnumeric():
	a.pop(int(b)-1)
	for i in range(len(a)):
		print(i+1, a[i], sep = '. ')
if b.isalpha():
	a.remove(b)
	for i in range(len(a)):
		print(i+1, a[i], sep = '. ')
