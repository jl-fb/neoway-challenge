from bs4 import BeautifulSoup 
import json
import utility.strings as s 
import utility.api as api
import utility.table as t
import utility.uf_infos as uf_infos
import utility.pagination as p

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
postFields = {'UF': 'SC', 'Localidade': ''}

js = []

# Initializing uf class to to able to set information iof de ufs...
ufInformations = uf_infos.UF_Infos() 

# Make post request to get the result html page
resultHTML = api.Api(url, postFields).getResult()

# Cleaning the data for search an set the pagination dictionary
resultEscapedXML = s.String_utils.cleanHTML(resultHTML)


# Initializing the pagination infos
pagination = p.Pagination().getPagination(resultEscapedXML)

resultHTML = resultHTML.decode('unicode_escape') 

# Passing the data to BeautifulSoup for manipulation
soup = BeautifulSoup(resultHTML, 'lxml') 

print(pagination)
#########

# Get the table of uf infos
tableHTML = t.Table.getTable(soup, 'table', 'tmptabela')

# Get the rows and td data 
table_rows = t.Table.findAllTableRows(tableHTML) 
rows = t.Table.getTableRowsData(soup, 'td')

# Transfor the one dimentional array to multi for to be able to store de each line of city info
rowsReshaped= t.Table.flatToMultiList(rows, 4)
for line in rowsReshaped:
    ufInformations.localidade = line[0]
    ufInformations.faixaCep = line[1]
    ufInformations.situacao = line[2]
    ufInformations.tipoFaixa = line[3]
    js.append(ufInformations.__repr__())

# Filtering the results to remove duplicate cities
filteredList = t.Table.filteredList(js, 'localidade')

# Transform the object into a json and whrite to a file in jsonl format
result = [json.dumps(record) for record in filteredList]
with open('table.jsonl', 'w') as wf:
    for line in result:
        line = bytes(line, 'utf-8').decode('unicode_escape')
        print(f'{line}\n')
        wf.write(f'{line}\n')