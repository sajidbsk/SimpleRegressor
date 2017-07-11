import pandas as pd 
import linear-regressor as lr 

#Importing the dataset
dataset = pd.read_csv('data.csv', header=None)
a = dataset.values.tolist()

correlation(a)
#Prediction done here:
def predictor():
	flag = 1
	print("What parameter do you want to predict? [x, y] ")
	while flag == 1:
		x = input()
		if (x == 'x'):
			j=input("Enter value")
			print(regressor_y(j,a))
			flag = 0
		elif (x == 'y'):
			j=input("Enter value")
			print(regressor_x(j,a))
			flag = 0
		else:
			print("Value not between x or y, enter again: ")

predictor()