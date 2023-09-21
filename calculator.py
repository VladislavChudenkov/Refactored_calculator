import math
def checkInt():
    while(True):
        firstNumber = input()
        if firstNumber.isdigit():
            return float(firstNumber)
        else:
            print("Вы ввели не число")
            continue


def getResult(action, firstNumber, secondNumber):
    match action:
        case "+":
            return (firstNumber + secondNumber)
        case "-":
            return (firstNumber - secondNumber)
        case "*":
            return (firstNumber * secondNumber)
        case "/":
            if secondNumber == 0:
                print("Делить на ноль нельзя")
            else:
                return (firstNumber / secondNumber)
        case "tan":
            return (math.tan(firstNumber))
        case "sin":
            return (math.sin(firstNumber))
        case "cos":
            return (math.cos(firstNumber))
        case "!":
            return (math.factorial(firstNumber))
        case "sqrt":
            return (math.sqrt(firstNumber))
        case "^":
            return (firstNumber ** secondNumber)
        case _:
            print("Неизвестная операция")
            return(None)

    
lastresult= (None)
bool  (True)
while (True):
    print ("Последний результат " + str(lastresult))
    print("Введите действие (end для завершения работы программы)")
    action = input()
    if action == "end":
        break
    print("Введите первое число")
    firstNumber = checkInt()
    print("Введите второе число")
    secondNumber = checkInt()
    lastresult= getResult(action, firstNumber, secondNumber)
    print(lastresult)