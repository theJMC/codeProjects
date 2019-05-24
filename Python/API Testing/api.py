"""
Title: Phillips Hue API

Date: 22/04/2019

Author: James McCarthy

Notes:

Todo:

"""
# Imports dependencies
import reference as ref # Personal Reference file
import json # To be able to handle JSON
import urllib.request # To be able to hadle URLs 
import requests # Grabs the raw JSON file

# Variable Setup 
api_key = "qlSEH3JH8d7nin2DSQ2aphmBu-mhsqBQ3yoyTvqg" # Unique API Key
url = "http://192.168.0.25/api/" + api_key # URL to the bridge's /api folder

lights_json = requests.get(url + "/lights") # Grabs the raw lights JSON
rooms_json = requests.get(url + "/groups") # Grabs the raw rooms JSON

data_lights = lights_json.json() # Converts the Raw JSON into Python Dictionaries 
data_rooms = rooms_json.json() # Converts the Raw JSON into Python Dictionaries 


""" Old printout code. Only use for Debugging """
# for i in range(1, len(data_lights)):
#     print(data_lights[str(i)]["name"] + " -- " + str(data_lights[str(i)]["state"]["on"]))

# define the viewState function: It prints out the states of the lights
def viewState(target):
    print("\n")
    if target == "all":
        # Iterates all of the groups: includes rooms
        for i in range(1, len(data_rooms)):
            # Finds if it is a room
            if data_rooms[str(i)]["type"] == "Room":  
                # Prints the first part of the line
                print(data_rooms[str(i)]["name"] + ": ")
                # Prints out the state
                for light_identifier in data_rooms[str(i)]["lights"]:
                    state = "On" if data_lights[light_identifier]["state"]["on"] else "Off"
                    print("\t- " + data_lights[light_identifier]["name"] + " - " + state)
    else:
        # iterates to see if the target is in the name 
        for i in range(1, len(data_lights)):
            if target in data_lights[str(i)]["name"]:
                state = "On" if data_lights[str(i)]["state"]["on"] else "Off"
                print(data_lights[str(i)]["name"] + "  --  " + state)
    input("\nPress enter to continue")
    main()

# Main Program Deifinition
def main():
    # Startup code
    ref.clear() # Clears the terminal
    print("Welcome to the JMC Hue Light Interaction Program!!")
    print("Please select an option:\n\n[1]: View states of all lights\n[2]: View the state of a specific light\n[3]: Change the light state\n[0]: Exit")
    option = input("\nPlease select an option > ")
    # Classic Option Selection If/Else
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

# Runs the program immediatly if not imported
if __name__ == "__main__":
    main()




