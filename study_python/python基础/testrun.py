import vertica_python
import logging
import smtplib
import pandas as pd
import time
from datetime import datetime
import xlrd
import parame
excel_file_name = r'C:\Users\XieQiYo\Desktop\MyInformatino\EXCEL\Copy of Copy of Copy of Fact_Employee_Hist v3 _ Country Code_FINAL.xlsx'




df = pd.read_excel(excel_file_name,dtype=str)
book = xlrd.open_workbook(excel_file_name)
#获取第一个
sheet1 = book.sheets()[0]
#获取行和列的总数
nrows = sheet1.nrows
ncols = sheet1.ncols
print(df.iloc[0]['Fact_Employee_Hist.Report_Date'])






# date = sheet1.cell(1,0).value
# print(type(date))
# print(datetime.fromtimestamp(date))
# 

# print('表格总行数',nrows)



# print('表格总列数',ncols)
# print(sheet1.cell(30,3).value)
