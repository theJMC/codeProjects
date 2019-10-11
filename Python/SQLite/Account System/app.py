"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import accounts as a
import cherrypy


class login(object):
    @cherrypy.expose
    def index(self):
        return open("html/index.html")

    @cherrypy.expose
    def table(self, table):
        pass

    @cherrypy.expose
    def login(self, email, password, submit):
        user = db.login(email, password)
        with open("html/success.html") as file:
                data = file.readlines()
                page = ''.join(data)
        if user[1] == 200:
            print("Success! Logged in as: " + user[0])
            tables = db.getTables()[0]
            result = []
            for item in tables:
                result.append(f"<a class='btn btn-primary nav-link' href='table?table={item}'>{str(item).capitalize()}</a><br>")
            print(result)
            return str(page).format(user[0], ''.join(result))
        else:
            print(user)
            return str(page).format("Error! " + str(user[0]) + str(user[1]))
        



if __name__ == "__main__":
    db = a.database("website.db")
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 1337})
    cherrypy.quickstart(login())