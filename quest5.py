def calc_sum(*nums):
    sum = 0
    stop = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            stop = True
    return sum, stop


sum_2 = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop = calc_sum(*numbers_string)
    sum_2 += sum
    print(f'Сумма: {sum_2}')

    if stop:
        break
