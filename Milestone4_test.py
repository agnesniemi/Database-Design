

import pymysql

# CONNECTING SO SQL CAN BE USED
mydb = pymysql.connect(
    host='127.0.0.1',
    user='ht23_2_group_48',
    password='pasSWd_48'
)

# WILL INTERPRET YOUR SQL-COMMAND AND GIVE AN ITERABLE WITH THE OBTAINED OBJECTS
mycursor = mydb.cursor ()

mycursor. execute ("SHOW DATABASES")

# THESE SECTIONS ARE FOR DISPLAYING THE OBTAINED OBJECTS GENERATED FROM A SQL COMMAND

for x in mycursor:
    print (x)

mycursor. execute ('USE ht23_2_project_group_48')
mycursor. execute ('SELECT * FROM Department')

for x in mycursor:
    print (x)

# USER CHOOSES DERARTMENT ID (PRIMARY KEY TITLE)
dep_id = input('Choose Department ID: ')

# IF LEAF DEPARTMENT
mycursor. execute (f"SELECT Product_title, (Price_before_tax + Tax_added_to_price + Sale) AS Current_Retail_Price FROM Product WHERE Product_title IN (SELECT Product_title FROM Product WHERE Department_title = '{dep_id}')")

for x in mycursor:
    print (x)

# IF NOT LEAF
'''
mycursor. execute (f'SQL COMMAND')


for x in mycursor:
    print (x)
'''

# USER CHOOSES PRODUCT ID
prod_id = input('Choose Product ID: ')

# FINDS PRODUCT AND SHOWS DISCOUNT

mycursor. execute (f"SELECT Product_title, Sale from Product WHERE Product_title = '{prod_id}'")


for x in mycursor:
    print (x)

change_discount = input("Do you want to change the discount (y/n): ")

if change_discount == "y":
    new_discount = input("Enter new discount: ")
    mycursor. execute (f"UPDATE Product SET Sale = '{new_discount}' WHERE Product_title = '{prod_id}'")
    print(f"Your new discount on product {prod_id} is {new_discount}")

mydb.close()

