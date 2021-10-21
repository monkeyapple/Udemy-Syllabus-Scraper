import re
class Validator():
    def validate_check(self,inputString):
        regex=re.compile('https:\/\/www\.udemy\.com\/course\/[\d*\w*\-*]{1,256}\/',re.I)
        match=regex.match(inputString)
        return bool(match)