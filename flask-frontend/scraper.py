from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json
import copy
class Scraper():
    def __init__(self,inputURL):
        html=urlopen(inputURL)
        bs=BeautifulSoup(html.read(),'html.parser')
        div_raw=bs.find("div",{"class":"ud-component--course-landing-page-udlite--curriculum"})
        headerOne=[]
        headerTwo=[]
        selection=(json.loads(div_raw['data-component-props']))['sections']
        for idx,i in enumerate(selection):
            headerOne.append({i['title']:None})
            for m in i['items']:
                headerTwo.append(m['title'])
            arrayValue=copy.deepcopy(headerTwo)
            headerOne[idx][i['title']]=arrayValue
            headerTwo.clear()
        return headerOne
        
    
# if __name__ == "__main__":
#     Scraper("https://www.udemy.com/course/rest-api-flask-and-python/")