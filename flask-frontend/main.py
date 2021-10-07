from flask import Flask,session,redirect,jsonify,request,redirect,url_for,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,Regexp
from scraper import Scraper
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
# from config import config
from flaskext.markdown import Markdown
from db import read_config,connection_uri

app=Flask(__name__)
Markdown(app)

app.config['SECRET_KEY']='onlinecoursesecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################

DB_URI = connection_uri()

app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class CourseContent(db.Model):
    __tablename__='coursecontent'
    course_id=db.Column(db.Integer,primary_key=True)
    course_name=db.Column(db.String(80),nullable=False)
    course_link=db.Column(db.String(250),unique=True,nullable=False)
    course_content=db.Column(db.Text)

    def __init__(self,course_name,course_link,course_content):
        self.course_name=course_name
        self.course_link=course_link
        self.course_content=course_content


    def __repr__(self):
        return f"Course name is:{self.course_name}"

###################################################
##################### Form #######################
###################################################
class SearchForm(FlaskForm):
    courseLink=StringField('Enter the Udemy course URL:',validators=[Regexp('https:\/\/www\.udemy\.com\/course\/[\d*\w*\-*]{1,256}\/',message="Please enter the correct Udemy course URL!")])
    submit=SubmitField('Get it')

###################################################
###################### View #######################
###################################################

@app.route('/',methods=['GET','POST'])
def index():

    form=SearchForm()
    if form.validate_on_submit():
        link=form.courseLink.data
        queryRow=CourseContent.query.filter_by(course_link=link).first()
        if queryRow:
            displayResult=[queryRow.course_name,queryRow.course_content]
        else:
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
            displayResult=[link[29:-1],contentResult]
            new_courseContent=CourseContent(link[29:-1],link,contentResult)
            db.session.add(new_courseContent)
            db.session.commit()
        session['result']=displayResult

        return redirect(url_for('index'))
    return render_template('index.html',form=form,display=session.get('result',['-Course Name-','The course content will be displayed here...']))


@app.route('/list')
def list_courses():
    courses=CourseContent.query.all()
    return render_template('list_courses.html',courses=courses)

if __name__=='__main__':
    app.run(debug=True)
