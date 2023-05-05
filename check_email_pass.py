import re


email = input("Придумайте и введите email: ")
password = input("Придумайте и введите пароль: ")

# функция проверки корректности email


def check_email(email):
    # структура email
    email_regexp = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    # передаем методу compile r строку и создаем паттерн
    email_check_pattern = re.compile(email_regexp)
    # должно быть полное совпадение fullmatch со структурой паттерна
    # print(email_check_pattern.fullmatch(email))
    validation_result = "email valid" if email_check_pattern.fullmatch(
        email) else "email not valid"
    return (email, validation_result)

# # функция проверки корректности пароля


def check_password(password):
    password_regexp_low_char = r"[a-z]+"
    password_regexp_up_char = r"[A-Z]+"
    password_regexp_digit = r"[0-9]+"
    password_regexp_spec = r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]+"

    # создаем 4 паттерна
    # по этим паттернам методом search будем искать совпадения в password
    pass_check_pattern_low_char = re.compile(password_regexp_low_char)
    pass_check_pattern_up_char = re.compile(password_regexp_up_char)
    pass_check_pattern_digit = re.compile(password_regexp_digit)
    pass_check_pattern_spec = re.compile(password_regexp_spec)

    # увидеть, где найдено совпадение
    # print(pass_check_pattern_low_char.search(password))
    # print(pass_check_pattern_up_char.search(password))
    # print(pass_check_pattern_digit.search(password))
    # print(pass_check_pattern_spec.search(password))

    # print(bool(pass_check_pattern_low_char.search(password)))
    # print(bool(pass_check_pattern_up_char.search(password)))
    # print(bool(pass_check_pattern_digit.search(password)))
    # print(bool(pass_check_pattern_spec.search(password)))

    pass_validation_result = "password valid" if len(password) >= 8 and pass_check_pattern_low_char.search(
        password) and pass_check_pattern_up_char.search(
        password) and pass_check_pattern_digit.search(
        password) and pass_check_pattern_spec.search(
        password) else "password not valid"
    return (password, pass_validation_result)


print(check_email(email))
print(check_password(password))

# в r строке можно передавать спец. символы,
# поэтому их используют в регулярных выражениях
