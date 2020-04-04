def hasAlphaNum(s):
    for c in s:
        if c.isalnum():
            return True
    return False


def hasAlphabet(s):
    for c in s:
        if c.isalpha():
            return True
    return False


def hasDigit(s):
    for c in s:
        if c.isdigit():
            return True
    return False


def hasLower(s):
    for c in s:
        if c.islower():
            return True
    return False


def hasUpper(s):
    for c in s:
        if c.isupper():
            return True
    return False


s = input()
print(hasAlphaNum(s), hasAlphabet(s), hasDigit(
    s), hasLower(s), hasUpper(s), sep='\n')
