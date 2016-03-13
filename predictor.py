import csv

file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/ground_records_2009.csv','r')
k = csv.reader(file , delimiter=',')
arr09_1 = []

for m in k:
	arr09_1.append(m)

file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/t20wins_2009.csv','r')
k = csv.reader(file , delimiter=',')
arr09_2 = []

for m in k:
	arr09_2.append(m)

arr09=[]

for i in range(0,9):
	arr09.append(float(float(arr09_1[i][1])**2) +float(float(arr09_2[i][1])**2))


file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/ground_records_2010.csv' , 'r')
k = csv.reader(file , delimiter=',')
arr10_1 = []

for m in k:
	arr10_1.append(m)

file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/t20wins_2010.csv','r')
k = csv.reader(file , delimiter=',')
arr10_2 = []

for m in k:
	arr10_2.append(m)

arr10=[]

for i in range(0,9):
	arr10.append(float(float(arr10_1[i][1])**2) +float(float(arr10_2[i][1])**2))


file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/ground_records_2012.csv','r')
k = csv.reader(file , delimiter=',')
arr12_1 = []

for m in k:
	arr12_1.append(m)

file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/t20wins_2012.csv' , 'r')
k = csv.reader(file , delimiter=',')
arr12_2 = []

for m in k:
	arr12_2.append(m)

arr12=[]

for i in range(0,9):
	arr12.append(float(float(arr12_1[i][1])**2) +float(float(arr12_2[i][1])**2))

file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/ground_records_2014.csv','r')
k = csv.reader(file , delimiter=',')
arr14_1 = []

for m in k:
	arr14_1.append(m)

file = open('/home/shravan97/Desktop/codes/t20_predictor/datasets/t20wins_2014.csv' , 'r')
k = csv.reader(file , delimiter=',')
arr14_2 = []

for m in k:
	arr14_2.append(m)

arr14=[]

for i in range(0,9):
	arr14.append(float(float(arr14_1[i][1])**2) +float(float(arr14_2[i][1])**2))
	