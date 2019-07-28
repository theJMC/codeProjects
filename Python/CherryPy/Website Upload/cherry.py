"""
Title: Cherry Py Image Upload

Date: 28/07/2019

Author: James McCarthy

Notes:

Todo:

"""
import cherrypy
from columnar import columnar
import time
from Lib.datetime import datetime
import os

class imageServer(object):

    @cherrypy.expose
    def index(self):
        return open("index.html")

    @cherrypy.expose
    def upload(self, image, submit):
        upload_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
        file_extension = os.path.splitext(image.filename)[1]
        img = image.file.read()
        with open("image/" + upload_time + file_extension, "wb+") as file:
            file.write(img)
        with open("upload.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        return str(page).format("<h2>Done!</h2>")

    @cherrypy.expose
    def download(self):
        with open("download.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        os.chdir("image")
        images = os.listdir()
        os.chdir("..")
        results = []
        for item in images:
            results.append(f"<img src=/download/{item} class='img-thumbnail'>")
        # headers = ["Image", "Link"]
        # table = columnar(results, headers)
        return str(page).format("<div class='container'> " + ''.join(results) + "</div>")

if __name__ == "__main__":
    config = {'/download':
    {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': "C:\\Users\\legoj\\Desktop\\Code Workspace\\codeProjects\\Python\\CherryPy\\Website Upload\\image",
    }
}
    cherrypy.quickstart(imageServer(), config=config)