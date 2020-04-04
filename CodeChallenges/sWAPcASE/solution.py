def swap_case(phrase):
    result = ''
    for char in phrase:
        if char.isupper():
            result = result+char.lower()
        else:
            result = result+char.upper()
    return result


s = input()
result = swap_case(s)
print(result)
