import re

text = '''
234-234-234
234.234.234
234.234.234.
234*234*234
123..234.234

4567891234567890
4567891234777777
4567-8912-3456-7890
4567_8912_3456_7890
1234555566667777
'''

# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
pattern = re.compile(
    r'[4,5,6](\d{15}|\d{3}-?[^\s_]\d{4}-?[^\s_]\d{4}-?[^\s_]\d{4})')
pattern2 = re.compile(r'(\d)\1\1\1')
matches = pattern.finditer(text)
# for match in matches:
#     print(match)

s = input()
if(pattern.search(s) and not pattern2.search(s.replace("-", ""))):
    print('valid')
else:
    print('invalid')


# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import re


# for _ in range(int(input())):
#     s = input()

#     if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
#         print("Valid")
#     else:
#         print("Invalid")
