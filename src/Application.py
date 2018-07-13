'''
Created on Jul 12, 2018

@author: y948467
'''
import copy

class Application(object):



    def __init__(self, applicationName, serverName, instances):
        self.applicationName = applicationName
        self.serverName = serverName
        self.instances = instances
        
        
    def printInfo(self):
        print("Application Name: " + self.applicationName)
        print("Server Name: " + self.serverName)
        for instance in self.instances:
            instance.printInfo()
        
        
        
class Instance(object):

    def __init__(self, name, expected):
        self.name = name
        self.expected = expected #urls mapped to an array of expected responses
        self.actual = copy.deepcopy(expected)
        
        for key in self.actual:
            print(key)
            
            
    def printInfo(self):
        print(self.name)
        print(self.expected)
        print(self.actual)
            
            