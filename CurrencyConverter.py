USD = 26.80

print("Курс доллара:", str(USD))
choise = input("Изменить? (y/n): ")

if choise == "y":
    USD = float(input("Новый курс доллара: "))
print()

usrNum = float(input("Введите суму: "))

print(str(round(usrNum, 2)), "UAH", "=", round(usrNum / USD, 2), "USD")
print(str(round(usrNum, 2)), "USD", "=", round(usrNum * USD, 2), "UAH")

input()