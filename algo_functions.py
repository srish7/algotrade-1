import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt 
#Given l and time t, find out the support and resistance by finding out the time points, through which the lines should pass.    
#col is the input vector of time series. 
# The output is a vector m[0,1,2,3] where m[1] is a list containing the time points so that the support line is obtained by joining (m[1][0],col[m[1][0]]) and (m[1][1], col[m[1][1]]). 
# m[0] gives the distance of CG from the support line. 
# Similarly m[2] gives the distance of CG from the resistance line and m[3] gives the resistance line.

#defining function SnR
def SnR(data,t,l):
	cond1=[[0 for x in range(l+1)] for y in range(l+1)]
	cond2=[[0 for x in range(l+1)] for y in range(l+1)]
	J=0
	m=[0 for x in range(4)]
	x=list(data[t-l:t+1])
	print("x = ", x)
	g=[t-0.5*l,sum(x)/(l+1)]
	print("g = ", g)
	m[0]=10**8
	m[2]=10**8
	if l%2==1:
		for i in range(0, math.floor(l/2)+1):
			for j in range(math.floor(l/2)+1,l+1):
				a=np.abs((x[i]-x[j])*g[0]-(i-j)*g[1]+ (x[j]*i-x[i]*j))
				print("a = ", a)
				b=np.sqrt((x[i]-x[j])**2+(i-j)**2)
				print("b = ", b)
				J=a/b
				print("J = ",J)
				C= (x[i]-x[j])/(i-j)
				for k in range (0,l+1):
					if x[k]< x[j]+C*(k-j):
						cond1[i][j]+=1
					elif x[k]== x[j]+C*(k-j):
						cond2[i][j]+=1
				print(cond1[i][j],cond2[i][j])
				if cond1[i][j]==0:
					print(J)
					m[0]=min(m[0],J)
					if m[0]==J:
						m[1]=[i,j]
				elif cond1[i][j]+cond2[i][j]==l:
					print(J)
					m[2]=min(m[2],J)
					if m[2]==J:
						m[3]=[i,j]
	if l%2==0:
		for i in range(0, math.floor(l/2)+1):
			for j in range(math.floor(l/2),l+1):
				if i-j==0:
					cond1[i][j] = 2*l
					cond2[i][j] = 2*l
					continue
				a=np.abs((x[i]-x[j])*g[0]-(i-j)*g[1]+ (x[j]*i-x[i]*j))
				print("a = ", a)
				b=np.sqrt((x[i]-x[j])**2+(i-j)**2)
				print("b = ", b)
				J=a/b
				print("J = ",J)
				C= (x[i]-x[j])/(i-j)
				for k in range (0,l+1):
					if x[k]< x[j]+C*(k-j):
						cond1[i][j]+=1
					elif x[k]== x[j]+C*(k-j):
						cond2[i][j]+=1
				print(cond1[i][j],cond2[i][j])
				if cond1[i][j]==0:
					print(J)
					m[0]=min(m[0],J)
					if m[0]==J:
						m[1]=[i,j]
				elif cond1[i][j]+cond2[i][j]==l:
					print(J)
					m[2]=min(m[2],J)
					if m[2]==J:
						m[3]=[i,j]
	m[1][0]+=t-l
	m[1][1]+=t-l
	m[3][0]+=t-l
	m[3][1]+=t-l
	x1, y1 = m[1],[data[m[1][0]],data[m[1][1]]]
	x2, y2 = m[3],[data[m[3][0]],data[m[3][1]]]
	return [x1,y1,x2,y2]

#defining function to compute delta
def delta(data,t,l,x_sup, y_sup, x_res, y_res):
	x=list(data[t-l:t+1])
	# for calculating delta_plus (based on resistance equation)
	for i in range(t+1, len(data)):
		L_plus = y_res[1] + ((y_res[1]-y_res[0])*(i-x_res[1])/(x_res[1]-x_res[0]))
		if data[i] > L_plus:
			break
	if i >= t+l+1:
		i = min(i,l)
		delta_plus = i
	else:
		delta_plus = i-t-1

	#for calculating delta_minus (based on support equation)
	for j in range(t+1, len(data)):
		L_minus = y_sup[1] + ((y_sup[1]-y_sup[0])*(j-x_sup[1])/(x_sup[1]-x_sup[0]))
		if data[i] < L_minus:
			break
	if j >= t+l+1:
		j = min(j,l)
		delta_minus = l
	else:
		delta_minus = j-t-1
	return [delta_plus,delta_minus]

#defining function to determine the empirical distribution of delta_plus and delta_minus
def emp_delta(delta_plus_list, delta_minus_list): #delta_plus_list and delta_minus_list are arrays containing delta values for t = l, l+1, ... , N
	A = sorted(delta_plus_list)
	B = sorted(delta_minus_list)
	F_delta_plus = [0 for x in range(max(delta_plus_list)+1)]
	F_delta_minus = [0 for x in range(max(delta_minus_list)+1)]
	#empirical distribution of delta_plus
	for k in range(max(delta_plus_list)+1):
		count1 = 0
		for i in range(len(A)):
			if A[i]<= k:
				count1 = count1 +1
			else:
				break
		F_delta_plus[k] = count1/(len(delta_plus_list))
	
	#empirical distribution of delta_minus
	for k in range(max(delta_minus_list)+1):
		count = 0
		for j in range(len(B)):
			if B[j]<= k:
				count = count +1
			else:
				break
		F_delta_minus[k] = count/(len(delta_minus_list))
	return [F_delta_plus, F_delta_minus]

#calling the functions	

data = pd.read_csv('/home/csjoshi/Documents/SemProject/Datasets/bse_c.csv')
y = data['Close']
l = 20
delta_plus = [0 for z in range(l,len(y)-l)]
delta_minus = [0 for z in range(l,len(y)-l)]
for t in range(l+1,len(y)-l):
	print(t)
	[x1,y1,x2,y2] = SnR(y, t, l)
	[a,b] = delta(y,t,l,x1,y1,x2,y2)
	delta_plus[t-20] = a
	delta_minus[t-20] = b

[emp_delta_plus, emp_delta_minus] = emp_delta(delta_plus, delta_minus)
emp_delta_plus = list(np.around(np.array(emp_delta_plus),3))
emp_delta_minus = list(np.around(np.array(emp_delta_minus),3))

print ("Delta_plus = ", delta_plus)
print ("Delta_minus = ", delta_minus)
print ("Empirical distribution of Delta_plus = ", emp_delta_plus)
#print (len(emp_delta_plus))
print ("Empirical distribution of Delta_minus = ", emp_delta_minus)
#print (len(emp_delta_minus))

#plotting the cdf
x = []
for i in range(l+1):
	x.append(i)
plt.plot(x,emp_delta_plus, label = 'for resistance')
plt.plot(x,emp_delta_minus, label = 'for support')
plt.xlabel('x')
plt.ylabel('empirical cdf')
plt.title = 'Graph of empirical cdf of delta values for support and resistance'
plt.xlim(0,l)
plt.ylim(0,1)
plt.legend()
plt.show()
