import os
import sys
from numpy import mod
from openpyxl.styles import NamedStyle, Font, Border, Side
import tkinter as tk
from tkinter import Label, filedialog, Text
import tkinter.font as font
from openpyxl.utils.dataframe import dataframe_to_rows
from tkinter.filedialog import asksaveasfile
from openpyxl.styles import Alignment
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.styles import NamedStyle, Font, Border, Side, numbers
import pandas as pd
import pandas as pd
import datetime
from openpyxl import Workbook
from openpyxl.styles import Font
import re
import matplotlib.pyplot as plt

date = []
datetick = 0
load = []
solar = []
test = [1, 2, 3, 4, 5]

df = pd.read_pickle("data.pkl")
dM = df.groupby(['Year', 'Month']).Load.max().reset_index().copy()
dMS = df.groupby(['Year', 'Month']).Solar.max().reset_index().copy()
for x, row in dM.iterrows():
    date.append(str(dM.iloc[x]['Year']) + '-' + str(dM.iloc[x]['Month']))
    load.append(float(dM.iloc[x]['Load']/1000))
    datetick = x
for x, row in dMS.iterrows():
    solar.append(dMS.iloc[x]['Solar'])

for x, i in enumerate(date):
    a = i.split("-")
    if a[1] == '1.0':
        date[x] = "Jan" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '2.0':
        date[x] = "Feb" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '3.0':
        date[x] = "Mar" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '4.0':
        date[x] = "Apr" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '5.0':
        date[x] = "May" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '6.0':
        date[x] = "Jun" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '7.0':
        date[x] = "Jul" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '8.0':
        date[x] = "Aug" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '9.0':
        date[x] = "Sep" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '10.0':
        date[x] = "Oct" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '11.0':
        date[x] = "Nov" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '12.0':
        date[x] = "Dec" + '-' + "20" + str(a[0].split('.')[0])

plt.title("Farm Otjikaru 2ND, Supply Point: 8017 - Max demand")
plt.xticks(rotation='vertical')
plt.xlabel("Date")
plt.ylabel("Demand (kVA)")
plt.plot(date, load, 'bo-', label="Demand", )
# plt.plot(date, solar, 'go-', label="Average Power Factor", )
for i, v in enumerate(load):
    plt.text(i, v + 1, "%.2f" % v, rotation = 90,ha="center", color = "blue")
# for i, v in enumerate(solar):
#     plt.text(i, v, "%d" % v ,rotation = 90, ha="center", color = "green")
plt.ylim(-1, 50)
plt.legend()

plt.show()


# plt.title("Cumulative Solar Energy & Cumulative Consumption for selected months")
# plt.xticks(rotation='vertical')
# plt.xlabel("Date")
# plt.ylabel("Energy Produced/used (kWh)")
# plt.plot(date, load, 'bo-', label="Load", )
# plt.plot(date, solar, 'go-', label="Solar", )
# for i, v in enumerate(load):
#     plt.text(i, v+2000, "%d" % v, rotation = 90,ha="center", color = "blue")
# for i, v in enumerate(solar):
#     plt.text(i, v-6000, "%d" % v,rotation = 90, ha="center", color = "green")
# plt.ylim(-10, 50000)
# plt.legend()

# plt.show()

