from bs4 import BeautifulSoup
from numpy import reshape, array

class Table:
    
    def getTableByClass(soup, class_='tmptabela'): # @NoSelf
        try:
            return soup.find('table', class_)
        except Exception as error:
            print(f'[Table_class] Error to find table rows. Error {error}')
    
    def getTableByID(soup, id_='resultado-DNEC'): # @NoSelf
        try:
            return soup.find('table', id_)
        except Exception as error:
            print(f'[Table_class] Error to find table rows. Error {error}')
   
   
    def findAllTableRows(table): # @NoSelf
        try:
            return table.find_all('tr')
        except Exception as error:
            print(f'[Table_class] Error to find table rows. Error {error}')

    def getFirstTableRowsData(soup, tag): # @NoSelf
        try:
            first_td = soup.find(tag)
            nexts_tds = first_td.find_all_next(tag)
            tds = BeautifulSoup(str(nexts_tds), "lxml")
            second_td = tds.find(tag)
            last_tds = second_td.find_all_next(tag)
            rows = [data.text for data in last_tds]
        except Exception as error:
            print(f'[Table_class] Error to get table rows. Error {error}')
        else:
            return rows
    
    def getTableRowsData(soup): # @NoSelf
        try:
            td = soup.find_all('td')
            rows = [i.text for i in td]
        except Exception as error:
            print(f'[Table_class] Error to get table rows. Error {error}')
        else:
            return rows
    
    def flatToMultiList(source,  size): # @NoSelf
        try:
            narray = array(source)
            slices = round(len(source) / size)
            return reshape(narray, (slices, size))
        
        except Exception as error:
            print(f'[Table_class] Error to transform list. Error {error}') 
        
    def filteredList(source, pattern): # @NoSelf
        res = []
        temp = []
        try:
            for i in source:
                if i[pattern] not in res:
                    res.append(i[pattern])
                    temp.append(i)
            return temp
        
        except Exception as error:
            print(f'[Table_class] Error to filter list. Error {error}')