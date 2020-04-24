import re
rp = r"^\d{2}\D\d{2}\D\d{4,}$"  # Do not delete 'r'.
s = input()
m = re.search(rp, s)
ms = re.findall(rp, s)
for mi in ms:
    print(mi)
print(str(bool(m)).lower())
