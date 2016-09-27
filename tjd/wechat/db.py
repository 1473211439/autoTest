#-*-coding:utf-8-*-
import MySQLdb,cPickle

#连接到数据库，并获得图标
connection = MySQLdb.connect(user = 'root',db='zm',passwd = '36039975',host='localhost')
cursor = connection.cursor()

#创建一个新表以用于试验
cursor.execute('create table test(name TEXT, ablob BLOB)')

try:
    #准备一些BLOB用于测试
    names = 'aramis', 'athos','porthos'
    data = { }

    for name in names:
        datum = list(name)
        datum.sort()
        data[name] = cPickle.dumps(datum,2)
    #execute insert
    sql = "insert into test values(%s, %s)"
    for name in names:
        cursor.execute(sql,(name,MySQLdb.escape_string(data[name])))
    #check in the database
    sql = "select name, ablob from test order by name"
    cursor.execute(sql)
    for name , blob in cursor.fetchall():
        print name, cPickle.loads(blob), cPickle.loads(data[name])

finally:
    #finish,delete table and close connection
    cursor.execute("drop table test")
    cursor.close()
    connection.close()