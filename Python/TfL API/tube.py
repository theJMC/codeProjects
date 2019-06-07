"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

TODO Add Routes

"""
from getjson import getJsonFromURL as getJson
from columnar import columnar
from datetime import datetime

class tube:

    def __init__(self):
        self.update()

    def update(self):
        self.tube_status = getJson("https://api.tfl.gov.uk/line/mode/tube/status")
        self.dlr_status = getJson("https://api.tfl.gov.uk/line/mode/dlr/status")
        self.lines_data = getJson("https://api.tfl.gov.uk/line/mode/tube")
        self.updated = datetime.now().strftime("%d-%m-%Y %H:%M")

    def getTube(self):
        print("\n")
        headers = ["Line", "Status", "Issues"]
        data = []
        for item in self.tube_status:
            if item["lineStatuses"][0]["statusSeverityDescription"] != "Good Service":
                data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"], item["lineStatuses"][0]["reason"]])
            else:
                data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"], "N/a"])
        if self.dlr_status[0]["lineStatuses"][0]["statusSeverityDescription"] != "Good Service":
            data.append([self.dlr_status[0]["name"], self.dlr_status[0]["lineStatuses"][0]["statusSeverityDescription"], self.dlr_status[0]["lineStatuses"][0]["reason"]])
        else:
            data.append([self.dlr_status[0]["name"], self.dlr_status[0]["lineStatuses"][0]["statusSeverityDescription"], "N/a"])
        table = "Last Updated: " + self.updated + "\n" + columnar(data, headers)
        return table

    def getLines(self, id_select):
        lines = []
        if id_select:
            for item in self.lines_data:
                lines.append(item["id"])
        else:
            for item in self.lines_data:
                lines.append(item["name"])
        return lines

    def getStationsOnLine(self, line_ID):
        stations = []
        stations_raw = getJson("https://api.tfl.gov.uk/line/" + line_ID + "/stoppoints")
        for item in stations_raw:
            stations.append(item["commonName"].replace('Underground Station', ''))
        return stations

    def getRoutesOnLine(self, line_ID):
        routes = []
        allRoutes = getJson("https://api.tfl.gov.uk/line/" + line_ID + "/route")
        for item in allRoutes["routeSections"]:
            routes.append(item["name"].replace('Underground Station', ''))
        return routes

    def getAllStations(self, id_select):
        stations_withDuplicates = []
        for item in self.getLines(True):
            stations_raw = getJson("https://api.tfl.gov.uk/line/" + item + "/stoppoints")
            for item in stations_raw:
                if id_select:
                    stations_withDuplicates.append(item["id"])
                else:
                    stations_withDuplicates.append(item["commonName"].replace('Underground Station', ''))
        stations = list(dict.fromkeys(stations_withDuplicates))
        return stations

    def searchAllStations(self, stationName):
        all_station_names = self.getAllStations(False)
        results = []
        for item in all_station_names:
            if stationName.lower() in item.lower() or stationName.lower() == item.lower():
                results.append(item)
        return results

    def convertIDtoName(self, id_num):
        all_station_names = self.getAllStations(False)
        all_station_ids = self.getAllStations(True)
        results = []
        for i in range(len(all_station_ids)):
            if id_num == all_station_ids[i]:
                results.append(all_station_names[i])
        return results

    def convertNametoID(self, name):
        all_station_names = self.getAllStations(False)
        all_station_ids = self.getAllStations(True)
        results = []
        for i in range(len(all_station_names)):
            if name.lower() in all_station_names[i].lower() or name.lower() == all_station_names[i].lower():
                results.append(all_station_ids[i])
        return results
    
    def fares(self, origin_id, dest_id):
        pass


class rail:

    def __init__(self):
        self.update()

    def update(self):
        self.tube_status = getJson("https://api.tfl.gov.uk/line/mode/tube/status")
        self.dlr_status = getJson("https://api.tfl.gov.uk/line/mode/dlr/status")
        self.lines_data = getJson("https://api.tfl.gov.uk/line/mode/tube")
        self.updated = datetime.now().strftime("%d-%m-%Y %H:%M")

    def getRail(self):
        rail_status = getJson("https://api.tfl.gov.uk/line/mode/national-rail/status")
        headers = ["Line", "Status", "Issues"]
        data = []
        for item in rail_status:
            if item["lineStatuses"][0]["statusSeverityDescription"] != "Good Service":
                data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"]])
            else:
                data.append([item["name"], item["lineStatuses"][0]["statusSeverityDescription"]])
        table = "Last Updated: " + self.updated + "\n" + columnar(data, headers)
        return table




if __name__ == "__main__":
    t = tube()
    print(t.convertIDtoName("940GZZLUKSX"))