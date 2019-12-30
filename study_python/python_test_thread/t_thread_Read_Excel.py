#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading
import pandas as pd
import time
import xlrd

excel_file_name = "***"
path = 'C:/Users/XieQiYo/Desktop/MyInformatino/Threadtest.txt'


class MyThread(threading.Thread):
    def __init__(self, target, args=()):  
        super(MyThread, self).__init__()  
        self.target = target  
        self.args = args  
    def run(self):  
        self.result = self.target(*self.args)  # 在执行函数的同时，把结果赋值给result,  
        # 然后通过get_result函数获取返回的结果  
  
    def get_result(self):  
        try:  
            return self.result  
        except Exception as e:  
            return str(e)
def E(excel_file_name):
    print('E我在运行')
    df = pd.read_excel(excel_file_name,dtype=str)
    listdate = []
    id = 0
    while id<2000:
        mapdate = {}
        mapdate.setdefault('Report_Date',df.iloc[id]["Fact_Employee_Hist.Report_Date"]) 
        mapdate.setdefault('Worker_ID',df.iloc[id]["Fact_Employee_Hist.Worker_ID"])
        mapdate.setdefault('Email_Address',df.iloc[id]["Fact_Employee_Hist.Email_Address"])
        mapdate.setdefault('Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Preferred_Name"])
        mapdate.setdefault('Mgr_Hrchy_Level_1_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_1_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_01_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_01_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_2_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_2_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_02_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_02_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_3_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_3_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_03_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_03_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_4_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_4_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_04_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_04_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_5_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_5_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_05_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_05_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_6_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_6_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_06_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_06_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_7_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_7_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_07_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_07_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_8_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_8_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_08_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_08_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_9_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_9_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_09_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_09_Preferred_Name"])	
        mapdate.setdefault('Manager_Hierarchy_Level',df.iloc[id]["Fact_Employee_Hist.Manager_Hierarchy_Level"])	
        mapdate.setdefault('Job_Title',df.iloc[id]["Fact_Employee_Hist.Job_Title"])	
        mapdate.setdefault('Job_Family_Code',df.iloc[id]["Fact_Employee_Hist.Job_Family_Code"])	
        mapdate.setdefault('Job_Code',df.iloc[id]["Fact_Employee_Hist.Job_Code"])	
        mapdate.setdefault('FTE',df.iloc[id]["Fact_Employee_Hist.FTE"])	
        mapdate.setdefault('Job_Category_Code',df.iloc[id]["Fact_Employee_Hist.Job_Category_Code"])	
        mapdate.setdefault('SCS_Code',df.iloc[id]["Fact_Employee_Hist.SCS_Code"])	
        mapdate.setdefault('Worker_Reg_Or_Temp_Code',df.iloc[id]["Fact_Employee_Hist.Worker_Reg_Or_Temp_Code"])	
        mapdate.setdefault('Employee_Type',df.iloc[id]["Fact_Employee_Hist.Employee_Type"])	
        mapdate.setdefault('Job_Level_Type_Code',df.iloc[id]["Fact_Employee_Hist.Job_Level_Type_Code"])	
        mapdate.setdefault('Location_Code',df.iloc[id]["Fact_Employee_Hist.Location_Code"])	
        mapdate.setdefault('Work_Address_Country',df.iloc[id]["Fact_Employee_Hist.Work_Address_Country"])	
        mapdate.setdefault('Workplace_Type_ID',df.iloc[id]["Fact_Employee_Hist.Workplace_Type_ID"])	
        mapdate.setdefault('Workplace_Description',df.iloc[id]["Fact_Employee_Hist.Workplace_Description"])	
        mapdate.setdefault('Supervsor_Level_01_Email',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_01_Email"])	
        mapdate.setdefault('Supervsor_Level_01_Employee_ID',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_01_Employee_ID"])	
        mapdate.setdefault('Supervsor_Level_01_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_01_Preferred_Name"])	
        mapdate.setdefault('Supervsor_Level_02_Email',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_02_Email"])	
        mapdate.setdefault('Supervsor_Level_02_Employee_ID',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_02_Employee_ID"])	
        mapdate.setdefault('Supervsor_Level_02_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_02_Preferred_Name"])	
        mapdate.setdefault('Work_Addres_City',df.iloc[id]["Fact_Employee_Hist.Work_Addres_City"])	
        mapdate.setdefault('Work_Location_Region_Code',df.iloc[id]["Fact_Employee_Hist.Work_Location_Region_Code"])	
        mapdate.setdefault('Location_Name',df.iloc[id]["Fact_Employee_Hist.Location_Name"])	
        mapdate.setdefault('Per_Type_Code',df.iloc[id]["Fact_Employee_Hist.Per_Type_Code"])	
        mapdate.setdefault('Per_Type_Desc',df.iloc[id]["Fact_Employee_Hist.Per_Type_Desc"])	
        mapdate.setdefault('Cost_Center_Name',df.iloc[id]["Fact_Employee_Hist.Cost_Center_Name"])
        mapdate.setdefault('Is_HP',df.iloc[id]["Fact_Employee_Hist.Is_HP"])
        listdate.append(mapdate)
        id = id+1  
    insert = []
    for mapdate in listdate:
        name = "INSERT into App_BM_Graphics_Services_Headcount.Fact_Employee_Hist(Report_Date,Worker_ID,Email_Address,Preferred_Name,Mgr_Hrchy_Level_1_Manager_ID,Management_Chain_Level_01_Preferred_Name,Mgr_Hrchy_Level_2_Manager_ID,Management_Chain_Level_02_Preferred_Name,Mgr_Hrchy_Level_3_Manager_ID,Management_Chain_Level_03_Preferred_Name,Mgr_Hrchy_Level_4_Manager_ID,Management_Chain_Level_04_Preferred_Name,Mgr_Hrchy_Level_5_Manager_ID,Management_Chain_Level_05_Preferred_Name,Mgr_Hrchy_Level_6_Manager_ID,Management_Chain_Level_06_Preferred_Name,Mgr_Hrchy_Level_7_Manager_ID,Management_Chain_Level_07_Preferred_Name,Mgr_Hrchy_Level_8_Manager_ID,Management_Chain_Level_08_Preferred_Name,Mgr_Hrchy_Level_9_Manager_ID,Management_Chain_Level_09_Preferred_Name,Manager_Hierarchy_Level,Job_Title,Job_Family_Code,Job_Code,FTE,Job_Category_Code,SCS_Code,Worker_Reg_Or_Temp_Code,Employee_Type,Job_Level_Type_Code,Location_Code,Work_Address_Country,Workplace_Type_ID,Workplace_Description,Supervsor_Level_01_Email,Supervsor_Level_01_Employee_ID,Supervsor_Level_01_Preferred_Name,Supervsor_Level_02_Email,Supervsor_Level_02_Employee_ID,Supervsor_Level_02_Preferred_Name,Work_Addres_City,Work_Location_Region_Code,Location_Name,Per_Type_Code,Per_Type_Desc,Cost_Center_Name,Is_HP) "
        values = "VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(mapdate.get('Report_Date','null')[:10]	,mapdate.get('Worker_ID','null')	,mapdate.get('Email_Address','null')	,mapdate.get('Preferred_Name','null').replace("'",'’')	,mapdate.get('Mgr_Hrchy_Level_1_Manager_ID','null')	,mapdate.get('Management_Chain_Level_01_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_2_Manager_ID','null')	,mapdate.get('Management_Chain_Level_02_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_3_Manager_ID','null')	,mapdate.get('Management_Chain_Level_03_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_4_Manager_ID','null')	,mapdate.get('Management_Chain_Level_04_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_5_Manager_ID','null')	,mapdate.get('Management_Chain_Level_05_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_6_Manager_ID','null')	,mapdate.get('Management_Chain_Level_06_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_7_Manager_ID','null')	,mapdate.get('Management_Chain_Level_07_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_8_Manager_ID','null')	,mapdate.get('Management_Chain_Level_08_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_9_Manager_ID','null')	,mapdate.get('Management_Chain_Level_09_Preferred_Name','null')	,mapdate.get('Manager_Hierarchy_Level','null')	,mapdate.get('Job_Title','null')	,mapdate.get('Job_Family_Code','null')	,mapdate.get('Job_Code','null')	,mapdate.get('FTE','null')	,mapdate.get('Job_Category_Code','null')	,mapdate.get('SCS_Code','null')	,mapdate.get('Worker_Reg_Or_Temp_Code','null')	,mapdate.get('Employee_Type','null')	,mapdate.get('Job_Level_Type_Code','null')	,mapdate.get('Location_Code','null')	,mapdate.get('Work_Address_Country','null')	,mapdate.get('Workplace_Type_ID','null').split('-')[0].strip()	,mapdate.get('Workplace_Type_ID','null')	,mapdate.get('Workplace_Description','null')	,mapdate.get('Supervsor_Level_01_Email','null')	,mapdate.get('Supervsor_Level_01_Employee_ID','null')	,mapdate.get('Supervsor_Level_01_Preferred_Name','null')	,mapdate.get('Supervsor_Level_02_Email','null')	,mapdate.get('Supervsor_Level_02_Employee_ID','null')	,mapdate.get('Work_Addres_City','null')	,mapdate.get('Work_Location_Region_Code','null')	,mapdate.get('Location_Name','null')	,mapdate.get('Per_Type_Code','null')	,mapdate.get('Per_Type_Desc','null')	,mapdate.get('Cost_Center_Name','null')	,mapdate.get('Is_HP'))
        insert.append(name+values)
    return insert


def Et(excel_file_name):
    print('Et我在运行')
    df = pd.read_excel(excel_file_name,dtype=str)
    listdate = []
    id = 2000
    while id<5533:
        mapdate = {}
        mapdate.setdefault('Report_Date',df.iloc[id]["Fact_Employee_Hist.Report_Date"]) 
        mapdate.setdefault('Worker_ID',df.iloc[id]["Fact_Employee_Hist.Worker_ID"])
        mapdate.setdefault('Email_Address',df.iloc[id]["Fact_Employee_Hist.Email_Address"])
        mapdate.setdefault('Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Preferred_Name"])
        mapdate.setdefault('Mgr_Hrchy_Level_1_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_1_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_01_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_01_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_2_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_2_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_02_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_02_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_3_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_3_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_03_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_03_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_4_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_4_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_04_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_04_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_5_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_5_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_05_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_05_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_6_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_6_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_06_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_06_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_7_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_7_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_07_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_07_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_8_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_8_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_08_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_08_Preferred_Name"])	
        mapdate.setdefault('Mgr_Hrchy_Level_9_Manager_ID',df.iloc[id]["Fact_Employee_Hist.Mgr_Hrchy_Level_9_Manager_ID"])	
        mapdate.setdefault('Management_Chain_Level_09_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Management_Chain_Level_09_Preferred_Name"])	
        mapdate.setdefault('Manager_Hierarchy_Level',df.iloc[id]["Fact_Employee_Hist.Manager_Hierarchy_Level"])	
        mapdate.setdefault('Job_Title',df.iloc[id]["Fact_Employee_Hist.Job_Title"])	
        mapdate.setdefault('Job_Family_Code',df.iloc[id]["Fact_Employee_Hist.Job_Family_Code"])	
        mapdate.setdefault('Job_Code',df.iloc[id]["Fact_Employee_Hist.Job_Code"])	
        mapdate.setdefault('FTE',df.iloc[id]["Fact_Employee_Hist.FTE"])	
        mapdate.setdefault('Job_Category_Code',df.iloc[id]["Fact_Employee_Hist.Job_Category_Code"])	
        mapdate.setdefault('SCS_Code',df.iloc[id]["Fact_Employee_Hist.SCS_Code"])	
        mapdate.setdefault('Worker_Reg_Or_Temp_Code',df.iloc[id]["Fact_Employee_Hist.Worker_Reg_Or_Temp_Code"])	
        mapdate.setdefault('Employee_Type',df.iloc[id]["Fact_Employee_Hist.Employee_Type"])	
        mapdate.setdefault('Job_Level_Type_Code',df.iloc[id]["Fact_Employee_Hist.Job_Level_Type_Code"])	
        mapdate.setdefault('Location_Code',df.iloc[id]["Fact_Employee_Hist.Location_Code"])	
        mapdate.setdefault('Work_Address_Country',df.iloc[id]["Fact_Employee_Hist.Work_Address_Country"])	
        mapdate.setdefault('Workplace_Type_ID',df.iloc[id]["Fact_Employee_Hist.Workplace_Type_ID"])	
        mapdate.setdefault('Workplace_Description',df.iloc[id]["Fact_Employee_Hist.Workplace_Description"])	
        mapdate.setdefault('Supervsor_Level_01_Email',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_01_Email"])	
        mapdate.setdefault('Supervsor_Level_01_Employee_ID',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_01_Employee_ID"])	
        mapdate.setdefault('Supervsor_Level_01_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_01_Preferred_Name"])	
        mapdate.setdefault('Supervsor_Level_02_Email',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_02_Email"])	
        mapdate.setdefault('Supervsor_Level_02_Employee_ID',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_02_Employee_ID"])	
        mapdate.setdefault('Supervsor_Level_02_Preferred_Name',df.iloc[id]["Fact_Employee_Hist.Supervsor_Level_02_Preferred_Name"])	
        mapdate.setdefault('Work_Addres_City',df.iloc[id]["Fact_Employee_Hist.Work_Addres_City"])	
        mapdate.setdefault('Work_Location_Region_Code',df.iloc[id]["Fact_Employee_Hist.Work_Location_Region_Code"])	
        mapdate.setdefault('Location_Name',df.iloc[id]["Fact_Employee_Hist.Location_Name"])	
        mapdate.setdefault('Per_Type_Code',df.iloc[id]["Fact_Employee_Hist.Per_Type_Code"])	
        mapdate.setdefault('Per_Type_Desc',df.iloc[id]["Fact_Employee_Hist.Per_Type_Desc"])	
        mapdate.setdefault('Cost_Center_Name',df.iloc[id]["Fact_Employee_Hist.Cost_Center_Name"])
        mapdate.setdefault('Is_HP',df.iloc[id]["Fact_Employee_Hist.Is_HP"])
        listdate.append(mapdate)
        id = id+1
    insert = []
    for mapdate in listdate:
        name = "INSERT into App_BM_Graphics_Services_Headcount.Fact_Employee_Hist(Report_Date,Worker_ID,Email_Address,Preferred_Name,Mgr_Hrchy_Level_1_Manager_ID,Management_Chain_Level_01_Preferred_Name,Mgr_Hrchy_Level_2_Manager_ID,Management_Chain_Level_02_Preferred_Name,Mgr_Hrchy_Level_3_Manager_ID,Management_Chain_Level_03_Preferred_Name,Mgr_Hrchy_Level_4_Manager_ID,Management_Chain_Level_04_Preferred_Name,Mgr_Hrchy_Level_5_Manager_ID,Management_Chain_Level_05_Preferred_Name,Mgr_Hrchy_Level_6_Manager_ID,Management_Chain_Level_06_Preferred_Name,Mgr_Hrchy_Level_7_Manager_ID,Management_Chain_Level_07_Preferred_Name,Mgr_Hrchy_Level_8_Manager_ID,Management_Chain_Level_08_Preferred_Name,Mgr_Hrchy_Level_9_Manager_ID,Management_Chain_Level_09_Preferred_Name,Manager_Hierarchy_Level,Job_Title,Job_Family_Code,Job_Code,FTE,Job_Category_Code,SCS_Code,Worker_Reg_Or_Temp_Code,Employee_Type,Job_Level_Type_Code,Location_Code,Work_Address_Country,Workplace_Type_ID,Workplace_Description,Supervsor_Level_01_Email,Supervsor_Level_01_Employee_ID,Supervsor_Level_01_Preferred_Name,Supervsor_Level_02_Email,Supervsor_Level_02_Employee_ID,Supervsor_Level_02_Preferred_Name,Work_Addres_City,Work_Location_Region_Code,Location_Name,Per_Type_Code,Per_Type_Desc,Cost_Center_Name,Is_HP) "
        values = "VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(mapdate.get('Report_Date','null')[:10]	,mapdate.get('Worker_ID','null')	,mapdate.get('Email_Address','null')	,mapdate.get('Preferred_Name','null').replace("'",'’')	,mapdate.get('Mgr_Hrchy_Level_1_Manager_ID','null')	,mapdate.get('Management_Chain_Level_01_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_2_Manager_ID','null')	,mapdate.get('Management_Chain_Level_02_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_3_Manager_ID','null')	,mapdate.get('Management_Chain_Level_03_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_4_Manager_ID','null')	,mapdate.get('Management_Chain_Level_04_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_5_Manager_ID','null')	,mapdate.get('Management_Chain_Level_05_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_6_Manager_ID','null')	,mapdate.get('Management_Chain_Level_06_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_7_Manager_ID','null')	,mapdate.get('Management_Chain_Level_07_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_8_Manager_ID','null')	,mapdate.get('Management_Chain_Level_08_Preferred_Name','null')	,mapdate.get('Mgr_Hrchy_Level_9_Manager_ID','null')	,mapdate.get('Management_Chain_Level_09_Preferred_Name','null')	,mapdate.get('Manager_Hierarchy_Level','null')	,mapdate.get('Job_Title','null')	,mapdate.get('Job_Family_Code','null')	,mapdate.get('Job_Code','null')	,mapdate.get('FTE','null')	,mapdate.get('Job_Category_Code','null')	,mapdate.get('SCS_Code','null')	,mapdate.get('Worker_Reg_Or_Temp_Code','null')	,mapdate.get('Employee_Type','null')	,mapdate.get('Job_Level_Type_Code','null')	,mapdate.get('Location_Code','null')	,mapdate.get('Work_Address_Country','null')	,mapdate.get('Workplace_Type_ID','null').split('-')[0].strip()	,mapdate.get('Workplace_Type_ID','null')	,mapdate.get('Workplace_Description','null')	,mapdate.get('Supervsor_Level_01_Email','null')	,mapdate.get('Supervsor_Level_01_Employee_ID','null')	,mapdate.get('Supervsor_Level_01_Preferred_Name','null')	,mapdate.get('Supervsor_Level_02_Email','null')	,mapdate.get('Supervsor_Level_02_Employee_ID','null')	,mapdate.get('Work_Addres_City','null')	,mapdate.get('Work_Location_Region_Code','null')	,mapdate.get('Location_Name','null')	,mapdate.get('Per_Type_Code','null')	,mapdate.get('Per_Type_Desc','null')	,mapdate.get('Cost_Center_Name','null')	,mapdate.get('Is_HP'))
        insert.append(name+values)
    return insert

def isture():
    print('isture我在运行')
    return True

def testThread():
    result = []
    thread = []
    print('开始计算时间')
    start = time.time()
    # t1 = MyThread(target=E,args=(excel_file_name,))
    # t2 = MyThread(target=Et,args=(excel_file_name,))
    # thread.append(t1)
    # thread.append(t2)
    # t1.start()
    # t2.start()

    # t1.join()
    # result.append(t1.get_result())
    result.append(E(excel_file_name))
    # t2.join()
    result.append(Et(excel_file_name))
    # result.append(t2.get_result())
    max = 0
    for i in result:
        for c in i:
            with open(path,'ab')as r:
                r.write(('------------'+(str(max))).encode('utf-8'))
                r.write(b'\r\n')
                r.write(c.encode('utf-8'))
                r.write(b'\r\n')
                print(max)
                max = max+1
    end = time.time()
    print('运行时间',end-start)#1、98  2、85 #1、64  2、65


def common():
    print('common runing')
    start = time.time()
    listdate = []
    listdate.append(E(excel_file_name))
    listdate.append(Et(excel_file_name))
    max = 0
    for i in listdate:
        for c in i:
            with open(path,'ab')as r:
                r.write(('------------'+(str(max))).encode('utf-8'))
                r.write(b'\r\n')
                r.write(c.encode('utf-8'))
                r.write(b'\r\n')
                print(max)
                max = max+1
    end = time.time()
    print('运行时间',end-start)#79、
testThread()
# common()




