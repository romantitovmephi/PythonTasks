def update_car_info(**car):
    print(car)
    info = f"{car['brand']} {car['price']}"  # просто формирование строки
    return info


result = update_car_info(brand='Audi', price=1500000, is_available=True)
print(result)

# ** - соединяет все именнованные аргументы в словарь car
