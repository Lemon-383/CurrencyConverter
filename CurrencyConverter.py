# Python 3.8

def inputInt(prompt = ""):
    while True:
        try:
            res = int(input(prompt))
            return res
        except:
            print("Invalid input")


def inputFloat(prompt = ""):
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
    convTo = Menu(currency)

    if convTo == convFrom:
    	while not (convTo >= 0 and convTo < len(currency) and convFrom != convTo):
    		print("Invalid input")
    		convTo = inputInt("Your choise: ")
    print("\n" * 2)
    				

    convValue = 0
    while True:
    	convValue = inputFloat(f"Enter amoun in {currency[convFrom]}: ")
    	if convValue > 0:
    		break
    	else:
    		print("Invalid input")


    print("\nChoose an input option: ")
    choise = Menu([f"Enter {currency[convFrom]} cost in {currency[convTo]}: ", f"Enter {currency[convTo]} cost in {currency[convFrom]}: "])
    print()

    convRate = 0
    if choise == 0:
    	convRate = inputFloat(f"Enter {currency[convFrom]} cost in {currency[convTo]}: ")
    	convResult = convValue * convRate

    elif choise == 1:
    	convRate = inputFloat(f"Enter {currency[convTo]} cost in {currency[convFrom]}: ")
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
