"""
Title: getjson

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import json
import requests

def getJsonFromURL(url):
        json = requests.get(url)
        data = json.json()
        return data

def getJsonFromFile(location):
        with open(str(location), "r") as file:
                data = file.json()
                return data 
