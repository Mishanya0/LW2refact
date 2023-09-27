def process_data(data):
    if isinstance(data, dict):
        top_keys = sorted(data, key=data.get, reverse=True)[:3]
        return top_keys
    elif isinstance(data, list):
        count = len([num for num in data if num % 2 == 0])
        unique_list = list(set(data))
        return count, unique_list
    elif isinstance(data, int):
        digit_sum = sum(int(digit) for digit in str(data))
        return digit_sum
    elif isinstance(data, str):
        clean_string = ' '.join(data.split())
        word_count = len(clean_string.split())
        return clean_string, word_count
    else:
        return "Невалидный тип данных. Введите строку, словарь, список или число"

input_dict = {
    "apple": 42,
    "banana": 30,
    "orange": 35,
    "grape": 25,
    "kiwi": 50
}

input_list = [1, 2, 3, 4, 5, 2, 4, 6, 8]
input_num = 12345
input_str = "Hello, $123 world! Клоп."

output_dict = process_data(input_dict)
output_list = process_data(input_list)
output_num = process_data(input_num)
output_str = process_data(input_str)

print("Вывод словаря:", output_dict)
print("Вывод списка:", output_list)
print("Вывод числа:", output_num)
print("Вывод строки:", output_str)






