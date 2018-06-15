import MySQLdb

db_config = {
    'host' : '192.168.189.100',    #填写主机名(string)
    'user' : 'root',               #填写登录用户(string)
    'passwd' : 'XXXXXX',           #填写登录密码(string)
    'db' : 'test',                 #选择数据库(string)
    'port' : 3306,                #填写端口(int)
    'charset':'utf-8'              #设定字符集
}

try:
    conn = MySQLdb.connect(**db_config)
except Exception as e:
    raise e
finally:
    print ("mysql 连接成功！")
