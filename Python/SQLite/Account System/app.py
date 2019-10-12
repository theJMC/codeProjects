"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import accounts as a
import cherrypy

database = "website.db"

class login(object):
    @cherrypy.expose
    def index(self):
        return open("html/index.html")

    @cherrypy.expose
    def home(self):
        tables = db.getTables()[0]
        result = []
        with open("html/success.html") as file:
                data = file.readlines()
                page = ''.join(data)
        for item in tables:
            result.append(f"<tr><td>{str(item).capitalize()}</td><td><a class='btn btn-primary' href='table?table={item}'>Go</a></td>")
        return str(page).format(''.join(result))

    @cherrypy.expose
    def table(self, table):
        with open("html/table.html") as file:
            data = file.readlines()
            page = ''.join(data)
        data = db.getAllFromTable(table)[0]
        headers = db.getHeaders(table)[0]
        result = []
        result.append("<thead><tr>")
        for item in headers:
            result.append(f"<th scope='col'>{item[1]}</th>")
        result.append("</thead><tbody>")
        for row in data:
            result.append("<tr>")
            for item in row:
                result.append(f"<td>{item}</td>")
            result.append("</tr>")
        return str(page).format(str(table.capitalize()), ''.join(result))


    @cherrypy.expose
    def login(self, email, password, submit):
        user = db.login(email, password)
        with open("html/success.html") as file:
                data = file.readlines()
                page = ''.join(data)
        if user[1] == 200:
            raise cherrypy.HTTPRedirect("/home")
        else:
            return str(page).format("Error! " + str(user[0]) + str(user[1]))
        



if __name__ == "__main__":
    db = a.database(database)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 1337})
    cherrypy.quickstart(login())