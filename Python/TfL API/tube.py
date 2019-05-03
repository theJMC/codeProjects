"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
from getjson import getJson
from os import system
from columnar import columnar

def tubeStatus(tube, dlr):
    system("cls")
    print("\n")
    headers = ["Line", "Status", "Issues"]
    data = []
    if tube:
        tube_status = getJson("https://api.tfl.gov.uk/line/mode/tube/status")
        for item in tube_status:
            if item["lineStatuses"][0]["statusSeverityDescription"] != "Good Service":
                data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"], item["lineStatuses"][0]["reason"]])
            else:
                data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"], "N/a"])
    if dlr:
        dlr_status = getJson("https://api.tfl.gov.uk/line/mode/dlr/status")
        if dlr_status[0]["lineStatuses"][0]["statusSeverityDescription"] != "Good Service":
            data.append([dlr_status[0]["name"], dlr_status[0]["lineStatuses"][0]["statusSeverityDescription"], dlr_status[0]["lineStatuses"][0]["reason"]])
        else:
            data.append([dlr_status[0]["name"], dlr_status[0]["lineStatuses"][0]["statusSeverityDescription"], "N/a"])
    table = columnar(data, headers)
    return table

def natrailStatus():
    system("cls")
    rail_status = getJson("https://api.tfl.gov.uk/line/mode/national-rail/status")
    headers = ["Line", "Status", "Issues"]
    data = []
    for item in rail_status:
        if item["lineStatuses"][0]["statusSeverityDescription"] != "Good Service":
            data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"], item["lineStatuses"][0]["reason"]])
        else:
            data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"], "N/a"])
    table = columnar(data, headers)
    return table

if __name__ == "__main__":
    tubeStatus(True, True)
    # natrailStatus()