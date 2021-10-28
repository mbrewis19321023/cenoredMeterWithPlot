import os
import sys
from numpy import mod
from openpyxl.styles import NamedStyle, Font, Border, Side
import tkinter as tk
from tkinter import filedialog, Text
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

dateModify = re.compile(r"(\d{2})\-(\d{2})\-\d{2}(\d{2})")


csvFile = open("input.csv")
lines = csvFile.readlines()

print("breakpoint")

column_names = ["Year", "Month", "Day", "startTime", "Load", "Solar"]
df = pd.DataFrame(columns=column_names)
for x, i in enumerate(lines):
    p1 = i.split(";")
    try:
        p3 = p1[0].replace("/","-")
        r2 = re.findall(dateModify,p3)
        o1 = p3.split(" ")
        p1[6] = p1[6].replace(" ","")

        # p2 = p1[4].split("-")
        # p2[0] = p2[0].replace(" ","")
        # p2[0] = int(p2[0][2:])
        # p2[1] = int(p2[1])
        # p2[2] = int(p2[2])


        # p3 = p1[5].split(":")  
        # p3[0] = int(p3[0])
        # p3 = str(p3[0]) + ":" + p3[1] 
        # p3 = p3.replace(" ","")

        tempList = [int(r2[0][2]), int(r2[0][1]), int(r2[0][0]), o1[1], float(p1[6]), 0]
        df.loc[x] = tempList
    except:
        pass
df.to_pickle("./data.pkl")


# # ????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# digitReplace = re.compile(r"(\d+)(,)(\d+)")
# dateModify = re.compile(r"(\d{2})\-(\d{2})\-\d{2}(\d{2})")
# regGroup = re.compile(
#     r"\"\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",")

# monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
#              'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# for x in lines:
#     p1 = x.replace(';', '","')
#     p3 = p1.replace("/", '-')
#     p2 = p3.replace(" ", "")
#     p4 = p2[:10] + " " + p2[11:]
#     r1 = re.findall(dateModify, p4)
#     try:
#         if r1[0][1]:
#             if r1[0][1] == '01':
#                 p5 = re.sub(dateModify, r"\1-Jan-\3", p4)
#             if r1[0][1] == '02':
#                 p5 = re.sub(dateModify, r"\1-Feb-\3", p4)
#             if r1[0][1] == '03':
#                 p5 = re.sub(dateModify, r"\1-Mar-\3", p4)
#             if r1[0][1] == '04':
#                 p5 = re.sub(dateModify, r"\1-Apr-\3", p4)
#             if r1[0][1] == '05':
#                 p5 = re.sub(dateModify, r"\1-May-\3", p4)
#             if r1[0][1] == '06':
#                 p5 = re.sub(dateModify, r"\1-Jun-\3", p4)
#             if r1[0][1] == '07':
#                 p5 = re.sub(dateModify, r"\1-Jul-\3", p4)
#             if r1[0][1] == '08':
#                 p5 = re.sub(dateModify, r"\1-Aug-\3", p4)
#             if r1[0][1] == '09':
#                 p5 = re.sub(dateModify, r"\1-Sep-\3", p4)
#             if r1[0][1] == '10':
#                 p5 = re.sub(dateModify, r"\1-Oct-\3", p4)
#             if r1[0][1] == '11':
#                 p5 = re.sub(dateModify, r"\1-Nov-\3", p4)
#             if r1[0][1] == '12':
#                 p5 = re.sub(dateModify, r"\1-Dec-\3", p4)
#             p6 = p5.replace(" ", '","')
#             supString = '"","'
#             p7 = supString + p6
#             r2 = re.findall(regGroup, p7)
#             temp5 = float(r2[0][2]) * 2
#             r3 = [(r2[0][0], r2[0][1], temp5/1000, float(r2[0][3])/1000,
#                    float(r2[0][4])/1000, float(r2[0][5])*2/1000, float(r2[0][6])/1000, float(r2[0][7])/1000)]
#             p9 = p7[:22] + ',"blank",' + p7[23:]
#             print(r3)
#             p10 = '"","' + str(r3[0][0]) + '","' + str(r3[0][1]) + '","blank' + '","' + str(r3[0][2]) + '","' + str(
#                 r3[0][3]) + '","' + str(r3[0][4]) + '","' + str(r3[0][5]) + '","' + str(r3[0][6]) + '","' + str(r3[0][7]) + '"'
#     except IndexError:
#       print("oops")


# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????