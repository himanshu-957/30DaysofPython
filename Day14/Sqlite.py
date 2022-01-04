import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("create table info (Name text, Gender text, Place text)")

main_list = [("Himanshu Jadon","Male","Indore" ),
                ("Himanshu Rajore","Male","Akodia"),
                ("Anchal Rathore","Female","Rau"),
                ("Rohit Malviya","Male","Indore"),
                ("Vikas","Male","Indore")]

cursor.executemany("insert into info values (?,?,?)", main_list)
for row in cursor.execute("select * from info"):
    print(row)

#deleting data
cursor.execute("DELETE from info where Name = 'Vikas'")
connection.commit()
print("Record deleted successfully")

for row in cursor.execute("select * from info"):
    print(row)

#updating data
column = ('Vikas Rathore','Male','Indore')
cursor.execute("insert into info values (?,?,?)", column)
connection.commit()
print("Record updated successfully")

for row in cursor.execute("select * from info"):
    print(row)
connection.close()