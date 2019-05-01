"""
Title: getjson

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import json
import requests

def getJson(url):
    json = requests.get(url)
    data = json.json()
    return data