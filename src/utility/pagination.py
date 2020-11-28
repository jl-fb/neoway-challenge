class Pagination():
  
    def pagination(self, limit):
        try:
        # parsing to int
            if type(limit) is not int:
                limitInt = int(limit)
    
#         if type(maxResults) is not int:
#             maxResults = int(maxResults)

            offset = limitInt + 1
            pageEnd = offset + (limit - 1)
            
        except Exception as error:
            print(f'[Pagination_class] Error {error}') 
            
        else:
            return offset, pageEnd
