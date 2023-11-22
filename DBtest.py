import pymysql
from sshtunnel import SSHTunnelForwarder

tunnel = SSHTunnelForwarder(
    ('fries.it.uu.se', 22),# do not change 22, this is a portal
    ssh_username = 'agni0310', # use your Studium username
    ssh_password = '_k*hrWiaW9', # use your Studium password
    remote_bind_address=('127.0.0.1', 3306)
    ) 

tunnel.start()

mydb = pymysql.connect(
    host='127.0.0.1',
    user='ht23_1_group_50',
    password='pasSWd_50',
    port=tunnel.local_bind_port,
    db = 'ht23_1_project_group_50'
)

mycursor = mydb.cursor ()

mycursor.execute ("SHOW TABLES")

for x in mycursor:
    print (x)

mydb.close()
