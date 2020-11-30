from bs4 import BeautifulSoup 
import json
import utility.strings as s 
import utility.api as api
import utility.table as t
import utility.uf_infos as uf_infos
import utility.pagination as p
from uuid import uuid4

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
postFields = {'UF': 'SC', 'Localidade': ''}
limit = 50
"""
    The first request need to be make in separeted of another because of 
    the model of the Correios's site and the way I've make the functions to get the data.
    The queries to get the first data in the HTML requires that;
""" 
allResults = []

# Initializing uf class to to able to set information iof de ufs...
ufInformations = uf_infos.UF_Infos() 

# Make post request to get the result html page
resultHTML = api.Api.getResult(url, postFields)

# Cleaning the data for search an set the pagination dictionary
resultEscapedXML = s.String_utils.cleanHTML(resultHTML)

# Initializing the pagination infos
pagination = p.Pagination(limit).getPagination(resultEscapedXML)
controlPage = pagination['results']

resultHTML = resultHTML.decode('unicode_escape') 

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


allResults.append(filteredList)

### begin
def main(postFields):
    results = []

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
### end  

while controlPage > 0:
    postFields['pagini'] = pagination['pagini']
    postFields['pagfim'] = pagination['pagfim']
      
    results = main(postFields)
      
    pagination['pagini'], pagination['pagfim'] = p.Pagination.pageControl2(pagination['pagini'], limit)
    print('1',pagination)
    controlPage = controlPage - limit
    allResults.append(results)
# while p.Pagination.hasNext(pagination['results'], pagination['pagfim'], 50):
#     postFields['pagini'] = pagination['pagini']
#     postFields['pagfim'] = pagination['pagfim']
#       
#     results = main(postFields)
#       
#     pagination['pagini'], pagination['pagfim'] = p.Pagination.pageControl2(pagination['pagini'], 50)
#     print('1',pagination)
#     print(p.Pagination.hasNext(pagination['results'], pagination['pagfim'], 50))
#     allResults.append(results)
     
     
print(allResults)
 
with open('results.jsonl','w') as wf:
    for data in allResults:
#  Transform the object into a json and whrite to a file in jsonl format
        result = [json.dumps(record) for record in data]
        for line in result:
            line = bytes(line, 'utf-8').decode('unicode_escape')
            wf.write(f'{line}\n')
