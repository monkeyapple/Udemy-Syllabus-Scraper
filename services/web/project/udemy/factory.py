import requests
from bs4 import BeautifulSoup
from flask.app import Flask
import os,sys,inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from UdemyAPI.udemy import *
Client=PyUdemy()

class Factory():
    def getCourseID(self,inputURL):
        if 'udemy' in inputURL:
            platform=1
            cleanedLink=inputURL[21:]
        elif 'coursera' in inputURL:
            platform=2
            cleanedLink=inputURL[31:-1]
        bs=BeautifulSoup(requests.get(inputURL).text,'html.parser')

        #udemy
        if platform==1:
            div_raw=bs.find("body",{"id":"udemy"})

        #courera
        # elif platform==2:

        courseID=json.loads(div_raw['data-clp-course-id'])
        print('courseId is:'+str(courseID))
        return [courseID,platform,cleanedLink]
        

    def getCourseDetailsFromApi(self,courseID):
        rawResult=Client.get_coursesdetail(courseID)
        name=json.loads(rawResult)['title']
        return name

    def getCurriculumFromApi(self,courseID):
        displayArray=["# Course Syllabus"+"\n"]
        allRawResults=[]
        syllabus=None
        try:
            #set the last page to 50, error must be thrown out
            name=self.getCourseDetailsFromApi(courseID)
            for i in range(1,50):
                rawResult=Client.get_publiccurriculumlist(courseID,page=i,page_size=100)
                extractData=json.loads(rawResult)['results']
                allRawResults.extend(extractData)   
        except:
            print("error occured means reaching the last page")
        finally:
            if allRawResults!=[]:
                #Api successfully executed:
                for m in allRawResults:
                    if m['_class']=='chapter':
                        displayArray.append("### "+m['title']+"\n")
                    elif m['_class']=='lecture':
                        displayArray.append("*"+" "+m['title']+"\n")
                syllabus=''.join(displayArray)
                print("successfully fetching from API")
            else:
                print("Fail to fetching data from API")
        #####Calling the scraper is unnecessary!####
        # if syllabus==None:
        #     name,syllabus=self.markdowngenerate(inputLink,platform)
        #     print("fail fetching from API, now try to scrape")
        return (name,syllabus)

