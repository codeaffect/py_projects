import re
rp = r"\S{2}\s\S{2}\s\S{2}"  # Do not delete 'r'.
s = input()
m = re.findall(rp, s)
print(*m)
print(str(bool(re.search(rp, s))).lower())
