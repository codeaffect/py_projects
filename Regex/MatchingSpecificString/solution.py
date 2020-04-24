import re

rp = r'wikipedia'
s=''
while s!='x':
    s = input()
    m =  re.findall(rp,s)
    print('Number of matches:',len(m))