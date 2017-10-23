# -*- coding:utf-8 -*-

import csv
import math
import matplotlib.pyplot as plt

list_rssi1 = [ ]
list_count = [ ]
count = 0
j = 0

#f = open('bus_station.csv','r')
#f = open('bus_jikkenn.csv','r')
#f = open('bus_station2_huzokuanntena.csv','r')
#f = open('LTE_rssi.csv','r')
#f = open('bus_jikkenn3.csv','r')
#f = open('bus_jikkenn.csv','r')
#f = open('rssi_1765_0pe.csv','r')
#f = open('rssi_1770_0pe.csv','r')
#f = open('rssi_1775_0pe.csv','r')
#f = open('rssi_1765_10pe.csv','r')
#f = open('rssi_1770_10pe.csv','r')
#f = open('rssi_1775_10pe.csv','r')
#f = open('rssi_1765_40pe.csv','r')
#f = open('rssi_1770_40pe.csv','r')
#f = open('rssi_1775_40pe.csv','r')
#f = open('rssi_1765_50pe.csv','r')
#f = open('rssi_1770_50pe.csv','r')
f = open('rssi_1775_50pe.csv','r')


reader = csv.reader(f)

for row in reader:
    #list_time.append(row[0])

    del row[0]
    data = list(map(float,row))
    row_ave = sum(data)/len(data)

    list_rssi1.append(float(row_ave))

    #list_rssi1.append(float(row[1]))

#1750_threshold : 7
#1770,1775_threshold : 10

for i in range(len(list_rssi1)):
    list_count.append(i)

    if list_rssi1[i] > 10:
        count = count + 1

print count

plt.plot(list_count,list_rssi1,color="green")
plt.ylabel("RSSI ")
plt.xlabel("count ")
#plt.title("average_5s")

plt.show()
