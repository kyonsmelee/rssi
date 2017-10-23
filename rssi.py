# -*- coding:utf-8 -*-

import csv
import math
import matplotlib.pyplot as plt

#list_time = [ ]
list_rssi1 = [ ]
list_count = [ ]

#f = open('bus_station.csv','r')
#f = open('bus_station2_LTEanntena.csv','r')
#f = open('bus_station2_huzokuanntena.csv','r')
#f = open('LTE_rssi.csv','r')
#f = open('rouka3_jikkenn.csv','r')
#f = open('bus_jikkenn.csv','r')
#f = open('bus_jikkenn2.csv','rU')
#f = open('bus_jikkenn3.csv','r')
#f = open('rssi_2M_1770-1772.csv','r')
#f = open('rssi_2M_1775-1777.csv','r')
#f = open('rssi_1765_0pe.csv','r')
f = open('rssi_1770_0pe.csv','r')
#f = open('rssi_1775_0pe.csv','r')
#f = open('rssi_1765_10pe.csv','r')
#f = open('rssi_1770_10pe.csv','r')
#f = open('rssi_1775_10pe.csv','r')
#f = open('rssi_1765_40pe.csv','r')
#f = open('rssi_1770_40pe.csv','r')
#f = open('rssi_1775_40pe.csv','r')
#f = open('rssi_1765_50pe.csv','r')
#f = open('rssi_1770_50pe.csv','r')
#f = open('rssi_1775_50pe.csv','r')
#f = open('rssi_1775_1day.csv','r')
#f = open('rssi_1770_box.csv','r')
#f = open('rssi_1770_nobox.csv','r')
#f = open('rssi_softbank.csv','r')
#f = open('rssi_au.csv','r')
#f = open('rssi_docomo_LAB.csv','r')
#f = open('rssi_au_LAB.csv','r')
#f = open('rssi_softbank_LAB.csv','r')
#f = open('rssi_docomo_15pe.csv','r')
#f = open('rssi_softbank_15pe.csv','r')
#f = open('rssi_au_15pe.csv','r')
#f = open('rssi_softbank_10pe.csv','r')
#f = open('rssi_au_10pe.csv','r')
#f = open('rssi_docomo_50pe.csv','r')
#f = open('rssi_softbank_50pe.csv','r')
f = open('rssi_au_50pe.csv','r')

reader = csv.reader(f)

for row in reader:
    #list_time.append(row[0])
    del row[0]
    #del row[-1]
    data = list(map(float,row))
    row_ave = sum(data)/len(data)

    #list_rssi1.append(float(row_ave))
    list_rssi1.append(float(row[0]))

'''
for i in range(len(list_rssi1[300*10-60:300*10+60])):
    list_count.append(i)
'''

for i in range(len(list_rssi1)):
    list_count.append(i)

print len(list_count)

plt.plot(list_count,list_rssi1,color="green")
plt.ylabel("RSSI ")
plt.xlabel("count ")
#plt.title("average_5s")

'''
max_num = max(list_rssi1[300*10-60:300*10+60])
min_num = min(list_rssi1[300*10-60:300*10+60])

num = max_num-min_num
print num
num = math.floor(max_num-min_num)

max = max(list_rssi1)
min = min(list_rssi1)
num = max - min

plt.hist(list_rssi1,bins=num,color="red")
'''

#plt.hist(list_rssi1[300*10-60:300*10+60],bins = num,color="red",normed=True,rwidth=1)
#plt.xlim(0,50)

plt.show()
