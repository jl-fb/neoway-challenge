from bs4 import BeautifulSoup 
import pandas as pd
from itertools import groupby
import json
import utility.strings as s 
import utility.api as api
import utility.table as t
import utility.uf_infos as uf_infos
import utility.pagination as p
import numpy
from enum import unique

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
postFields = {'UF': 'SC', 'Localidade': ''}

test = ['UF', 'SC', 'Localidade', '']
# pagination = {'pagini': 0, 'pagfim': 0, 'results': 0, 'qtdrow': 50}

js = []

# class Table:
#     def __init__(self):
#         self.localidade = ''
#         self.faixaCep = '' 
#         self.situacao = ''
#         self.tipoFaixa = ''
#     
#     def __repr__(self):
# #         return {'UF': '%s', 'faixa_cep_UF': '%s',  'localidade': '%s', 'faixa_cep_localidade': '%s', 'situacao': '%s', 'tipoFaixa': '%s'} % (self.uf, self.faixaCepUF, self.localidade, self.faixaCepLocalidade, self.situacao, self.tipoFaixa)
#         return {'localidade': self.localidade, 'faixa_cep_localidade': self.faixaCep, 'situacao': self.situacao, 'tipoFaixa': self.tipoFaixa}
#     
#     def __out__(self):
#         return self.localidade, self.faixaCep, self.situacao, self.tipoFaixa

# Initializing UFS informations
ufInformations = uf_infos.UF_Infos() 

# Make post request to get the result html page
resultHTML = api.Api(url, postFields).getResult()

# Cleaning the data for search an set the pagination dictionary
resultEscapedXML = s.String_utils.cleanHTML(resultHTML)


print(resultEscapedXML)
pagination = p.Pagination().getPagination(resultEscapedXML)

resultHTML = resultHTML.decode('unicode_escape') 

# Passing the data to BeautifulSoup for manipulation
soup = BeautifulSoup(resultHTML, 'lxml') 
#table = soup.find('table', attrs=cl)
# 
# r = []
# dfs = pd.read_html(resultHTML)
# for df in dfs:
#     r.append(df)
# 
# print(df.values)
# for rows in df.values:
#     data.localidade = rows[0]
#     data.faixaCep = rows[1]
#     data.situacao = rows[2]
#     data.tipoFaixa = rows[3]
#     js.append(data.__repr__())
# 
# with open('table.jsonl', 'w') as wf:
#     for data in js:
#         wf.write(f'{data}\n')
        

#     
#print(pagination)

print(pagination)
#########

tableHTML = t.Table.getTable(soup, 'table', 'tmptabela')
 
table_rows = t.Table.findAllTableRows(tableHTML)
 
rows = t.Table.getTableRowsData(soup, 'td')

rowsReshaped= t.Table.flatToMultiList(rows, 4)


print(rowsReshaped)

for line in rowsReshaped:
    ufInformations.localidade = line[0]
    ufInformations.faixaCep = line[1]
    ufInformations.situacao = line[2]
    ufInformations.tipoFaixa = line[3]
    js.append(ufInformations.__repr__())


filteredList = t.Table.filteredList(js, 'localidade')
print(len(filteredList))

result = [json.dumps(record) for record in filteredList]
with open('table.jsonl', 'w') as wf:
    for line in result:
        line = bytes(line, 'utf-8').decode('unicode_escape')
        print(f'{line}\n')
        wf.write(f'{line}\n')