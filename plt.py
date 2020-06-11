import matplotlib.pyplot as plt
import csv 

A=[]
B=[]
#with open('C:\\Users\\anzeq\\Desktop\\python2\\dataX.csv') as csv_file:
with open('C:/Users/anzeq/Desktop/python2/dataX.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        #print(row)
        if not row:
            continue
        if "X" in row[0]:
            continue
        A.append(float(row[0]))
#print(A)

with open('C:/Users/anzeq/Desktop/python2/dataY.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        #print(row)
        if not row:
            continue
        if "Y" in row[0]:
            continue
        B.append(float(row[0]))
#print(B)
plt.plot(A,B)

A1=[]
B1=[]
for i in range (int(len(A)/4)):
    A1.append(A[i])
    B1.append(B[i])

plt.fill_between(A1, B1, 0,
                facecolor="black", # The fill color
                color='black',       # The outline color
                alpha=0.2)          # Transparency of the fill
plt.show()