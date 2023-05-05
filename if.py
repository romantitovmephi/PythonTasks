def rout_info(my_dict):
    if my_dict.get('distance') and (type(my_dict['distance']) is int):
        return f"Distance to your destination is {my_dict['distance']}"

    if (not my_dict.get('distance') and
        my_dict.get('speed') and
        my_dict.get('time') and
        (type(my_dict['speed']) is int) and
            (type(my_dict['time']) is int)):
        return f"Distance to your destination is {my_dict['speed'] * my_dict['time']}"
    return "No distance info is available"


my_dict = {
    # 'distance': 75,
    'speed': 15,
    'time': 5,
    'relax_time': 1
}

print(rout_info(my_dict))
