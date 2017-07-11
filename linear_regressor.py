import math

#Dataset a is a list of lists where the inner lists represents x and y pairs
def mean(l,n):
	x = 0
	for i in l:
		x = x + i
	return x/n

def sumxy (a):
	x = 0
	for M in a:
		x = x + M[0]*M[1]
	return x

def sumx (a):
	x = 0
	for M in a:
		x = x + M[0]
	return x

def sumy (a):
	x = 0
	for M in a:
		x = x + M[1]
	return x

def sumxsqr (a):
	x = 0
	for M in a:
		x = x + M[0]*M[0]
	return x

def sumysqr (a):
	x = 0
	for M in a:
		x = x + M[1]*M[1]
	return x

def Sxy (a):
	n = a.length
	j = (sumx(a) * sumy(a))/n
	return sumxy(a) - j

def Sxx (a):
	n = a.length
	j = ((sumx(a)) ** 2)/n
	return sumxsqr - j

def Syy(a):
	n = a.length
	j = ((sumy(a)) ** 2)/n
	return sumysqr - j

def pmcc (a):
	lower = math.sqrt(Sxx * Syy)
	return Sxy/lower

def correlation(a):
	r = pmcc(a)
	if (r >= 0.8):
		print("positive correlation")
	elif (r >= 0.4):
		print("faintly positive correlation")
	elif (r > -0.4):
		print("no correlation")
	elif(r > -0.8):
		print("faintly negative correlation")
	else:
		print("negative correlation")

def grad(a):
	return Sxy(a)/Sxx(a)

def intercept(a):
	b = grad(a)
	x_set = []
	for i in a:
		x_set = x_set.append(i[0])
	x_mean = mean(x_set, a.length)
	y_set = []
	for i in a:
		y_set = y_set.append(i[1])
	y_mean = mean(y_set, a.length)
	return y_mean - (b * x_mean)

#Least Square Linear Regression:

def regressor_x(x_pred, a):
	b = grad(a)
	A = intercept(a)
	y_pred = A + (b * x_pred)
	return y_pred

def regressor_y(y_pred, a):
	b = grad(a)
	A = intercept(a)
	x_pred = (y_pred - A)/b
	return x_pred
	