import cmath
c = complex(input())
r = cmath.polar(c)
print(*r, sep="\n")
# print(*cmath.polar(complex(input())), sep='\n')
