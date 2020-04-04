def remove_dups(s):
    s1 = []
    for i in range(len(s)):
        if s[i] not in s1:
            s1.append(s[i])
    return ''.join(s1)


def merge_the_tools(s, k):
    s1 = [remove_dups(s[i:i+k]) for i in range(0, len(s), k)]
    print(*s1, sep='\n')


string, k = 'aabbbcccd', 3  # input(), int(input())
merge_the_tools(string, k)
