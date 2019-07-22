PoN = input('Enter \'play\' to start the game: ')
if PoN.lower() == 'play':

	print('NHAP O CHO PHEP TINH DUNG VA X CHO PHEP TINH SAI')
	point = 0

	while 1:
		print('Point = ', point)
    
		from random import randint
		tf = randint(0,1) # 0 == False, 1 == True
		pt = randint(0,1) # 0 == +, 1 == -
		a = randint(0,100)
		b = randint(0,100)
		c = randint(-100,100)

		if tf == 0:
			if pt == 0:
				print(a, '+', b, '=',c )
				i = input('O or X: ')
				if a + b == c:
					if i == 'O' or i == 'o':
						point += 1
					elif i == 'X' or 'x':
						print('Game over')
						point = 0
						ii = input('Enter \'play\' to start the game: ')
						if ii.lower() == 'play':
							continue
						else:
							break
					else: 
						print('Cau tra loi khong hop le')
						continue
				else:
					if i == 'X' or i == 'x':
						point += 1
					elif i == 'O' or 'o':
						print('Game over')
						point = 0
						ii = input('Enter \'play\' to start the game: ')
						if ii.lower() == 'play':
							continue
						else:
							break
					else: 
						print('Cau tra loi khong hop le')
						continue
			else:
				print(a, '-', b, '=',c )
				i = input('O or X: ')
				if a - b == c:
					if i == 'O' or i == 'o':
						point += 1
					elif i == 'X' or 'x':
						print('Game over')
						point = 0
						ii = input('Enter \'play\' to start the game: ')
						if ii.lower() == 'play':
							continue
						else:
							break
					else: 
						print('Cau tra loi khong hop le')
						continue
				else:
					if i == 'X' or i == 'x':
						point += 1
					elif i == 'O' or 'o':
						print('Game over')
						point = 0
						ii = input('Enter \'play\' to start the game: ')
						if ii.lower() == 'play':
							continue
						else:
							break
					else: 
						print('Cau tra loi khong hop le')
						continue

		else:
			if pt == 0:
				print(a, '+',b,'=', a + b)
				i = input('O or X: ')
				if i == 'O' or i == 'o':
					point += 1
				elif i == 'X' or 'x':
					print('Game over')
					point = 0
					ii = input('Enter \'play\' to start the game: ')
					if ii.lower() == 'play':
						continue
					else:
						break
				else: 
					print('Cau tra loi khong hop le')
					continue
			else:
				print(a,'-',b,'=', a - b)
				i = input('O or X: ')
				if i == 'O' or i == 'o':
					point += 1
				elif i == 'X' or 'x':
					print('Game over')
					point = 0
					ii = input('Enter \'play\' to start the game: ')
					if ii.lower() == 'play':
						continue
					else:
						break
				else: 
					print('Cau tra loi khong hop le')
					continue

else:
	print('Goodbye')

