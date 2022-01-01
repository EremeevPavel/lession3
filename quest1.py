
def s_calc(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No values'


print(s_calc((float(input("Введи первое число: "))), float(input("Введи второе число: "))))
