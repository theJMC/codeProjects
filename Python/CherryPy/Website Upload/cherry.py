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
import os.path

class imageServer(object):

    @cherrypy.expose
    def index(self):
        return open("index.html")

    @cherrypy.expose
    def upload(self, image, submit):
        upload_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
        file_extension = os.path.splitext(image.filename)[1]
        # image_path = "C:\\Users\\legoj\\Desktop\\Code Workspace\\codeProjects\\Python\\CherryPy\\Website Upload\\image"
        img = image.file.read()
        with open(upload_time + file_extension, "wb+") as file:
            file.write(img)
        return "Done!"
        # return datetime.now().strftime("%d-%m-%Y_%H:%M:%S:%f")

if __name__ == "__main__":
    cherrypy.quickstart(imageServer())