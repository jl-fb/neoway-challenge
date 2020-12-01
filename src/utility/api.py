import requests

class Api:

    def getResult(url, postFields): # @NoSelf
        source = requests.post(url, data = postFields)
        
        if source.status_code != 200:
            return f'Error to reach URL: {url}. Error {source.status_code} '
        result = source.content
        return result