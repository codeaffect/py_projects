def mutate_string(string, position, character):
    result = string[:position] + character + string[position+1:]
    return result


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
