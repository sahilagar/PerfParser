'''
Created on Jun 25, 2018

@author: y948467
'''
class Cell(object):
    def __init__(self, address, serverName, title):
        self.address = address #11.120.228.252
        self.serverName = serverName #esu2v735
        self.title = title #FCC Client Cell A
        self.healthCheck = {} #name, response
        self.names = [] # name
        self.urlAndResponse = {} #url and the given response
        self.urls = []
        
        
           
    def addCheck(self, name, result):
        self.healthCheck[name] = result
     
    def addName(self, name):
        self.names.append(name)
        
    def addUrlAndResponse(self, url, response):
        self.urlAndResponse[url] = response
        
    def addUrl(self, url):
        self.urls.append(url)
        
    def getUrls(self):
        return self.urls
    
    def getUrlAndResponse(self):
        return self.urlAndResponse
        
    def getNames(self):
        return self.names    

    def printHealthCheck(self):
        print(self.healthCheck)
        
    def getAddress(self):
        return self.address
    
    def getServerName(self):
        return self.serverName
    
    def getTitle(self):
        return self.title
    
    def getHealthCheck(self):
        return self.healthCheck
    
    def printInfo(self):
        print(self.title)
        print(self.address)
        print(self.healthCheck)
        print(self.urlAndResponse)
    
        