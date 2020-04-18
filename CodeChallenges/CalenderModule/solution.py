import calendar

# print(*calendar.day_name)
# days = ['MONDAY', 'TUESDAY', 'WEDNESDAY','THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(year=y, month=m, day=d)])
