from bs4 import BeautifulSoup 
from uuid import uuid4
import utility.api as api
import utility.table as t
import utility.uf_infos as uf_infos

class Next_Call__To_API:
    
    def nexCall(url,postFields): # @NoSelf
        results = []
        filteredList = []
        # Initializing uf class to to able to set information iof de ufs...
        ufInformations = uf_infos.UF_Infos() 
        resultHTML = api.Api.getResult(url, postFields)
        resultHTML = resultHTML.decode('unicode_escape') 
    
        soup =  BeautifulSoup(resultHTML, 'lxml')

        rows = t.Table.getTableRowsData(soup)

        # Transform the one dimentional array to multi, for to be able to store de each line of city info
        rowsReshaped = t.Table.flatToMultiList(rows, 4)

        for line in rowsReshaped:
            ufInformations.id = str(uuid4())
            ufInformations.localidade = line[0]
            ufInformations.faixaCep = line[1]
            ufInformations.situacao = line[2]
            ufInformations.tipoFaixa = line[3]
            results.append(ufInformations.__repr__())

            # Filtering the results to remove duplicate cities
            filteredList = t.Table.filteredList(results, 'localidade')
 
        return filteredList