import requests

class Api:
    
    def __init__(self, url, postFields):
        self.URL = url 
        self.postFields = postFields
    
    def getResult(self):
        source = requests.post(self.URL, data = self.postFields)
        
        if source.status_code != 200:
            return f'Error to reach URL: {self.URL}. Error {source.status_code} '
        result = source.content.encodings("'utf-8")
        return result