# Class to concentrate some string mathods common used
class String_utils():
  
    def unescapeXML(s):  # @NoSelf
        try:
            s = s.replace('&amp;', '&')
            s = s.replace('&lt;', '<')
            s = s.replace('&gt;', '>')
            s = s.replace('&nbsp;', ' ')
        except Exception as error: 
            print(f'[String_utils_class] Error in unescapeXML: Error: {error}')
        else: 
            return s

    def unescapeSpace(s): # @NoSelf:
        try:
            s = s.replace('\\r', '')
            s = s.replace('\\t', '')
            s = s.replace('\\n', '')
        except Exception as error:
            print(f'[String_utils_class] Error in unescapeSpace: Error: {error}')
        else:
            return s
  
    def decodeUnicode(s):  # @NoSelf
        try:
            decode = bytes(s, 'utf-8').decode('unicode_escape')
        except Exception as error:
            print(f'[String_utils_class] Error in decodeUnicode: Error: {error}')
        else:
            return decode
        
    def findInHTML(source, pattern, pos): # @NoSelf
        try:   
            index = int(source.index(pattern)) + len(pattern)
            result = source[index: index + pos]
        except Exception as error:
            print(f'[String_utils_class] Error in findInHTML: Error: {error}')
        else:
            return result
 
    def findInHTMLReverse(source, pattern, pos): # @NoSelf
        try:
            index = int(source.index(pattern)) - pos
            result = source[index: int(source.index(pattern))]
        except Exception as error:
            print(f'[String_utils_class] Error in findInHTMLReverse: Error: {error}')
        else:    
            return result
        
    def cleanHTML(html): # @NoSelf
        try:    
            #Cleaning the data for search an set the pagination dictionary
            resultEscapedSpaces = String_utils.unescapeSpace(str(html))
            resultEscapedUnicode = String_utils.decodeUnicode(resultEscapedSpaces)
            resultEscapedXML = String_utils.unescapeXML(resultEscapedUnicode)
        
        except Exception as error:
            print(f'[String_utils_class] Error in clean the HTML: Error: {error}')
        
        else:
            return resultEscapedXML
        