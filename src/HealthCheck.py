'''
Created on Jun 21, 2018

@author: Y948467
'''
import requests
import webbrowser
import numpy
from Cell import Cell

#update these parameters----------------------------------------------------
CONFIGURATION_FILE = "sample.txt"
hosts = ["8080", "8180", "8280"]
HEALTHCHECKURL = "/api/catalog/v2/categories/healthcheck"
HTTP = "http://"
#---------------------------------------------------------------------------
cells = []

def dataToHTML(cells):
    #https://stackoverflow.com/questions/33920896/table-within-an-html-document-using-python-list
    f = open('helloworld.html','w')
    
    
    head = """<HTML>
    <head>
    <style>
        table, th, td {
        border: 1px solid black;
    }
        table {
        border-collapse: collapse;
    }
        table {
        width: 100%;
    }

        th {
        height: 50px;
    }
        th, td {
        padding: 15px;
        text-align: left;
    }
        #content img {
            position: absolute;
            top: 0px;
            right: 0px;
            width: 15%;
            height: auto;
            
    }
    </style>
    </head>"""
    html = """
    <body>
        <div id="content">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Macys_logo.svg/1280px-Macys_logo.svg.png" class="ribbon"/>
        </div>
        <h1>Responses</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>URL</th>
                <th>Response</th>
                <th>Result</th>
            </tr>
            {0}
        </table>
    </body>
    </HTML>"""
    highlightCells = []
    items = []
    for cell in cells:
        urlsToReponse = cell.getUrlAndResponse()
        urls = cell.getUrls()
        names = cell.getNames()
        responses = []
        for url in urls:
            responses.append(urlsToReponse[url])
        for i in range(len(urls)):
            row = []
            row.append(names[i])
            row.append(urls[i])
            row.append(responses[i])
            if responses[i] == 200:
                row.append("Pass")
            else:
                row.append("Fail")
            items.append(row)
    print(items)
    
    #tr = "<tr>{0}</tr>"
    #td = "<td>{0}</td>"    
    #subitems = [tr.format(''.join([td.format(a) for a in item])) for item in items]
    
    formatted = []
    for item in items:
        row = ["<tr>"]
        for a in item:
            if a == "Fail":
                row.append("<td bgcolor=\"#FF0000\">" + str(a) + "</td>")
            elif a == "Pass":
                row.append("<td bgcolor=\"#00FF00\">" + str(a) + "</td>")
            else:
                row.append("<td>" + str(a) + "</td>")
        row.append("</tr>")
        row = "".join(row)
        formatted.append(row)
    
    f.write(head)
    f.write(html.format("".join(formatted))) #replace with sub items
    f.close()

    webbrowser.open_new_tab('helloworld.html')

#pings and finds the health of each server, puts it in the healthcheck dictionary in the cell class
def requestCells(cells):
    for cell in cells:
        names = cell.getNames()
        print("hi")
        for i in range(len(hosts)):
            url = HTTP + cell.getServerName() + ":" + hosts[i] + HEALTHCHECKURL
            cell.addUrlAndResponse(url, "Failed Connection")
            cell.addUrl(url)
            try:
                resp = requests.get(url)
                cell.addCheck(names[i], resp.status_code) #add the name of the 8080  and the response
                cell.addUrlAndResponse(url, resp.status_code) #add the url and the response that it receives
            except requests.exceptions.RequestException as e:
                print(e)

#populates the cell from the cell information array
def makeCell(cellInformation):
    cell = Cell(cellInformation[0], cellInformation[1], cellInformation[2])
    for i in range(3,6):
        cell.addCheck(cellInformation[i], -1)
        cell.addName(cellInformation[i])
    cells.append(cell)

    
#opens the configuration file and reads in all the information
with open(CONFIGURATION_FILE , 'r') as f:
    line = f.readline()
    while line:
        cellInformation = []
        for i in range(6):
            line = line.strip("\n")
            line = line.strip("\t")
            
            cellInformation.append(line)
            line = f.readline()
        makeCell(cellInformation)
        
requestCells(cells)
# for cell in cells:
#     cell.printInfo()
dataToHTML(cells)