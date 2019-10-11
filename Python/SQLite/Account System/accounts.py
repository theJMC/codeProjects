"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import sqlite3

class database():

    def __init__(self, fileName):
        self.file = fileName
        self.headers = ["id", "name", "email", "password"]

    def setupTable(self):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT unique, password TEXT)')
        return "Success", 200

    def signUp(self, name, email, password):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT * FROM users")
        data = c.fetchall()
        try:
            c.execute('''INSERT INTO users(name, email, password)
                VALUES(?,?,?,?)''', (name, email, password))
        except sqlite3.IntegrityError:
            return "Email already exists", 409
        finally:
            db.commit()
            db.close()
        return "User Created", 201

    def getUsers(self):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT * FROM users")
        data = c.fetchall()
        users = []
        for item in data:
            users.append(item[3])
        db.commit()
        db.close()
        return users, 200

    def login(self, email, password):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT name, email, password FROM users WHERE email = ?", (str(email).lower(),))
        user = c.fetchone()
        try:
            if user[2] == password:
                db.commit()
                db.close()
                return user[0], 200
            else:
                db.commit()
                db.close()
                return "User Not Found", 404
        except TypeError as e:
            return "User Not Found 2", 4042

    def getInfo(self, email):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT id, name, email FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        db.commit()
        db.close()
        return user, 200

    def updateUser(self, email, item, value):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        if item == 3 or item == 0:
            return "Unable to change Email or ID", 403
        c.execute(f"UPDATE users SET {self.headers[item]} = ? WHERE email = ?", (value, email))
        db.commit()
        db.close()
        return "Done", 200

    def getTables(self):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'")
        raw_tables = c.fetchall()
        tables = []
        for item in raw_tables:
            tables.append(item[0])
        return tables, 200
