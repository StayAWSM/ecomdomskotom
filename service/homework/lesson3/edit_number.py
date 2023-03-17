num = 8796
print(num % 10)
print(num % 1000)
print(num // 1000)
print(num // 100 + num % 100)
print(num // 1000 + num % 10)
print(num // 1000 + (num % 1000) // 100 + (num % 100) // 10 + num % 10)
#мы получчили 8   +      7            +     9               +    6



