li = input('Enter a list of numbers, separated by ‘ ‘: ')
llii = li.split(' ')
s = 0
for i in llii:
	s += int(i)
print('Sum of all entered numbers:',s)