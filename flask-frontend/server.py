from flask import Flask,session,redirect,jsonify,request,redirect,url_for,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,Regexp
from scraper import Scraper
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
params=config()
DB_URI = 'postgresql+psycopg2://{user}:{pw}@{host}/{db}'.format(
    user=config['udemy-scrape-postgresql']['user'],
    pw=config['udemy-scrape-postgresql']['password'],
    host=config['udemy-scrape-postgresql']['host'],
    db=config['udemy-scrape-postgresql']['dbname'])

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
    courseLink=StringField('Enter the course URL:',validators=[Regexp('https:\/\/www\.udemy\.com\/course\/[\d*\w*\-*]{1,256}\/',message="Please enter the correct Udemy course URL!")])
    submit=SubmitField('Search')

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
            displayResult=[queryRow.course_content]
            # queryRow.course_name,queryRow.course_link
        else:
            scraper=Scraper()
            displayArray=["# Table of Contents\n"]
            scrapedData=scraper.scrape(link)
            time.sleep(6)
            for i in scrapedData:
                for k,v in i.items():
                    displayArray.append("## "+k+"\n")
                    for m in v:
                        displayArray.append("### "+m+"\n")
            displayResult=''.join(displayArray)
            new_courseContent=CourseContent(link[29:],link,displayResult)
            db.session.add(new_courseContent)
            db.session.commit()
        session['result']=displayResult
        return redirect(url_for('index'))
    return render_template('index.html',form=form,display=session.get('result',None))


@app.route('/list')
def list_courses():
    courses=coursecontent.query.all()
    return render_template('list_courses',courses=courses)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
