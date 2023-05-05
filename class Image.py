class Image:
    total_images = 0  # атрибут КЛАССА Image

    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension
        # под __init__ - создаются СОБСТВЕННЫЕ атрибуты,
        # каждого экземпляра класса Image
        Image.total_images += 1  # считает картинки

    def resize(self):          # это уже МЕТОД всего класса Image
        self.resolution = "1280x720"

    def up_title(self):        
        self.title = self.title.upper()

    def re_extension(self):    
        self.extension = 'jpg'

    @staticmethod    # декоратор - не привязан к экземпляру класса, работает и как собственный атрибут, и как атрибут класса
    def merge_info_image(first, second):
        return f"{first} {second}"


my_first_pic = Image("2560x1440", 'Cat', 'gif')
my_second_pic = Image("1920x1080", 'Dog', 'png')

print(my_first_pic.resolution, my_first_pic.title, my_first_pic.extension)

my_first_pic.resize()  # меняем этим МЕТОДОМ размер картинки
my_first_pic.up_title()  # делаем название капсом
my_first_pic.re_extension()  # меняем расширение

print(my_first_pic.resolution, my_first_pic.title, my_first_pic.extension)

# для второй картинки
print(my_second_pic.resolution, my_second_pic.title, my_second_pic.extension)

my_second_pic.resize()  
my_second_pic.up_title() 
my_second_pic.re_extension() 

print(my_second_pic.resolution, my_second_pic.title, my_second_pic.extension)

# для статического метода
my_pet = Image("2560x1440", 'Pet', 'gif')
my1 = Image.merge_info_image("This is", 'Cat')
print(my1)
my2 = my_pet.merge_info_image("This is", 'Dog')
print(my2)

print(Image.total_images)  # считает картинки
