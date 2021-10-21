from flask import Blueprint,session,redirect,redirect,url_for,render_template
from project import db
from project.models import CourseContent
from project.udemy.forms import SearchForm
from project.udemy.scraper import Scraper
from project.udemy.validator import Validator
import time


index_blueprint=Blueprint('index_page',__name__)

###################################################
###################### View #######################
###################################################

@index_blueprint.route('/')
def index():
    return render_template('index.html')

@index_blueprint.route('/update',methods=['POST'])
def update():
    validator=Validator()
    link=request.form['link']
    if validator.validate_check(link):
        queryRow=CourseContent.query.filter_by(course_link=link).first()
        if queryRow==None:
            scraper=Scraper()
            displayArray=["# Course content"+"\n"]
            scrapedData=scraper.scrape(link)
            time.sleep(5)
            for i in scrapedData:
                for k,v in i.items():
                    displayArray.append("### "+k+"\n")
                    for m in v:
                        displayArray.append("*"+" "+m+"\n")
            contentResult=''.join(displayArray)
            name=link[29:-1]
            content=contentResult
            new_courseContent=CourseContent(link[29:-1],link,contentResult)
            db.session.add(new_courseContent)
            db.session.commit()
        else:
            name=queryRow.course_name
            content=queryRow.course_content

        return jsonify({'name':name,'content':content})
    return jsonify({'error':'Please enter the correct Udemy course URL!'})

@index_blueprint.route('/list')
def list_courses():
    courses=CourseContent.query.all()
    return render_template('list_courses.html',courses=courses)
