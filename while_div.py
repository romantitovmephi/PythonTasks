def delenie():
    while True:
        number1 = float(input("Введите первое число: "))
        global number2  # global чтобы использовать во втором цикле
        number2 = float(input("Введите второе число: "))

        if number2 == 0:
            raise ValueError

        print(number1/number2)
        answer = input("Хотите продолжить (да/нет) ? ")
        if answer == 'да':
            continue      # цикл выполняется повторно
        if answer == 'нет':
            break         # выход из цикла


# обработка деления на 0
try:
    delenie()
except ValueError:
    print("Ошибка: нельзя делить на 0!")

# print(bool(number2 == 0)) - проверить условие
# второй цикл запускается, если второе введенное число 0

while number2 == 0:
    next_answer = input("Хотите продолжить (да/нет) ? ")
    if next_answer == 'да':
        try:
            delenie()
        except ValueError:
            print("Ошибка: нельзя делить на 0!")
            continue
    break
