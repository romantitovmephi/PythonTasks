class Image:

    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def __eq__(self, other):  # добавлен маг-й метод сравнения (нет по умол-ю)
        if (self.resolution == other.resolution and
            self.title == other.title and
                self.extension == other.extension):
            return True
        return False


my_first_pic = Image("2560x1440", 'Cat', 'gif')
my_second_pic = Image("2560x1440", 'Cat', 'gif')

print(my_first_pic == my_second_pic)
