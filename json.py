import json


my_dict = {'a': 1,
           'b': 2.5,
           'c': "apps",
           'd': True,
           'e': [5, 7],
           'f': {'g': 123}, }

# конвертируем словарь в формат json и добавляем indent для отступов
my_json = json.dumps(my_dict, indent=1)

print(my_json)
print(type(my_json))  # формат json это всего лишь строка
