lst = []
for _ in range(int(input())):
    command, *params = input().split()
    if command == "print":
        print(lst)
    elif command == "insert":
        lst.insert(int(params[0]), int(params[1]))
    elif command == "remove":
        lst.remove(int(params[0]))
    elif command == "pop":
        lst.pop(len(lst)-1)
    elif command == "sort":
        lst.sort()
    elif command == "reverse":
        lst.reverse()
    elif command == "append":
        lst.append(int(params[0]))
