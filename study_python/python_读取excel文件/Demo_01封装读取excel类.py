#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xlrd
import pandas as pd
import os

class Read_Excel:
    """读取excel"""
    def __init__(self,path):
        """excel路径"""
        self._path = path
        if os.path.exists(path):
            self._df = pd.read_excel(path,dtype=str)
            self._book = xlrd.open_workbook(path)
        else:
            print("路径不存在")
    def _get_Value(self,col,row):
        """获取某一个单元格"""
        sheet1 = self._book.sheets()[0]
        return sheet1.cell(row,col).value
  
    def _get_colls_values(self,col):
        """
        获取这整列列信息
        col:要获取的列名(str)或者第几列(int)
        """
        values = []
        if isinstance(col,str):
            return self._df[col]
        elif isinstance(col,int):
            sheet1 = self._book.sheets()[0]
            colvals = sheet1.cell(0,col).value
            rowslen = sheet1.nrows
            for row in range(rowslen-1):
                values.append(self._df.iloc[row][colvals])
            return values  

    def _get_row_values(self,row):
        """获取这行信息"""
        return self._df.iloc[row]
 
    def _get_col_names(self):
        """获取每列的名字"""
        sheet1 = self._book.sheets()[0]
        ncols = sheet1.ncols
        colslist = []
        for col in range(ncols):
            colslist.append(sheet1.cell(0,col).value)
        return colslist
 
    def _Rall(self):
        """读取全部的数据"""
        #获取第一个
        sheet1 = self._book.sheets()[0]
        #获取行和列的总数
        nrows = sheet1.nrows
        ncols = sheet1.ncols
        colslist = []
        datalist = []
        column = []
        #通过先获取第一行的每一列，在根据每一列，获取值
        #获取列名
        for col in range(ncols):
            colslist.append(sheet1.cell(0,col).value)
        #获取每列的值用dict存储在放到list
        for row in range(nrows-1):
            rowmap = {}
            for col in colslist:
                rowmap.setdefault(col,self._df.iloc[row][col])
            datalist.append(rowmap)
        return datalist

        """后续记得优化为是用切片的方式来获取数据更加简洁方便"""
    
    def _Rspcify_Values(self,start,end):
        """读取指定区域的内容"""
        sheet1 = self._book.sheets()[0]
        #获取行和列的总数
        ncols = sheet1.ncols
        colslist = []
        datalist = []
        column = []
        #通过先获取第一行的每一列，在根据每一列，获取值
        #获取列名
        for col in range(ncols):
            colslist.append(sheet1.cell(0,col).value)
        #获取每列的值用dict存储在放到list
        for row in range(start-2,end-1):
            rowmap = {}
            for col in colslist:
                rowmap.setdefault(col,self._df.iloc[row][col])
            datalist.append(rowmap)
        return datalist

    def __getitem__(self,n):
        """使用切片的方式来"""
        #如果是切片
        if isinstance(n,slice):
            start = n.start
            end = n.stop
            sheet1 = self._book.sheets()[0]
            #获取行和列的总数
            ncols = sheet1.ncols
            nrows = sheet1.nrows
            colslist = []
            datalist = []
            column = []
            if start is None:
                start = 0
            if end is None:
                end = nrows
            #通过先获取第一行的每一列，在根据每一列，获取值
            #获取列名
            for col in range(ncols):
                colslist.append(sheet1.cell(0,col).value)
            #获取每列的值用dict存储在放到list
            for row in range(start,end-1):
                rowmap = {}
                for col in colslist:
                    rowmap.setdefault(col,self._df.iloc[row][col])
                datalist.append(rowmap)
            return datalist

#测试
excel = Read_Excel(path="")
print(excel[0:4])#ok
print(excel[:])#ok
print(excel[:3],'excel[:3]')#ok









