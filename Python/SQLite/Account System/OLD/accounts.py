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
        self.headers = ["id", "name", "phone", "email", "password"]

    def signUp(self, name, phone, email, password):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT * FROM users")
        data = c.fetchall()
        try:
            c.execute('''INSERT INTO users(name, phone, email, password)
                VALUES(?,?,?,?)''', (name, phone, email, password))
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
        c.execute("SELECT email, password FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        if user[1] == password:
            db.commit()
            db.close()
            return user[1], 200

    def getInfo(self, email):
        db = sqlite3.connect(self.file)
        c = db.cursor()
        c.execute("SELECT id, name, phone, email FROM users WHERE email = ?", (email,))
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
