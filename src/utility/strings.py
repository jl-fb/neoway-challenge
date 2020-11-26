# Class to concentrate some string mathods common used
class String_utils():
  
    def unescapeXML(s):  # @NoSelf
        s = s.replace("&amp;", "&")
        s = s.replace("&lt;", "<")
        s = s.replace("&gt;", ">")
        s = s.replace("&nbsp;", " ")
        return s

    def unescapeSpace(s): # @NoSelf:
        s = s.replace("\\r", '')
        s = s.replace("\\t", '')
        s = s.replace("\\n", '')
        return s
  
    def decodeUnicode(s):  # @NoSelf
        return bytes(s, "utf-8").decode("unicode_escape")

    def findInHTML(source, pattern, pos): # @NoSelf
        index = int(source.index(pattern)) + len(pattern)
        result = source[index: index + pos]
        return result
 
    def findInHTMLReverse(source, pattern, pos): # @NoSelf
        index = int(source.index(pattern)) - pos
        result = source[index: int(source.index(pattern))]
        return result
