a, b, c = int(input()),int(input()),int(input())

if a == b and b == c or a != c:
    print('равнобедреный')

if a == b and b == c and a == c:
    print('равносторонний')

if a != b and b != c or a != c:
    print('разностаронний')

else:
    print('ошибка')