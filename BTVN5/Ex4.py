list1 = ['ST','BĐ','BTL','CG','ĐĐ','HBT']
list2 = [150300, 247100, 333300, 266800, 420900,31800]
mx = 0
for i in list2:
	if i > mx:
		mx = i
	mn = i 
	for i in list2:
		if i < mn:
			mn = i

print('Quận đông dân nhất: ',list1[list2.index(mx)])
print('Quận ít dân nhất: ',list1[list2.index(mn)])


print(type(456)==int)