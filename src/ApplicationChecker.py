'''
Created on Jul 12, 2018

@author: y948467
'''
import requests
import webbrowser
from multiprocessing.dummy import Pool as ThreadPool 
from Application import Application
from Application import Instance

#----------------------------------------------------------------
CONFIGURATION_FILE = "sample5.txt"
#----------------------------------------------------------------
#ji
applications = []

def dataToHTML():
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
        height: 25px;
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
                <th>Application Name</th>
                <th>Server</th>
                <th>Instance</th>
                <th>URL</th>
                <th>Expected</th>
                <th>Actual</th>
                <th>Result</th>
            </tr>
            {0}
        </table>
    </body>
    </HTML>"""
    items = []
    for application in applications:
        instances = application.instances
        for instance in instances:
            expected = instance.expected
            actual = instance.actual
            urls = instance.urls
            for url in urls:
                for expectedValue in expected[url]:
                    for actualValue in actual[url]:
                        row = []
                        row.append(application.applicationName)
                        row.append(application.serverName)
                        row.append(instance.name)
                        row.append(url)
                        row.append(expectedValue)
                        row.append(actualValue)
                        if expectedValue == actualValue:
                            row.append("Pass")
                        else:
                            row.append("Fail")
                        items.append(row)
            
    
    
#     items = []
#     for cell in cells:
#         urlsToReponse = cell.getUrlAndResponse()
#         urls = cell.getUrls()
#         names = cell.getNames()
#         responses = []
#         for url in urls:
#             responses.append(urlsToReponse[url])
#         for i in range(len(urls)):
#             row = []
#             row.append(names[i])
#             row.append(urls[i])
#             row.append(responses[i])
#             if responses[i] == 200:
#                 row.append("Pass")
#             else:
#                 row.append("Fail")
#             items.append(row)
#     print(items)
    
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




def requestApplication(application):
    instances = application.instances
    for instance in instances:
        expected = instance.expected
        actual = instance.actual
        for url in expected:
            try:
                resp = requests.get(url)
                actual[url] = [str(resp.status_code)] * len(actual[url])
            except requests.exceptions.RequestException as e:
                print(e)
    


#read the file and populate the applications list
with open(CONFIGURATION_FILE , 'r') as f:
    line = f.readline()
    while line:
        applicationInformation = []
        for i in range(2):
            line = line.strip("\n")
            line = line.strip("\t")
            applicationInformation.append(line)
            line = f.readline()
        numbers = list(map(int, line.split()))
        line = f.readline().strip("\n")
        instances = []
        for i in range(numbers[0]): # number of instances
            instanceName = line
            line = f.readline().strip("\n")
            urls = {}
            for j in range(numbers[i + 1]):
                line = line.split()
                urls[line[0]] = line[1:]
                line = f.readline().strip("\n")
            instance = Instance(instanceName, urls)
            instances.append(instance)
        application = Application(applicationInformation[0], applicationInformation[1], instances)
        applications.append(application)

pool = ThreadPool(4) 
pool.map(requestApplication, applications)
pool.close()
pool.join()

dataToHTML()
for application in applications:
    application.printInfo()