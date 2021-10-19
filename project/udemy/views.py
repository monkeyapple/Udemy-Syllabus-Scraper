from flask import Blueprint,session,redirect,jsonify,request,redirect,url_for,render_template
from project import db
from project.models import CourseContent
from project.udemy.forms import SearchForm
from project.udemy.scraper import Scraper
import time

index_blueprint=Blueprint('index_page',__name__)

###################################################
###################### View #######################
###################################################

@index_blueprint.route('/',methods=['GET','POST'])
def index():
    form=SearchForm()
    if form.validate_on_submit():
        link=form.courseLink.data
        queryRow=CourseContent.query.filter_by(course_link=link).first()
        if queryRow==None:
            scraper=Scraper()
            displayArray=["# Course content"+"\n"]
            scrapedData=scraper.scrape(link)
            time.sleep(6)
            for i in scrapedData:
                for k,v in i.items():
                    displayArray.append("### "+k+"\n")
                    for m in v:
                        displayArray.append("*"+" "+m+"\n")
            contentResult=''.join(displayArray)
            session['name']=link[29:-1]
            session['content']=contentResult
            new_courseContent=CourseContent(link[29:-1],link,contentResult)
            db.session.add(new_courseContent)
            db.session.commit()
        else:
            session['name']=queryRow.course_name
            session['content']=queryRow.course_content

        return redirect(url_for('index_page.index'))
    return render_template('index.html',form=form,name=session.get('name','-Course Name-'),content=session.get('content','The course content will be displayed here...'))



@index_blueprint.route('/list')
def list_courses():
    courses=CourseContent.query.all()
    return render_template('list_courses.html',courses=courses)
