print('hello')
first_name=input('whats your first name? ')
last_name=input('whats your last name? ')
print((f'Well hello {first_name} ,{last_name}.Good Day!'))
dob =input('what year were you born? ')
age = 2019 - int(dob)
weight_lbs= input('how much do you weigh (in lbs)? ')
weight_kgs= float(weight_lbs) *.45
fav_color = 'finally, whats your favorite color? '
ending_stars= '*'*10
print(f'''
Yay! we are done.
Thanks for being patient.
We have created a profile for you.
Username      : {first_name[0:1]}{last_name}
Display Name  : {first_name}, {last_name}
Age           : {age}
weight in lbs : {weight_lbs}
weight in kgs : {weight_kgs}
Favorite Color: {fav_color}

Enjoy!
{ending_stars}
''')