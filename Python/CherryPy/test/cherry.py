"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import cherrypy
from columnar import columnar
import Lib.random as random
import Lib.string as string

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return open("index.html")

    @cherrypy.expose
    def generate(self, length=8):
        with open("result.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        return str(page).format(''.join(random.sample(string.hexdigits, int(length))))
        # return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == "__main__":
    cherrypy.quickstart(HelloWorld())