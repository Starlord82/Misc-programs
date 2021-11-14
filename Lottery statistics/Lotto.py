import pandas as pd
from tkinter import filedialog

filename = filedialog.askopenfilename(title = "Select CSV file", filetypes = (("CSV files", "*.csv"),))

df = pd.read_csv(filename, encoding = "ISO-8859-1")

my_columns = list(df.columns)

new_col = [my_columns[x] for x in range(1,9)]

df = df.filter(new_col)

my_columns = list(df.columns)

df.rename(columns={my_columns[0] : "Date",my_columns[-1] : "Strong Number"}, inplace = "True")

dcounter = {}

for x in range(1,38):
	dcounter[str(x)] = 0 

row = 0

while row < 1944:
	for col in range(1,7):
		dcounter[str(df.loc[row,str(col)])] += 1 
	row += 1

df_new = pd.DataFrame(dcounter,index = [0])


lottery_list = []
lottery_num = []
for x in range(1,38):
	num = df_new.loc[0,str(x)]
	if len(lottery_list) < 8:
		lottery_list.append(x)
		lottery_num.append(num)
	else:
		if num > min(lottery_num):
			ind = lottery_num.index(min(lottery_num))
			lottery_list[ind] = x
			lottery_num[ind] = num
		
lottery_others = {}
for x in range(1,38):
	dcounter[str(x)] = 0 

lottery_list = sorted(lottery_list)

print(lottery_list)
print(lottery_num)
for x in range(1,38):
	num = df_new.loc[0,str(x)]
	if num in lottery_num and x not in lottery_list:
		lottery_others[x] = num

lottery_precentage = [(x/row)*100 for x in lottery_num]
print(lottery_others)
print(lottery_precentage)

row_new = 0
result_list = []
while row_new < len(df):
	result = [df.loc[row_new,str(x)] for x in range(1,7)]
	result_list.append(result)
	row_new += 1

matches = []

for res in result_list:
	if set(res).issubset(set(lottery_list)):
		print(res)

print(matches)







	

