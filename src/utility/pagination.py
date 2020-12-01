from utility import strings as s
from ossaudiodev import control_labels

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
        
    def pageControl2(limit, currentPage, pageEnd, maxResults): # @NoSelf
        try:
            
        # parsing to int
            limit = Pagination.__toInt__(limit)
            currentPage = Pagination.__toInt__(currentPage)
            pageEnd = Pagination.__toInt__(pageEnd)
            maxResults = Pagination.__toInt__(maxResults)
             
            nextPage = limit + currentPage 
            pageEnd = nextPage + (limit - 1)
            
        except Exception as error:
            print(f'[Pagination_class] PageControl Error {error}') 
            
        else:
            return nextPage, pageEnd
    
    def hasNext(maxResults, currentPage, pageEnd): # @NoSelf
        try:
            maxResults = Pagination.__toInt__(maxResults)
            currentPage = Pagination.__toInt__(currentPage)
            pageEnd = Pagination.__toInt__(pageEnd)
            if type(currentPage) is not int:
                currentPage = int(currentPage)
            
            if currentPage < maxResults:
                flag = True
            else:    
                flag = False
            
            if pageEnd > maxResults:
                dif = maxResults - currentPage
                pageEnd = dif + currentPage
                print("PAGE END", pageEnd)
                
            return flag, pageEnd
        
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
    
    def __toInt__(source): # @NoSelf
        try:
            if type(source) is not int:
                return int(source)
            return source
        except Exception as error:
            print(f'[Pagination_class] Error to convert values. Error{error}')
            
