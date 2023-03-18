num = int(input())
s = num // 1000
e = num % 10
if s == e:
    print('Они равны ')
if s != e:
    print('Они не равны ')

