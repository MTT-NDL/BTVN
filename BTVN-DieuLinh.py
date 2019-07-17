# Ex1: Tạo 2 biến chứa số nguyên cho trước, bạn hãy tính tổng, hiệu, tích và thương của hai số rồi in kết quả ra màn hình.
a = 29
b = 1
print('Tong =', a + b)
print('Hieu =', a - b)
print('Tich =', a * b)
print('Thuong =', a / b)

# Ex2: Nhập hai số nguyên từ bàn phím, tính tổng, trung bình cộng của chúng và in ra màn hình.
a = int(input('Please enter the first integer: '))
b = int(input('Please enter the second integer: '))
print('Tong =', a + b)
print('Trung binh cong =', (a + b)/2)

# Ex3: Viết chương trình cho người dùng nhập hai số nguyên x, y, sau đó tính: p=x*y, s=x+y, q=s2+p(s-x)*(p+y) và in kết quả ra màn hình.
a = int(input("x = "))
b = int(input("y = "))
p = a*b
s = a+b
print("p=x*y=",p)
print("s=x+y=",s)
print("q=2s+p(s-x) =", 2*s+p*(s-a))

# Ex4: Chương trình cho người dùng nhập hai số và nhập một phép toán. Tương ứng với phép toán đã nhập bạn thực hiện phép tính trên hai số và in kết quả ra màn hình. Note: yêu cầu nhập đủ các phép tính +, -, *, /, %, **
a = int(input('Moi nhap so thu nhat: '))
b = int(input('Moi nhap so thu hai: '))
c = input('Moi nhap phep toan ban muon thuc hien (+, -, *, /, %, **): ')
if c == '+':
	print(a + b)
elif c == '-':
	print(a - b)
elif c == '*':
	print(a * b)
elif c == '/':
	print(a / b)
elif c == '%':
	print(a % b)
elif c == '**':
	print(a ** b)
else:
	print("Phep tinh khong hop le")

# Ex5: Viết chương trình yêu cầu nhập địa chỉ(yêu cầu viết đúng theo chính tả) sau đó in địa chỉ ở dạng viết hoa(uppercase) và viết thường(lowercase)	
a = input('Please enter your address: ')
print(a.lower())
print(a.upper())