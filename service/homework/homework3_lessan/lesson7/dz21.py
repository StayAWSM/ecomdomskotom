a = int(input())
if 0 <= a <= 7:
    print('ночь')
elif 7 <= a <= 11:
    print('утро')
elif 12 <= a <= 17:
    print('день')
elif 17 <= a <= 23:
    print('вечер')
else:
    print('ошибка')