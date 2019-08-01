"""
Title:

Date: 00/00/2019

Author: James McCarthy

Notes:

Todo:

"""
import tube
import cherrypy

class tube_app(object):
    @cherrypy.expose
    def index(self):
        result = []
        
        with open("index.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        return str(page).format(''.join(result))

    @cherrypy.expose
    def status(self):
        result = []
        with open("status.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        status = t.getTube()
        for item in status:
            if item[1] == "Severe Delays" or item[1] == "Part Suspended":
                if '&' in item[0]:
                    name = item[0].replace("&", "^")
                    result.append(f"<tr><th scope='row'><a href='/line?line={name.lower()}'>" + item[0] + "</a></th><td class='text-danger font-weight-bold'>" + item[1] + "</td></tr>")
                else:
                    result.append(f"<tr><th scope='row'><a href='/line?line={item[0].lower()}'>" + item[0] + "</a></th><td class='text-danger font-weight-bold'>" + item[1] + "</td></tr>")
            elif item[1] == "Minor Delays":
                if '&' in item[0]:
                    name = item[0].replace("&", "^")
                    result.append(f"<tr><th scope='row'><a href='/line?line={name.lower()}'>" + item[0] + "</a></th><td class='text-warning font-weight-bold'>" + item[1] + "</td></tr>")
                else:
                    result.append(f"<tr><th scope='row'><a href='/line?line={item[0].lower()}'>" + item[0] + "</a></th><td class='text-warning font-weight-bold'>" + item[1] + "</td></tr>")
            else:
                if '&' in item[0]:
                    name = item[0].replace("&", "^")
                    result.append(f"<tr><th scope='row'><a href='/line?line={name.lower()}'>" + item[0] + "</a></th><td>" + item[1] + "</td></tr>")
                else:
                    result.append(f"<tr><th scope='row'><a href='/line?line={item[0].lower()}'>" + item[0] + "</a></th><td>" + item[1] + "</td></tr>")
        return str(page).format(''.join(result))

    @cherrypy.expose
    def line(self, line):
        with open("line.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        status = t.getTube()
        for item in status:
            if item[0].lower().split()[0] == line.split()[0]:
                result = item
        if result[1] != "Good Service":
            final = "<tr><th scope='row'>Line:</th><td>" + result[0] + "</td></tr><tr><th scope='row'>Status:</th><td>" + result[1] + "</td></tr><tr><th scope='row'>Reason:</th><td>" + result[2] + "</td></tr>"
        else:
            final = "<tr><th scope='row' >Line:</th><td>" + result[0] + "</td></tr><tr><th scope='row'>Status:</th><td>" + result[1] + "</td></tr>"
        if line.lower() == "dlr":
            line = "DLR"
        if '^' in line.lower():
            line = line.replace("^", "&")
        return str(page).format(line, final)

    @cherrypy.expose
    def stations(self, line="all"):
        with open("stations.html", "r") as file:
            data = file.readlines()
            page = ''.join(data)
        status=t.getTube()
        result = ["<li class='nav-item'><a class='nav-link active' href='?line=all'>All</a></li>"]
        for item in status:
            if ' ' in item[0]:
                name = item[0].replace("&", "^")
            else:
                name = item[0]
            if item[0].lower == line:
                result.append(f"<li class='nav-item'><a class='nav-link active' href='?line={name.lower()}'>{item[0]}</a></li>")
            else:
                result.append(f"<li class='nav-item'><a class='nav-link' href='?line={name.lower()}'>{item[0]}</a></li>")
        line_title = ""
        if '^' in line:
            line = line.replace("^", "&")
        if line == "all":
            line_title = " All Lines"
        elif line == "dlr":
            line_title = "the DLR"
        else:
            line_title = f"the {line.capitalize()} Line"
        station_list = []
        line_names = t.getLines(False)
        line_ids = t.getLines(True)
        print(line_names)
        if line != "all":
            id_num = line_names.index(line.capitalize())
            line_id = line_ids[id_num]
            station_list = t.getStationsOnLine(line_id)
        else:
            station_list = t.getAllStations(False)
        station_result = []
        for item in station_list:
            station_result.append("<tr><td>" + item + "</td></tr>")
        return str(page).format(''.join(result), line_title, ''.join(station_result))

if __name__ == "__main__":
    t = tube.tube()
    cherrypy.quickstart(tube_app(), config="config.txt")