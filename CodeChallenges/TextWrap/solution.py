def wrap(s, w):
    return "\n".join([s[i:i+w] for i in range(0, len(s), w)])


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
