import sqlite3

connection =sqlite3.connect("fashion.db")
cursor=connection.cursor()

table_txt="CREATE TABLE fashion(USER_ID INT,PRODUCT_ID INT,PRODUCT_NAME VARCHAR(25),BRAND VARCHAR(25),CATEGORY VARCHAR(25),PRICE INT,COLOR VARCHAR(25),SIZE VARCHAR(25))"
cursor.execute(table_txt)

cursor.execute("INSERT INTO fashion VALUES(19,1,'Dress','Adidas','Mens fashion',40,'Black','XL')")
cursor.execute("INSERT INTO fashion VALUES(97,2,'Shoes','H&M','Womens fashion',82,'Black','L')")
cursor.execute("INSERT INTO fashion VALUES(25,3,'Dress','Adidas','Womens fashion',44,'Yellow','XL')")
cursor.execute("INSERT INTO fashion VALUES(57,4,'Shoes','Zara','Mens fashion',23,'White','S')")
cursor.execute("INSERT INTO fashion VALUES(19,1,'Dress','Adidas','Mens fashion',40,'Black','XL')")

data=cursor.execute("SELECT * FROM fashion")
for row in data:
    print(row)

connection.commit()
connection.close()