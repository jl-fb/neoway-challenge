from bs4 import BeautifulSoup

class Table:
    
    def getTable(soup, tag, class_="tmptabela"): # @NoSelf
        try:
            return soup.find(tag, class_)
        except Exception as error:
            print(f'[Table_class] Error to find table rows. Error {error}')
   
    def findAllTableRows(table): # @NoSelf
        try:
            return table.find_all("tr")
        except Exception as error:
            print(f'[Table_class] Error to find table rows. Error {error}')

    def getTableRowsData(soup, tag): # @NoSelf
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