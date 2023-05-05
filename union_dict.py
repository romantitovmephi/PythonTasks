my_dict = {'a': 10, 'b': 15, 'c': 20}
other_dict = {'a': 12, 'b': 17, 'c': 22}
big_dict = {'a': 22, 'b': 27, 'c': 32, 'd': 111}

union_dict = my_dict | other_dict | big_dict
print(union_dict)

my_union_dict = {
    **my_dict,
    **big_dict,
    **other_dict,
}
print(my_union_dict)
# разные значения, так как порядок важен
