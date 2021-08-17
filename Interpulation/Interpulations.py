
def inter(d1,d2,e1,e2,pn):
	result = {}
	for num in range(pn):
		
		user_dist = float(input(f'Enter distanse of point number {num+1}: '))
		result[user_dist] = e1 + ((e2-e1)/(d2-d1))*(user_dist-d1)

	for key, value in result.items():

		print(f'\n{key} : {value:.2f}')

if __name__ == "__main__":
	dist1  = float(input("Enter first distanse: "))
	dist2  = float(input("Enter last distanse: "))
	elev1 = float(input("Enter first elevation: "))
	elev2 = float(input("Enter last elevation: "))

	point_num = int(input("How many points between? "))

	inter(dist1, dist2, elev1, elev2, point_num)

