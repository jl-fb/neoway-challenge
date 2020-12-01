from bs4 import BeautifulSoup 
from uuid import uuid4
import utility.api as api
import utility.table as t
import utility.uf_infos as uf_infos
import utility.strings as s
import utility.pagination as p

class Call_To_API:
   
    def firstCall(url, postFields, limit): # @NoSelf
        
        # Initializing uf class to to able to set information iof de ufs...
        ufInformations = uf_infos.UF_Infos() 

        # Make post request to get the result html page
        resultHTML = api.Api.getResult(url, postFields)
        print(resultHTML)
        resultHTML = resultHTML.decode('unicode_escape') 
        
        # Cleaning the data for search an set the pagination dictionary
        resultEscapedXML = s.String_utils.cleanHTML(resultHTML)
        print(resultEscapedXML)
        # Initializing the pagination infos
        pagination = p.Pagination(limit).getPagination(resultEscapedXML)
        # Passing the data to BeautifulSoup for manipulation
        soup = BeautifulSoup(resultHTML, 'lxml') 

        # Get the rows and td data 
        rows = t.Table.getFirstTableRowsData(soup, 'td')

        # Transform the one dimentional array to multi, for to be able to store de each line of city info
        rowsReshaped = t.Table.flatToMultiList(rows, 4)
        results = []
        for line in rowsReshaped:
            ufInformations.id = str(uuid4())
            ufInformations.localidade = line[0]
            ufInformations.faixaCep = line[1]
            ufInformations.situacao = line[2]
            ufInformations.tipoFaixa = line[3]
            results.append(ufInformations.__repr__())

            # Filtering the results to remove duplicate cities
            filteredList = t.Table.filteredList(results, 'localidade') 
            
        return filteredList, pagination