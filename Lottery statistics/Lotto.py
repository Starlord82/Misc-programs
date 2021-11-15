import pandas as pd
from tkinter import filedialog
from operator import itemgetter

def FindCombo(combo,hot_list,lotto_df,rows):
	##See if there was a combinations of exactly "Combo" appearances
	result_combos = []
	for row in range(rows):
		result = [lotto_df.loc[row,str(col)] for col in range(1,7)]
		acounter = 0
		for (num, appearance, percent) in hot_list:
			if acounter == combo:
				result_combos.append(row)
				break
			else:
				if num in result:
					acounter += 1
	return result_combos

def FindAverage(dic):
	sum = 0
	for item, value in dic.items():
		sum += value
	avr = sum/(len(dic))
	return avr

##Create data base
filename = filedialog.askopenfilename(title = "Select CSV file", filetypes = (("CSV files", "*.csv"),))
df = pd.read_csv(filename, encoding = "ISO-8859-1")
my_columns = list(df.columns)
new_col = [my_columns[x] for x in range(1,9)]
df = df.filter(new_col)
my_columns = list(df.columns)
df.rename(columns={my_columns[0] : "Date",my_columns[-1] : "Strong Number"}, inplace = "True")

##Count number apperances
dcounter = {}

for x in range(1,38):
	dcounter[str(x)] = 0 

rows = 1500

for row in range(rows):
	for col in range(1,7):
		dcounter[str(df.loc[row,str(col)])] += 1 

print(f'Average percentages of apperances is {(FindAverage(dcounter)/rows)*100}')	

df_new = pd.DataFrame(dcounter,index = [0])


## Create a list with 8 numbers that appered the most
hot_list = []
hot_num = []

for x in range(1,38):
	num = df_new.loc[0,str(x)]
	if len(hot_list) < 8:
		hot_list.append((x,num,round((num/rows)*100,2)))
		hot_num.append(num)
	else:
		if num > min(hot_num):
			ind = hot_num.index(min(hot_num))
			hot_list[ind] = (x,num,round((num/rows)*100,2))
			hot_num[ind] = num

## Create a list with 8 numbers that appered the least
cold_list = []
cold_num = []

for x in range(1,38):
	num = df_new.loc[0,str(x)]
	if len(cold_list) < 8:
		cold_list.append((x,num,round((num/rows)*100,2)))
		cold_num.append(num)
	else:
		if num < max(cold_num):
			ind = cold_num.index(max(cold_num))
			cold_list[ind] = (x,num,round((num/rows)*100,2))
			cold_num[ind] = num

## Create a list with 8 numbers that overdue

overdue_list = []
first_appear = []

for x in range(1,38):
	for row in range(rows):
		res_list = [df.loc[row,str(col)] for col in range(1,7)]
		if x in res_list:
			first_appear.append((x,row+1))
			break

for x in range(8):
	max_tup_index = first_appear.index(max(first_appear,key=itemgetter(1)))
	overdue_list.append(first_appear.pop(max_tup_index))


print(f'The hot numbers in {rows} lotteries are: \n{hot_list}')
print(f'The cold numbers in {rows} lotteries are: \n{cold_list}')
print(f'The 8 overdue numbers are: \n{overdue_list}')
##Find duplicates

lottery_others = []

for x in range(1,38):
	num = df_new.loc[0,str(x)]
	tuptest = (x, num)
	for tup in hot_list:
		if tup[1] == tuptest[1] and tup not in hot_list:
			lottery_others.append(tuptest)

lottery_precentage = [round((x/rows)*100,2) for x in hot_num]
print(f'Duplicates are: \n{lottery_others}')
print(lottery_precentage)


##Find if combination appeard

row_new = 0
result_list = []
while row_new < len(df):
	result = [df.loc[row_new,str(x)] for x in range(1,7)]
	result_list.append(result)
	row_new += 1



for res in result_list:
	if set(res).issubset(set(hot_list)):
		print(res)

combo_num = 6
lrange = 1900
matches = FindCombo(combo_num,hot_list,df,lrange)

print(f'This combination catched {combo_num} numbers in {len(matches)} lotteries out of {lrange}, \n{matches} lotteries ago')






	

