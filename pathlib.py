from pathlib import Path

my_dir = Path('/Users') / 'Roman' / 'Desktop' / 'python practice' / 'files'


# проверяем exists(), если папка files еще не существует, то создаем ее mkdir()
if not my_dir.exists():
    my_dir.mkdir()


# проверяем, если папка files существует, то удаляем ее
# if my_dir.exists():
#     my_dir.rmdir()


# при инструкции with после выполнения операций, файл закроется автоматически
with open("files/first.txt", 'w') as first_file:
    first_file.write("First string\n")
    first_file.write("Second string\n")

with open("files/second.txt", 'w') as second_file:
    second_file.write("First string file\n")
    second_file.write("Second string file\n")

# поэтому, чтобы прочитать, его надо снова открыть уже в режиме чтения
with open("files/first.txt") as first_file:
    print(first_file.read())  # прочитать сразу все строки

with open("files/second.txt") as second_file:
    print(second_file.readline())  # прочитать только первую строку
    print(second_file.readline())  # прочитать вторую строку из файла


# удаление файлов
# first_file = Path("files/first.txt")
# if first_file.exists():  # если first_file существует, то удаляем его
#     first_file.unlink()

# second_file = Path("files/second.txt")
# if second_file.exists():  # если second_file существует, то удаляем его
#     second_file.unlink()
