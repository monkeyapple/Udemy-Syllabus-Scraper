from urllib.request import urlopen
from bs4 import BeautifulSoup
class Scraper():
    def __init__(self,inputURL):
        html=urlopen(inputURL)
        bs=BeautifulSoup(html.read(),'html.parser')
        div_raw=bs.find("div",{"class":"ud-component--course-landing-page-udlite--curriculum"})
        # print(inputURL[29:-1])
        return [inputURL[29:],inputURL,div_raw['data-component-props']]

# if __name__ == "__main__":
#     Scraper("https://www.udemy.com/course/rest-api-flask-and-python/")