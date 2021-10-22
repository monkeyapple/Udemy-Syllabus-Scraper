from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json
import copy
class Factory():
    def scrape(self,inputURL):
        html=urlopen(inputURL)
        bs=BeautifulSoup(html.read(),'html.parser')
        div_raw=bs.find("div",{"class":"ud-component--course-landing-page-udlite--curriculum"})
        courseTitle=bs.find("h1",{"data-purpose":"lead-title"}).get_text()
        courseTitle=courseTitle.strip()
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
        return (headerOne,courseTitle)

    def categorize(self,inputLink):
        if 'udemy' in inputLink:
            platform=1
            cleanedLink=inputLink[29:-1]
        elif 'coursera' in inputLink:
            platform=2
            cleanedLink=inputLink[31:-1]
        return (platform,cleanedLink)

    def markdowngenerate(self,inputLink):
        displayArray=["# Course Syllabus"+"\n"]
        scrapedResult=self.scrape(inputLink)
        scrapedsyllabusData=scrapedResult[0]
        time.sleep(5)
        for i in scrapedsyllabusData:
            for k,v in i.items():
                displayArray.append("### "+k+"\n")
                for m in v:
                    displayArray.append("*"+" "+m+"\n")
        contentSyllabus=''.join(displayArray)
        name=scrapedResult[1]
        syllabus=contentSyllabus
        return (name,syllabus)
