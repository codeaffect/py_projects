# If number is divisible by 3 then result=FIZZ
# If number is divisible by 5 then result=BUZZ
# If number is divisible by 3 & 5 then result=FIZZ_BUZZ


def fizz_buzz(inputValue):
    if inputValue % 3 == 0 and inputValue % 5 == 0:
        print("FIZZ_BUZZ")
    elif inputValue % 3 == 0:
        print("FIZZ")
    elif inputValue % 5 == 0:
        print("BUZZ")
    else:
        print("pfft")


def isInteger(inputValue):
    try:
        if int(inputValue):
            return True
    except ValueError:
        return False


def ReadInputValue():
    print("Enter a Number: ")
    inputValue = input()
    if inputValue == "x":
        print("=== Thank you! ====")
        return

    if not isInteger(inputValue):
        print(" **** Not a valid number *****")
        ReadInputValue()
    else:
        fizz_buzz(int(inputValue))
    ReadInputValue()


print(">>>>> START <<<<<<<")
ReadInputValue()
print(">>>>> END <<<<<<<")
