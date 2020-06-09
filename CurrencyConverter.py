# Python 3.8

def inputInt(prompt=""):
    while True:
        try:
            res = int(input(prompt))
            return res
        except:
            print("Invalid input")


def inputFloat(prompt=""):
    while True:
        try:
            res = float(input(prompt))
            return res
        except:
            print("Invalid input")


def Menu(menuItems):
    i = 0
    while i < len(menuItems):
        print("[" + str(i) + "]", menuItems[i])
        i += 1

    while True:
        out = inputInt("Your choise: ")
        if out >= 0 and out < len(menuItems):
            return out
        else:
            print("Invalid input")


def Main():
    currency = ["USD", "EUR", "UAH", "PLN", "BYR", "CNY", "RUB"]

    print("Convert from:")
    convFrom = Menu(currency)
    print("\n" * 2)

    print("Convert to:")
    convTo = Menu(list(currency[0: convFrom]) +
                  list(currency[convFrom + 1: len(currency)]))
    if convTo >= convFrom:
    	convTo += 1
    print("\n" * 2)

    convValue = 0
    while True:
        convValue = inputFloat(f"Enter amoun in {currency[convFrom]}: ")
        if convValue > 0:
            break
        else:
            print("Invalid input")


    print("\nChoose an input option: ")
    choise = Menu([f"Enter {currency[convFrom]} cost in {currency[convTo]}: ",
                   f"Enter {currency[convTo]} cost in {currency[convFrom]}: "])
    print()

    convRate = 0
    if choise == 0:
        while True:
            convRate = inputFloat(f"Enter {currency[convFrom]} cost in {currency[convTo]}: ")
            if convRate > 0:
                break
            else:
                print("Invalid input")
        convResult = convValue * convRate

    elif choise == 1:
        while True:
            convRate = inputFloat(f"Enter {currency[convTo]} cost in {currency[convFrom]}: ")
            if convRate > 0:
                break
            else:
                print("Invalid input")
        convResult = convValue / convRate

    print(str(round(convValue, 2)), currency[convFrom], "=", str(round(convResult, 2)), currency[convTo])


Main()
convAgain = 'n'
while True:
    convAgain = input("\nConvert again? (y/n): ")
    if convAgain == 'y':
        Main()
    else:
        break
