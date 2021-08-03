import datetime

period = input('Whats the first day of the last period? (dd/mm/yyyy): ')

def week_by_date():
	day, month, year = map(int,period.split('/'))

	f_date = input('Enter future date: (dd/mm/yyyy): ')

	f_day, f_month, f_year = map(int, f_date.split("/"))


	p_date = datetime.datetime(year, month, day)
	f_date = datetime.datetime(f_year, f_month, f_day)

	weeks = int(((f_date - p_date).days)/7)

	print(f'{weeks} weeks')

def date_by_week():

	weeks = input('Enter week: ')
	days = weeks * 7
	f_date = p_date + datetime.timedelta(days = days)

	print(f_date)

if __name__ == "__main__":

	while True:

		choice = input('Enter "1" for week by future date, or "2" for date by week')

		if choice == "1":

			week_by_date()
			break

	 	elif choice == "2":

	 		date_by_week()
	 		break
	 	else:
	 		print('wrong input!')
	 		continue

