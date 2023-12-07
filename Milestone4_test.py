

import pymysql
mydb = pymysql.connect(
    host='127.0.0.1',
    user='ht23_2_group_48',
    password='pasSWd_48'
)

mycursor = mydb.cursor ()

mycursor. execute ("SHOW DATABASES")

for x in mycursor:
    print (x)

mycursor. execute ("USE ht23_2_project_group_48")
mycursor. execute ("SELECT * FROM Department")

for x in mycursor:
    print (x)


dep_id = input('Choose Department ID: ')

# IF LEAF DEPARTMENT
mycursor. execute (f"SELECT Product_title, (Price_before_tax + Tax_added_to_price + Sale) AS Current_Retail_Price FROM Product WHERE Product_title IN (SELECT Product_title FROM Product WHERE Department_title = '{dep_id}')")

for x in mycursor:
    print (x)

mydb.close()

