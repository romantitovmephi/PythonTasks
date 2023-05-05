import sys
from array import array

print(sys.argv)

# ожидаются 3 аргумента от пользователя
# username, password и имя файла (my_array.bin)
# из которого будет импортирован массив

if len(sys.argv) < 3:
    raise IOError("You must provide username, password and array filename")

array_filename = sys.argv[3]
imported_array = array('i')

with open(array_filename, 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)
