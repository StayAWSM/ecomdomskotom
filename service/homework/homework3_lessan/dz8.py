a = 123

b = a // 100
c = a % 100
print(b, c, sep='')#123

b = a // 100
c = a % 10
d = a % 100 // 10
print(b, c, d, sep='')#132

b = a % 100 // 10
c = a // 100
d = a % 10
print(b, c, d, sep='')#213

b = a % 100 // 10
c = a // 100 + a % 100 // 10
d = a // 100
print(b, c, d, sep='')#231

b = a % 10
c = a // 10
print(b, c, sep='')#312

b = a % 10
c = a // 10 % 10
d = a // 100
print(b, c, d, sep='')#321

