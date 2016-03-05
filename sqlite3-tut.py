# python 3
# SQLite3 demo

import sqlite3

# if tut.db donot exists , will be created
conn=sqlite3.connect('tut.db')
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS student(name TEXT,marks INTEGER)")

def data_entry(name,marks):
    c.execute("INSERT INTO student VALUES (?,?) ",(name,marks))
    conn.commit()

def read_db():
    c.execute("SELECT * FROM student")
    #data=c.fetchall()  # fetchone() to fetch single row
    #print(data)

    for data in c.fetchall():
        print(data)

create_table()

names=['A','B','C','D','E','F','G','H','I','J']
marks=[10,20,30,50,80,60,70,60,80,88]

for i in range(10):
    data_entry(names[i],marks[i])

read_db()
conn.close()
