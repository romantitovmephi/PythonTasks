from array import array

my_int_array = array('i', [12, 45, 34, 77, 80])

# сохраним массив в файл my_array.bin
with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

# прочитаем из файла
imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)

# метод reverse
imported_array.reverse()
print(imported_array)
