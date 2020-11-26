from bs4 import BeautifulSoup 
import pandas as pd
import utility.strings as s 
import utility.api as api

url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm"
postFields = {"UF": "SC", "Localidade": ""}

test = ["UF", "SC", "Localidade", ""]
pagination = {"pagini": 0, "pagfim": 0, "results": 0, "qtdrow": 50}
table = []

class Table:
    def __init__(self):
        self.localidade = ""
        self.faixaCep = "" 
        self.situacao = ""
        self.tipoFaixa = ""
        
        
resultTeste = Table()

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
dfs = pd.read_html(resultHTML)
r = [i.values for i in dfs]
print(r)

for df in dfs:
    table.append(df)
    
for rows in df.values:
    for content in rows:
        print(content)
# print(pagination)
# 
#             
# with open("result.txt", "w") as f:
#     f.write(resultEscapedXML)



