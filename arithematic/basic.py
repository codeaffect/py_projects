base_num=10
print('*'*10+'START'+'*'*10)
print(f'Base Number       :{base_num}')
print(f'Add 3             :{base_num+3}')
print(f'Substract 3       :{base_num-3}')
print(f'Multiply by 3     :{base_num*3}')
print(f'Divide by 3       :{base_num/3}')
print(f'Divide by 3(Round):{base_num//3}')
print(f'Power by 3        :{base_num**3}')
print(f'Exponent  3       :{base_num%3}')
print('-'*10+'AUGUMENTED'+'-'*10)
base_num+=3
print(f'Add base by 3            : {base_num}')
base_num-=3
print(f'Substract base by 3      : {base_num}')
base_num*=3
print(f'Multiply base by 3       : {base_num}')
base_num/=3
print(f'Division base by 3       : {base_num}')
base_num//=3
print(f'Round Division base by 3 : {base_num}')
base_num**=3
print(f'Power base with 3        : {base_num}')
base_num%=3
print(f'Exponent value of 3      : {base_num}')
print('*'*10+'END'+'*'*10)