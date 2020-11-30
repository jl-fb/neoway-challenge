from utility import strings as s

class Pagination:
  
    def __init__(self, limit):
        self.initial = 0
        self.end = 0
        self.results = 0
        self.limit = limit 
        
    def pageControl(currenLimit): # @NoSelf
       
        try:
        # parsing to int
            
            if type(currenLimit) is not int:
                limitInt = int(currenLimit)
            limitInt = currenLimit
#         if type(maxResults) is not int:
#             maxResults = int(maxResults)

            offset = limitInt + 1
            pageEnd = offset + (limitInt - 1)
            
        except Exception as error:
            print(f'[Pagination_class] PageControl Error {error}') 
            
        else:
            return offset, pageEnd
    
    def hasNext(maxResults, currResults): # @NoSelf
        try:
            if currResults < maxResults:
                return True
            return False
        
        except Exception as error:
            print(f'[Pagination_class] Error verify if has next page. Error {error}') 
            
    def getPagination(self, html, sourceIni='name=pagini value="', offsetIni=2, sourceEnd='name=pagfim value="', offsetEnd = 3, sourceResults='<br><br><table class="tmptabela"', offsetResults=4): 
        try:
                     
            #set the pagination variables
            self.initial = int(s.String_utils.findInHTML(html, sourceIni, offsetIni))
            self.end = int(s.String_utils.findInHTML(html, sourceEnd, offsetEnd))
            self.results = int(s.String_utils.findInHTMLReverse(html, sourceResults, offsetResults))
            
            return {'pagini': self.initial, 'pagfim': self.end, 'results': self.results}
        
        except Exception as error:
            print(f'[Pagination_class] Error to get pagination values. Error{error}')
        
