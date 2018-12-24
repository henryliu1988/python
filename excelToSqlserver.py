# -*- coding: utf-8 -*-

import xlrd
from datetime import date,datetime
import pymssql
import os
import  urllib.request
from urllib.parse import quote
import  string
import uuid


examIdList = []
#所属列 分别 userid,name,phone,cate_id,cate_name,company_name,idcard,exam_num,score1,score2,score3,score4
filelist = {'2018吕梁市安全技术培训中心安全生产管理人员危险化学品经营单位初训4期':[' ',1,11,'0002','安全管理人员',10,5,3,6,7,8,9],
'2018吕梁市安全技术培训中心安全生产管理人员危险化学品生产单位初训3期':[' ',1,11,'0002','安全管理人员',10,5,3,6,7,8,9],
'2018吕梁市安全技术培训中心安全生产管理人员危险化学品生产单位初训4期':[' ',1,11,'0002','安全管理人员',10,5,3,6,7,8,9],
'2018吕梁市安全技术培训中心特种作业人员电工作业低压电工作业初训5期':[' ',1,'','0003','特种作业人员',8,3,'',4,5,6,7],
'2018吕梁市安全技术培训中心特种作业人员焊接与热切割作业熔化焊接与热切割作业初训4期':[' ',1,10,'0003','特种作业人员',9,4,3,5,6,7,8],
'2018吕梁市安全技术培训中心特种作业人员焊接与热切割作业熔化焊接与热切割作业复训4期':[' ',1,10,'0003','特种作业人员',9,4,3,5,6,7,8],
'2018吕梁市安全技术培训中心特种作业人员冶金（有色）生产安全作业煤气作业初训5期':[' ',1,9,'0003','特种作业人员',8,3,'',4,5,6,7],
'2018吕梁市安全技术培训中心特种作业人员冶金（有色）生产安全作业煤气作业初训7期':[' ',1,10,'0003','特种作业人员',9,4,3,5,6,7,8],
'2018吕梁市安全技术培训中心主要负责人危险化学品经营单位初训4期':[' ',1,11,'0001','主要负责人',10,5,3,6,7,8,9]}


conn = pymssql.connect(host='47.105.181.34',
                       user='spcsis',
                       password='spcsis2017',
                       database='spcsis',
                       charset='GBK')
cursor = conn.cursor() # 获取光标
#examId='0001'
#categoryId = '0002'
#categoryName='安全管理人员'

inserlist = []
#colIndex = ['001',' ',1,11,categoryId,categoryName,10,5,3,6,7,8,9]
def loadExam():
    cursor.execute('select  e.id,p.class_name name from sp_educate_exam e LEFT JOIN sp_educate_train_plan  p on e.plan_id=p.id')
    examIdList = cursor.fetchall()
    for exam in examIdList:
        read_excel(exam)

def read_excel(exam):
    #获取目标EXCEL文件sheet名
    colIndex = filelist[exam[1]]
    colIndex.insert(0,exam[0])
    print(colIndex)
    ExcelFile=xlrd.open_workbook(exam[1] + '.xls')
    sheet=ExcelFile.sheet_by_index(0)
    row=3
    while row < sheet.nrows:
        datalist=[]
        for col in colIndex:
            if isinstance(col,int):
                if isinstance(sheet.cell_value(row,col),str) :
                    datalist.append("'" + sheet.cell_value(row,col) + "'")
                else:
                    datalist.append("'" + str(sheet.cell_value(row,col)) + "'")
            else:
                datalist.append("'" +col+ "'")
        insertsql = "INSERT INTO sp_educate_exam_result VALUES (" + ','.join(datalist)  + ")"
        print(insertsql)
        cursor.execute(insertsql)
        conn.commit()
        inserlist.append(insertsql)
        row = row+1


loadExam()
    
