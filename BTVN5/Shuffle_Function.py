def shuffle(a):

	if type(a) is str or type(a) is list:
		from random import randint
		list_a = list(a)
		ab = randint(0,len(list_a)-1)
		b = []
		b.append(ab)
		new_list = []
		new_list.append(list_a[ab])
		while 1:
			c = randint(0,len(list_a)-1)
			if c in b:
				continue
			else:
				b.append(c)
				new_list.append(list_a[c])
			if len(list_a) == len(new_list):
				break
		if type(a) == str:
			print(*new_list, sep = '')
		else:
			print(new_list)
	else:
		print('This function only works with string and list')