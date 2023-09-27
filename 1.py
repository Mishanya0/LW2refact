def countofsymbols():
    countvow = 0
    countcons = 0
    vowels = 'aeiouаэыуояеёюи'
    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'
    stroka = input("Введите строку: ")
    for el in stroka:
        if el.lower() in vowels:
            countvow += 1
        elif el.lower() in consonants:
            countcons += 1
    return countvow, countcons

try:
    a = 0
    while a != 1:
         countvow_val, countcons_val = countofsymbols()
         if countvow_val == 0 and countcons_val == 0:
            print("Введите непустую либо минимум с одной буквой строку")
            continue
         print(f"Количество гласных - {countvow_val}\n"
            f"Количество согласных - {countcons_val}")
except ValueError as e:
    print(f"Ошибка: {e}")