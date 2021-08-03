import datetime

period = input('Whats the first day of the last period? (dd/mm/yyyy): ')

day, month, year = map(int,period.split('/'))

f_date = input('Enter future date: (dd/mm/yyyy): ')

f_day, f_month, f_year = map(int, f_date.split("/"))


p_date = datetime.datetime(year, month, day)
f_date = datetime.datetime(f_year, f_month, f_day)

weeks = int(((f_date - p_date).days)/7)

print(f'{weeks} weeks')