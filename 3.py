def count_nonzero_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    count = 0
    for j in range(num_cols):
        zero = False
        for i in range(num_rows):
            if matrix[i][j] == 0:
                zero = True
                break
        if not zero:
            count += 1

    return count

while True:
    try:
        num_rows = int(input("Введите количество строк: "))
        num_cols = int(input("Введите количество столбцов: "))
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
matrix = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        while True:
            try:
                element = int(input(f"Введите элемент [{i}][{j}]: "))
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")
        row.append(element)
    matrix.append(row)
nonzero_count = count_nonzero_columns(matrix)

print(f"Количество столбцов, не содержащих ни одного нулевого элемента: {nonzero_count}")
