from bs4 import BeautifulSoup 
import json
from uuid import uuid4
import utility.strings as s 
import utility.api as api
import utility.table as t
import utility.uf_infos as uf_infos
import utility.pagination as p
import utility.constant as constant
from functions import firstCallToAPI, nextCallToAPI

UFS = constant.UFS
url = constant.URL 
postFields = {'UF': 'TO', 'Localidade': ''}
limit = constant.LIMIT

"""
    The first request need to be make in separeted of another because of 
    the model of the Correios's site and the way I've make the functions to get the data.
    The queries to get the first data in the HTML requires that;
""" 
# Variable to store data before write to a file
allResults = []

# # # Initializing uf class to to able to set information iof de ufs...
# #ufInformations = uf_infos.UF_Infos() 
# # 
# # # Make post request to get the result html page
# # resultHTML = api.Api.getResult(url, postFields)
# # 
# # # Cleaning the data for search an set the pagination dictionary
# # resultEscapedXML = s.String_utils.cleanHTML(resultHTML)
# # 
# # # Initializing the pagination infos
# # pagination = p.Pagination(limit).getPagination(resultEscapedXML)
# # controlPage = pagination['results']
# # 
# # resultHTML = resultHTML.decode('unicode_escape') 
# # 
# # # Passing the data to BeautifulSoup for manipulation
# # soup = BeautifulSoup(resultHTML, 'lxml') 
# # 
# # # Get the rows and td data 
# # rows = t.Table.getFirstTableRowsData(soup, 'td')
# # 
# # # Transform the one dimentional array to multi, for to be able to store de each line of city info
# # rowsReshaped = t.Table.flatToMultiList(rows, 4)
# # results = []
# # for line in rowsReshaped:
# #     ufInformations.id = str(uuid4())
# #     ufInformations.localidade = line[0]
# #     ufInformations.faixaCep = line[1]
# #     ufInformations.situacao = line[2]
# #     ufInformations.tipoFaixa = line[3]
# #     results.append(ufInformations.__repr__())
# # 
# # # Filtering the results to remove duplicate cities
# # filteredList = t.Table.filteredList(results, 'localidade')
# 
# 
# filteredList, pagination = firstCallToAPI.Call_To_API.firstCall(url, postFields, limit)
# allResults.append(filteredList)
# 
# ### begin
# # def main(postFields):
# #     results = []
# # 
# #     resultHTML = api.Api.getResult(url, postFields)
# #     resultHTML = resultHTML.decode('unicode_escape') 
# #     
# #     soup =  BeautifulSoup(resultHTML, 'lxml')
# # 
# #     rows = t.Table.getTableRowsData(soup)
# # 
# # # Transform the one dimentional array to multi, for to be able to store de each line of city info
# #     rowsReshaped = t.Table.flatToMultiList(rows, 4)
# # 
# #     for line in rowsReshaped:
# #         ufInformations.id = str(uuid4())
# #         ufInformations.localidade = line[0]
# #         ufInformations.faixaCep = line[1]
# #         ufInformations.situacao = line[2]
# #         ufInformations.tipoFaixa = line[3]
# #         results.append(ufInformations.__repr__())
# # 
# # # Filtering the results to remove duplicate cities
# #     filteredList = t.Table.filteredList(results, 'localidade')
# #  
# #     return filteredList
# ### end  
# hasNext,_ =  hasNext, page  = p.Pagination.hasNext(pagination['results'], pagination['pagini'], pagination['pagfim'])
# # 
# # ## Make all of the post request to get the data 
# while hasNext:
#     postFields['pagini'] = pagination['pagini']
#     postFields['pagfim'] = pagination['pagfim']
#     hasNext, page  = p.Pagination.hasNext(pagination['results'], pagination['pagini'], pagination['pagfim'])
#     print(hasNext, page)
#     if hasNext == False:
#         pagination['pagini'] = page
#         print('PAGINATION', pagination['pagini'])
#     results = nextCallToAPI.Next_Call__To_API.nexCall(url, postFields)
#        
#     pagination['pagini'], pagination['pagfim'] = p.Pagination.pageControl2(limit, pagination['pagini'], pagination['pagfim'], pagination['results'])
# #     controlPage = controlPage - limit
#     allResults.append(results)
# # 
# print(allResults)
# #  
# with open('results.jsonl','w') as wf:
#     for data in allResults:
# #  Transform the object into a json and whrite to a file in jsonl format
#         result = [json.dumps(record) for record in data]
#         for line in result:
#             line = bytes(line, 'utf-8').decode('unicode_escape')
#             wf.write(f'{line}\n')
#              
            
for uf in UFS:
    postFields = {'UF': uf, 'Localidade': ''}
    try:
        
        filteredList, pagination = firstCallToAPI.Call_To_API.firstCall(url, postFields, limit)
        allResults.append(filteredList)
        hasNext,_ =  hasNext, page  = p.Pagination.hasNext(pagination['results'], pagination['pagini'], pagination['pagfim'])
        ## Make all of the post request to get the data 
        while hasNext:
            postFields['pagini'] = pagination['pagini']
            postFields['pagfim'] = pagination['pagfim']
            hasNext, page  = p.Pagination.hasNext(pagination['results'], pagination['pagini'], pagination['pagfim'])
            print(hasNext, page)
            if hasNext == False:
                pagination['pagini'] = page
                print('PAGINATION', pagination['pagini'])
            results = nextCallToAPI.Next_Call__To_API.nexCall(url, postFields)
        
            pagination['pagini'], pagination['pagfim'] = p.Pagination.pageControl2(limit, pagination['pagini'], pagination['pagfim'], pagination['results'])
            allResults.append(results)
  
        print(allResults)
        with open(f'{uf}_results.jsonl','w') as wf:
            for data in allResults:
                #Transform the object into a json and whrite to a file in jsonl format
                result = [json.dumps(record) for record in data]
                for line in result:
                    line = bytes(line, 'utf-8').decode('unicode_escape')
                    wf.write(f'{line}\n')
    except Exception as  error:
        print(f'Error to get data. Error {error}')
