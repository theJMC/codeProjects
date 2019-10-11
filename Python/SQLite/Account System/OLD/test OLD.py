"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import sqlite3

db = sqlite3.connect("jamesDB.db")
c = db.cursor()
#c.execute('''
#            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
#                                phone TEXT, email TEXT unique, password TEXT)''')
"""
class Person():
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

james = Person("James", "07437 323746", "jamesmccarthy150@gmail.com", "admin")
charlotte = Person("Charlotte", "07845 675238", "15RichardsonC@students.sjl.herts.sch.uk", "12345678")

c.execute('''INSERT INTO users(name, phone, email, password)
            VALUES(?,?,?,?)''', (james.name, james.phone, james.email, james.password))

c.execute('''INSERT INTO users(name, phone, email, password)
            VALUES(?,?,?,?)''', (charlotte.name, charlotte.phone, charlotte.email, charlotte.password))"""

c.execute("SELECT name, email, phone FROM users")
data = c.fetchall()
for row in data:
    print(f"Name: {row[0]} Email: {row[1]} Phone: {row[2]}")

#db.commit()
db.close()