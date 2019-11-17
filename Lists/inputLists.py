def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


x = input("X: ")
mylist = x.split(",")
print(f"Length of string: {len(mylist)}")
for i in mylist:
    print(f"item: {i}", end=",")
    print(f"type: {type(i)}")
    if isInt(i):
        print(f"**YES! is an integer")
    elif isfloat(i):
        print(f">>YES! is a float")
    else:
        print("--Not an integer")
