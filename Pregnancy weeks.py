import datetime as dt


def week_by_date():

	f_date = input('Enter future date: (dd/mm/yyyy): ')

	f_day, f_month, f_year = map(int, f_date.split("/"))
	
	f_date = dt.datetime(f_year, f_month, f_day)

	weeks = int(((f_date - p_date).days)/7)

	print(f'{weeks} weeks')

def date_by_week():

	weeks = int(input('Enter week: '))
	f_days = weeks * 7

	f_date = p_date + dt.timedelta(weeks=weeks)

	f_day, f_month, f_year = (f_date.day, f_date.month, f_date.year)

	print(f'Week {weeks} will be at:\n{f_day}\\{f_month}\\{f_year}')

if __name__ == "__main__":

	while True:
		period = input('Whats the first day of the last period? (dd/mm/yyyy): ')
		print("\n"*3)
		day, month, year = map(int,period.split('/'))
		p_date = dt.datetime(year, month, day)

		choice = input('Enter "1" for week by future date, or "2" for date by week: ')

		if choice == "1":

			week_by_date()
			break

		elif choice == "2":

			date_by_week()
			break
		else:
			print('wrong input!')
			continue

