my_dict_list = [
    {'name': 'Roman', 'years': 28},
    {'name': 'Katya', 'years': 24},
    {'name': 'Vaska', 'years': 24}
]  # список из 3х словарей

first, second, third = my_dict_list
# распаковали список в 3 переменные
print(first)
print(second)
print(third)

# распаковываем словарь в функции


def my_func(name, years):
    return f"{name} now {years} years"


print(my_func(**first))
print(my_func(**second))
print(my_func(**third))
