s = input()
methods = [str.isalnum,  str.isalpha,  str.isdigit, str.islower, str.isupper]

for res in map(lambda m: any(map(m, s)), methods):
    print(res)

# Second method
s = input()
for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(any("c." + test + "()" for c in s))
