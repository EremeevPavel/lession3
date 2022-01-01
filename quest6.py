def int_func(str):
    return str.title()  # Можно поставить capitalize для того что бы выводилась только первая заглавная буква из введеного предложения.


text = input('Введи текст: ')

print(int_func(text))
