def merge_lists_to_dict(name, price):
    merge = zip(name, price)
    in_dict = dict(merge)
    return in_dict


name = ['orange', 'lemon']
price = [15, 13]
result = merge_lists_to_dict(name, price)
print(result)
