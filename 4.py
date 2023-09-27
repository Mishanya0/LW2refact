try:
    x = 1 / 0
except ZeroDivisionError:
    print("Деление на ноль!")
finally:
    print("Конец программы")
