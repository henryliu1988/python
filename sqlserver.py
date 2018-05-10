#coding=utf-8


import pymssql
import os
import  urllib.request
from urllib.parse import quote
import  string

conn = pymssql.connect(host='118.190.97.164',
                       user='erp',
                       password='erp2018',
                       database='hqdlerp',
                       charset='GBK')

docstoreurl='http://118.190.97.164:8080/erpdocs/'

path=r'F:\erpfile'    

#查看连接是否成功
cursor = conn.cursor()

sqlGroup = 'select id,name from he_file_group'
cursor.execute(sqlGroup)
groupList = cursor.fetchall()
for group in groupList:
    groupId = group[0]
    groupName = group[1]
    dest_dir = os.path.join(path,groupName)
    print(dest_dir)
    folder = os.path.exists(dest_dir) 
    if not folder:
        os.makedirs(dest_dir) 
    sqlFile = 'select file_name,file_url from he_file_list where group_id=\'%s\'' % (groupId)
    cursor.execute(sqlFile)
    fileList = cursor.fetchall()
    for file in fileList:
       fielName = file[0]
       fileUrl = quote(docstoreurl+file[1],safe = string.printable)
       dest_file=os.path.join(dest_dir,fielName)
       try:
         print('startDownload file %s' % (fileUrl))
         urllib.request.urlretrieve(fileUrl, dest_file)
         print('endDownload file %s' % (fileUrl))

       except:
         print ("fail" + fileUrl)   




