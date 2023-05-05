def merge_lists_to_dict(name, price):
    product = f"{name} {price}"
    return product


result = merge_lists_to_dict(name='orange', price=15)
print(result)

result = merge_lists_to_dict('orange', price=15)
print(result)

result = merge_lists_to_dict('orange', 15)
print(result)
