from bs4 import BeautifulSoup 
import pandas as pd
import json
import utility.strings as s 
import utility.api as api

url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
postFields = {"UF": "SC", "Localidade": ""}

test = ["UF", "SC", "Localidade", ""]
pagination = {"pagini": 0, "pagfim": 0, "results": 0, "qtdrow": 50}
table = []
js = []
class Table:
    def __init__(self):
        self.localidade = ""
        self.faixaCep = "" 
        self.situacao = ""
        self.tipoFaixa = ""
    
    def __repr__(self):
        return '{"localidade": "%s", "faixaCep": "%s", "situacao": "%s", "tipoFaixa": "%s"}' % (self.localidade, self.faixaCep, self.situacao, self.tipoFaixa)
    
    def __out__(self):
        return self.localidade, self.faixaCep, self.situacao, self.tipoFaixa
    
data = Table()
teste = []

resultHTML = api.Api(url, postFields).getResult()

#Cleaning the data for search an set the pagination dictionary
resultEscapedSpaces = s.String_utils.unescapeSpace(str(resultHTML))
resultEscapedUnicode = s.String_utils.decodeUnicode(resultEscapedSpaces)
resultEscapedXML = s.String_utils.unescapeXML(resultEscapedUnicode)

#set the pagination variables
pagination["pagini"] = int(s.String_utils.findInHTML(resultEscapedXML, 'name=pagini value="', 2))
pagination["pagfim"] = int(s.String_utils.findInHTML(resultEscapedXML, 'name=pagfim value="', 3))
pagination["results"] = int(s.String_utils.findInHTMLReverse(resultEscapedXML, '<br><br><table class="tmptabela"', 4))

resultHTML = resultHTML.decode("unicode_escape") 

# Passing the data to BeautifulSoup for manipulation
soup = BeautifulSoup(resultHTML, 'lxml') 
#table = soup.find("table", attrs=cl)
#  
# dfs = pd.read_html(resultHTML)
# for df in dfs:
#     table.append(df)
#     
# for rows in df.values:
#     data.localidade = rows[0]
#     data.faixaCep = rows[1]
#     data.situacao = rows[2]
#     data.tipoFaixa = rows[3]
#     js.append(data.__repr__())
# 
# with open("table.jsonl", "w") as wf:
#     for data in js:
#         wf.write(f"{data}\n")
        
# result = [json.dumps(record) for record in js]
# with open("table.jsonl", "w") as wf:
#     for line in result:
#         line = bytes(line, "utf-8").decode("unicode_escape")
#         print(f"{line}\n")
#         wf.write(f"{line}\n")
#     
#print(pagination)

print() 