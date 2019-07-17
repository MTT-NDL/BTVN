# Ex1:
for i in range(8,0,-1):
    print('*'*i)

# Ex2:
a = input('Hay nhap n so, yeu cau moi so cach nhau boi dau phay: ')
b = a.split(',')
s = 0
for i in b: 
    s += int(i)
print(s / len(b))

# Ex3:
year = int(input("Nhap nam muon kiem tra:"))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("Day la nam nhuan")
else:
    print("Day khong la nam nhuan")

# Ex4:
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a == 0:
    if b != 0:
        print('Phuong trinh co mot nghiem')
        print('x = ',(-c)/b)
    else:
        if c != 0:
            print("Phuong trinh vo nghiem")
        else:
            print('Phuong trinh co vo so nghiem')
else:
    delta = b**2 - 4*a*c
    if delta == 0:
        print('Phuong trinh co mot nghiem')
        print('x = ',(-b)/(2*a))
    elif delta < 0:
        print('Phuong trinh vo nghiem')
    else:
        print('Phuong trinh co hai nghiem phan biet')
        from math import sqrt
        print('x1 = ',((-b)+(-sqrt(delta)))/(2*a))
        print('x2 = ',((-b)+(sqrt(delta)))/(2*a))