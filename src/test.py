'''
Created on Jul 13, 2018

@author: y948467
'''
from Application import Application
from Application import Instance


applications = []
CONFIGURATION_FILE = "sample7.txt"

def processLine(line):
    info = line.split(":")[1]
    info = info.split()
    info = " ".join(info)
    return info

with open(CONFIGURATION_FILE , 'r') as f:
    for line in f:
        currApplication = Application()
        if line.startswith("APPLICATIONNAME:"):
            applicationName = processLine(line)
            print(applicationName)
            currApplication.applicationName = applicationName

        
        
        
        
        
        
# applicationInformation = []
# for i in range(2):
#     line = line.strip("\n")
#     line = line.strip("\t")
#     applicationInformation.append(line)
#     line = f.readline()
# numbers = list(map(int, line.split()))
# line = f.readline().strip("\n")
# instances = []
# for i in range(numbers[0]): # number of instances
#     instanceName = line
#     line = f.readline().strip("\n")
#     urls = {}
#     for j in range(numbers[i + 1]):
#         line = line.split()
#         urls[line[0]] = line[1:]
#         line = f.readline().strip("\n")
#     instance = Instance(instanceName, urls)
#     instances.append(instance)
# application = Application(applicationInformation[0], applicationInformation[1], instances)
# applications.append(application)