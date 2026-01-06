import requests
import re
import os,sys,inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from UdemyAPI.udemy import *
Client=PyUdemy()

class Factory():
    def getCourseID(self,inputURL):
        if 'udemy' not in inputURL:
            raise Exception("Only Udemy URLs are supported")

        platform = 1
        # Extract slug from URL: https://www.udemy.com/course/SLUG/
        parts = inputURL.split('/course/')
        if len(parts) < 2:
            raise Exception("Invalid Udemy URL format")

        slug = parts[1].strip('/').split('/')[0].split('?')[0]
        cleanedLink = f"/course/{slug}/"

        # Scrape course ID from page's CDN image URLs
        # Pattern: udemycdn.com/course/{size}/{course_id}_...
        try:
            response = requests.get(inputURL, timeout=30)
            if response.status_code == 200:
                # Extract course ID from CDN image URLs
                match = re.search(r'udemycdn\.com/course/[^/]+/(\d+)', response.text)
                if match:
                    courseID = int(match.group(1))
                    return [courseID, platform, cleanedLink]
        except Exception as e:
            print(f"Scraping failed: {e}")

        raise Exception(f"Could not find course ID for: {slug}")
        

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

