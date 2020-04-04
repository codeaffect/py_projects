def count_substring(string, ss):
    c = 0
    i = 0
    while i < len(string):
        index = string.find(ss, i)
        if index == -1:
            return c
        else:
            i = index+1
            c += 1

    return c


string, sub_string = map(str, input().strip().split())

count = count_substring(string, sub_string)
print(count)
