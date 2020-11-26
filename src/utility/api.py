from urllib.request import Request, urlopen
from urllib.parse import urlencode
import requests

class Api:
    
    def __init__(self, url, postFields):
        self.URL = url 
        self.postFields = postFields
    
    def getResults(self):
        # Make the POST request to the APT 
        request = Request(self.URL, urlencode(self.postFields).encode())
        print(request)
        
        # Convert the result to string for manipulation
        pageHTML = urlopen(request).read()
        return pageHTML
    
    def getResult(self):
        source = requests.post(self.URL, data = self.postFields)
        
        if source.status_code != 200:
            return f"Error to reach URL: {self.URL}. Error {source.status_code} "
        result = source.content
        return result