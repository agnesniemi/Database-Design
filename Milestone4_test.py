import pymysql

mydb = pymysql.connect(
    host='127.0.0.1',
    user='ht23_1_group_48',
    password='pasSWd_48'
)

mycursor = mydb.cursor ()

mycursor. execute ("SHOW DATABASES")

for x in mycursor:
    print (x)

mydb.close()

