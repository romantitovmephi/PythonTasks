def image_info(**my_dict):
    # print(my_dict)  # переданный словарь в функцию
    if not (my_dict['image_title'] and my_dict['image_id']):
        # если хотя бы нет одного из ключей
        # not возвращает булево значение
        raise KeyError  # можно написать общий класс ошибок - Exeption
    else:
        print(f"Image {my_dict['image_title']} has id {my_dict['image_id']}")

    # return print(f"Image {my_dict['image_title']} has id {my_dict['image_id']}")


try:
    image_info(image_title="'nature'",
               imageee_id=110)  # один лишний ключ
# except KeyError:
#   print("Один из ключей отсутствует")
except KeyError as e:  # через as e - вернет значение по and
    print(e)
    print("Один из ключей отсутствует")

print('Continue...')
