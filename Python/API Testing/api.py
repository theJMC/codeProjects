"""
Title: Phillips Hue API

Date: 22/04/2019

Author: James McCarthy

Notes:

Todo:

"""
import reference as ref
import json
import urllib.request
import requests

api_key = "qlSEH3JH8d7nin2DSQ2aphmBu-mhsqBQ3yoyTvqg"

url = "http://192.168.0.25/api/" + api_key

lights_json = requests.get(url + "/lights")
rooms_json = requests.get(url + "/groups")

data_lights = lights_json.json()
data_rooms = rooms_json.json()

# for i in range(1, len(data_lights)):
#     print(data_lights[str(i)]["name"] + " -- " + str(data_lights[str(i)]["state"]["on"]))


def viewState(target):
    print("\n")
    if target == "all":
        for i in range(1, len(data_rooms)):
            if data_rooms[str(i)]["type"] == "Room":    
                print(data_rooms[str(i)]["name"] + ": ")
                for light_identifier in data_rooms[str(i)]["lights"]:
                    state = "On" if data_lights[light_identifier]["state"]["on"] else "Off"
                    print("\t- " + data_lights[light_identifier]["name"] + " - " + state)
    else:
        for i in range(1, len(data_lights)):
            if target in data_lights[str(i)]["name"]:
                state = "On" if data_lights[str(i)]["state"]["on"] else "Off"
                print(data_lights[str(i)]["name"] + "  --  " + state)
    input("\nPress enter to continue")
    main()

def main():
    ref.clear()
    print("Welcome to the JMC Hue Light Interaction Program!!")
    print("Please select an option:\n\n[1]: View states of all lights\n[2]: View the state of a specific light\n[3]: Change the light state\n[0]: Exit")
    option = input("\nPlease select an option > ")
    if option == "1":
        viewState("all")
    elif option == "2":
        lightName = input("What is the name of the light you want to find? > ")
        viewState(lightName)
    elif option == "3":
        pass
    elif option == "0":
        raise SystemExit
    else:
        print("That is not a valid option, please select a different option")
        main()

if __name__ == "__main__":
    main()




