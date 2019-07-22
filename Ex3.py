# Ex3:
a = input('Moi nhap ten dang nhap: ')
b = input('Moi nhap mat khau: ')
while b.isalpha() or b.isnumeric() or len(b) < 8:
    print('Mat khau khong hop le')
    b = input('Moi nhap mat khau: ')
c = input('Moi nhap lai mat khau: ')
while b != c:
    print('Mat khau nhap lai khong giong, moi nhap lai')
    b = input('Moi nhap mat khau: ')
    while b.isalpha() or b.isnumeric() or len(b) < 8:
        print('Mat khau khong hop le')
        b = input('Moi nhap mat khau: ')
    c = input('Moi nhap lai mat khau: ')
d = input('Moi nhap email: ')
while '@' not in d or '.com' not in d :
    print('Email khong hop le')
    d = input('Moi nhap email: ')

print('Da dang ky tai khoan thanh cong')