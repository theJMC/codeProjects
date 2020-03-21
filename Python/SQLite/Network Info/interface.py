"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import sqlite3

class database():

    def __init__(self, database):
        self.file = database

    def createDB(self):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("CREATE TABLE home(id INTEGER PRIMARY KEY, name TEXT unique, ip_addr TEXT)")
        db.commit()
        db.close()

    def addDevice(self, name, ip_addr):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("INSERT INTO home(name, ip_addr) VALUES(?,?)", (name, ip_addr))
        db.commit()
        db.close()
    
    def getAllDevices(self):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT name, ip_addr FROM home")
        data = c.fetchall()
        print(data)

    def lookupName(self, ip):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT * FROM home WHERE ip_addr = ?", (ip,))
        data = c.fetchone()
        return data[1]
        

    def lookupIP(self, name):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT * FROM home WHERE name = ?", (name,))
        data = c.fetchone()
        return data[2]
