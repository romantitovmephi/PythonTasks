my_dict = {'x': 1.1, 'y': 2, 'z': 3}


def dict_to_list():
    my_list = []
    for key in my_dict:
        if type(my_dict[key]) is int:
            my_tuple = key, my_dict[key]*2
        else:
            my_tuple = key, my_dict[key]

        my_list.append(my_tuple)
        print(type(my_dict[key]))
    return my_list


print(dict_to_list())
