import json
import utility.pagination as p
import utility.constant as constant
from functions import firstCallToAPI, nextCallToAPI

UFS = constant.UFS
url = constant.URL 
postFields = {'UF': 'TO', 'Localidade': ''}
limit = constant.LIMIT

"""
    The first request need to be made in separeted of another because of 
    the model of the Correios's site and the way I've make the functions to get the data.
    The queries to get the first data in the HTML requires that;
""" 
# Variable to store data before write to a file
allResults = []

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
