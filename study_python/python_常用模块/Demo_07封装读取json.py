#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import json
import os
class ReadJson:
    """处理json格式的数据或读取json文件"""
    def __init__(self,jsondata=None,jsonpath = None):
        """传入json数据dict和文件路径，文件路径默认为空"""
        if jsondata is None:
            self._jsondata = None
        else:
            self._jsondata = jsondata
        if jsonpath is None:
            self._jsonpath = None
        else:
            self._jsonpath = jsonpath

    def __file_exist(self):
        """判断文件是否存在"""
        if not self.__fileIsNone():
            return os.path.exists(self._jsonpath)

    def __fileIsNone(self):
        """判断用户是否输入路径"""
        if self._jsonpath is None:
            return True
        else:
            return False
    
    def __r_filedata(self):
        """返回读取到的json数据"""
        if self.__file_exist():
            f = open(self._jsonpath,encoding="utf-8")
            return  json.load(f)

    def find_data(self,datastr):
        """查找对应的数据"""
        listjson = []
        if self.__file_exist():
            self.__dictFind(self.__r_filedata(),datastr,listjson)
            return listjson
        else:
            if not self._jsondata is None:
                self.__dictFind(self._jsondata,datastr,listjson)
            return listjson
    
    def __dictFind(self,dictdata,strdata,listjson):
        """递归查询dict中的strdata数据"""
        if isinstance(dictdata,dict):
            for k,v in dictdata.items():
                if isinstance(v,dict):
                    self.__dictFind(v,strdata,listjson)
                if k == strdata:
                    listjson.append(v)
                    continue
        
path = r"C:\Users\XieQiYo\Desktop\Study\python\task\VerticaCopy\config\config.json"
datajson ={"shr4-vrt-pro-007.houston.hp.com": {"host": "shr4-vrt-pro-007.houston.hp.com",
                                                    "port": 5433,
                                                    "user": "a236a9403b6deee149c04084e50cae48",
                                                    "password": "f728a8d9903a26ad50a770f10a8f1b97",
                                                    "database": "shr4_vrt_pro_007",
                                                    "unicode_error": "strict",
                                                    "ssl": False}}
