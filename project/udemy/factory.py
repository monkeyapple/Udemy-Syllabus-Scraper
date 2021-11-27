from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask.app import Flask
import os,sys,inspect
import time
import json
import copy

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from UdemyAPI.udemy import *
Client=PyUdemy()

class Factory():
    def scrape(self,inputURL,platform):
        html=urlopen(inputURL)
        bs=BeautifulSoup(html.read(),'html.parser')
        #udemy
        if platform==1:
            div_raw=bs.find("div",{"class":"ud-component--course-landing-page-udlite--curriculum"})
            courseTitle=bs.find("h1",{"data-purpose":"lead-title"}).get_text()
        #courera
        # elif platform==2:
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

    def markdowngenerate(self,inputLink,platform):
        displayArray=["# Course Syllabus"+"\n"]
        scrapedResult=self.scrape(inputLink,platform)
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

    def categorize(self,inputLink):
        #Example: 
        #inputLink='https://www.udemy.com/course/coursename/' 
        #result:'/course/coursename/'
        if 'udemy' in inputLink:
            platform=1
            cleanedLink=inputLink[21:]
        elif 'coursera' in inputLink:
            platform=2
            cleanedLink=inputLink[31:-1]
        return (platform,cleanedLink)


    def getCourseID(self,inputURL,platform):
        html=urlopen(inputURL)
        bs=BeautifulSoup(html.read(),'html.parser')
        #udemy
        if platform==1:
            div_raw=bs.find("div",{"class":"ud-component--course-landing-page-udlite--instructors"})

        #courera
        # elif platform==2:

        courseID=(json.loads(div_raw['data-component-props']))['course_id']
        return courseID

    def getCourseDetailsFromApi(self,courseID):
        rawResult=Client.get_coursesdetail(courseID)
        name=json.loads(rawResult)['title']
        return name

    def getCurriculumFromApi(self,courseID,inputLink,platform):
        displayArray=["# Course Syllabus"+"\n"]
        allRawResults=[]
        syllabus=None
        try:
            #set the last page to 5, error must be thrown out
            name=self.getCourseDetailsFromApi(courseID)
            for i in range(1,5):
                rawResult=Client.get_publiccurriculumlist(courseID,page=i,page_size=100)
                allRawResults.append(json.loads(rawResult)['results'])  
        except:
            #if Api successfully executed:
            for m in allRawResults[0]:
                if m['_class']=='chapter':
                    displayArray.append("### "+m['title']+"\n")
                elif m['_class']=='lecture':
                    displayArray.append("*"+" "+m['title']+"\n")
            syllabus=''.join(displayArray)
        if syllabus==None:
            #if Api get nothing:
            name,syllabus=self.markdowngenerate(inputLink,platform)
        return (name,syllabus)

