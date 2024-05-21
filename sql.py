import sqlite3

connection=sqlite3.connect("Student.db")
cursor=connection.cursor()

table_txt="CREATE TABLE Student (NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)"
cursor.execute(table_txt)

cursor.execute("INSERT INTO Student VALUES('arun','genai','a',90)")
cursor.execute("INSERT INTO Student VALUES('sara','nodejs','a',92)")
cursor.execute("INSERT INTO Student VALUES('tej','genai','c',76)")
cursor.execute("INSERT INTO Student VALUES('dev','Reactjs','c',83)")

data=cursor.execute("SELECT * FROM Student")
for row in data:
    print(row)

connection.commit()
connection.close()