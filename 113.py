# names = [
#     "Victoria",
#     "Wade",
#     "Chanelle",
#     "Victoria",
#     "Evan",
#     "Tyrone",
#     "Neve",
#     "Peggy",
#     "Tyrone",
#     "Peggy",
# ]
#
# # Используем set для удаления дубликатов и list comprehension для фильтрации по длине имен
# unique_names = list({name for name in names if len(name) >= 5})
#
# print(unique_names)

#
# keys = ["key1", "key2", "key3", "key4"]
# values = [145, 12.4, False, "Some Text"]
#
# # Используем dict comprehension
# dictionary = {keys[i]: values[i] for i in range(len(keys))}
#
# print(dictionary)


#
# text = "This is some text to test."
#
# # Удаляем пробелы и создаем словарь с подсчетом каждой буквы
# letter_count = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
#
# print(letter_count)



# Ввод товаров пользователем
required_goods = input("Введите нужные товары (через запятую): ").lower().replace(" ", "").split(',')
available_goods = input("Введите товары на складе (через запятую): ").lower().replace(" ", "").split(',')

# Проверка наличия товаров
for item in required_goods:
    item_display = item.capitalize()
    availability = "Да" if item in available_goods else "Нет"
    print(f"<{item_display}> на складе: [{availability}]")
