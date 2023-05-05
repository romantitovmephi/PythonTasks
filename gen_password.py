import secrets
import string


# соберем все символы
all_symbols = string.ascii_letters + string.digits + string.punctuation

# print(string.punctuation)
# с помощью join получим 10 случайных символов в виде пароля
print(''.join(secrets.choice(all_symbols) for i in range(10)))
