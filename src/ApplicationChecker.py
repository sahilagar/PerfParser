'''
Created on Jul 12, 2018

@author: y948467
'''

from Application import Application
from Application import Instance

#----------------------------------------------------------------
CONFIGURATION_FILE = "sample5.txt"
#----------------------------------------------------------------

applications = []


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

for application in applications:
    application.printInfo()