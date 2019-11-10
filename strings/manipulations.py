print('*'*10+'START'+'*'*10)
message = 'How are you'
#index of a string
print (f'Index of "you" in "{message}"')
print(message.find('you'))
#replace string
print('Replacing "you" with "YOU"');
message = message.replace('you','YOU')
print(message)
#lower and upper case
print('lower:'+message.lower()+'\nUPPER:'+message.upper())
#checking values in a string
print(f'Does "are" exists in "{message}"?')
print('are' in message)
#title()
print('title()::--',message.title())