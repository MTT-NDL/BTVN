a = [29,1,2003,9,1977,20,2,1975,17,10,23,3]
b = input('Enter a number: ')
if int(b) not in a :
	print("Not found in our list")
else:
	print('Found,','position',a.index(int(b)))