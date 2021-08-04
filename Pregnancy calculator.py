import datetime as dt
import os


def week_by_date():

	f_date = input('Enter future date: (dd/mm/yyyy): ')
	print("\n"*3)

	f_day, f_month, f_year = map(int, f_date.split("/"))
	
	f_date = dt.datetime(f_year, f_month, f_day)

	weeks = int(((f_date - p_date).days)/7)
	print('You will be:')
	print(f'{weeks} weeks pregnant')
	print("\n"*3)

def date_by_week():

	weeks = int(input('Enter week: '))
	print("\n"*3)
	f_days = weeks * 7

	f_date = p_date + dt.timedelta(weeks=weeks)

	f_day, f_month, f_year = (f_date.day, f_date.month, f_date.year)

	print(f'Week {weeks} will be at:\n{f_day}\\{f_month}\\{f_year}')

if __name__ == "__main__":
	
	print('Hello and welcome to Pregnancy Calculator!')
	check = True
	while check:
		print("\n"*3)
		period = input('Whats the first day of the last period? (dd/mm/yyyy): ')
		print("\n"*3)
		day, month, year = map(int,period.split('/'))
		p_date = dt.datetime(year, month, day)
		while True:
			choice = input('Enter "1" for week by future date, or "2" for date by week: ')
			print("\n"*3)

			if choice == "1":

				week_by_date()
				break

			elif choice == "2":

				date_by_week()
				break
			else:
				print('wrong input!')
				continue
		print("\n"*3)
		i = input('continue? (y/n): ')
		if i in ['y','Y','']:
			check = True
		else:
			print('Thank you for you using pregnancy calculator')
			check = False
		os.system('cls')

