import re

pattern = re.compile(
    r'^[4,5,6](\d{15}|\d{3}-?[^\s_]\d{4}-?[^\s_]\d{4}-?[^\s_]\d{4})$')
pattern2 = re.compile(r'(\d)\1\1\1')

for _ in range(int(input())):
    s = input()
    if(pattern.match(s) and not pattern2.search(s.replace("-", ""))):
        print('Valid')
    else:
        print('Invalid')
