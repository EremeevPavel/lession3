def exe_2(**kwargs):
    return kwargs


n = input("Имя: ").title()
s = input("Фамилия: ").title()
d = input("Дата рождения: ")
c = input("Город проживания: ").title()
e = input("Электронный адрес: ").lower()
tel = input("Телефон: ")
print(exe_2(Имя=n, Фамилия=s, Дата_рождения=d, Город_проживания=c, e_mail=e, Телефон=tel))
