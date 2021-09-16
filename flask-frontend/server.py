from flask import Flask,session,redirect,jsonify,request,redirect,url_for,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,Regexp
from scraper import Scraper
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:854823@localhost/course_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db)

class CourseContent(db.Model):
    __tablename__='coursecontent'
    course_id=db.Column(db.Integer,primary_key=True)
    course_name=db.Column(db.String(80),nullable=False)
    course_link=db.Column(db.String(250),unique=True,nullable=False)
    course_content=db.Column(db.String(80))

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
        result=[]
        link=form.course_link.data
        queryRow=CourseContent.query.filter_by(course_link=link).first()
        if queryRow:
            result=[queryRow.course_name,queryRow.course_content]
        else:
            db.session.add()



        return redirect(url_for('index'))
    return render_template('index.html',form=form,urlQuery=session.get('courseLink',None))

@app.route('/scrape')
def scrape():
   
    scrapeData=Scraper('https://www.udemy.com/course/rest-api-flask-and-python/')
    print(scrapeData)
    time.sleep(10)
    # return jsonify(scrapeData)

@app.route('/list')
def list_courses():
    courses=CourseContent.query.all()
    return render_template('list_courses',courses=courses)

if __name__=='__main__':
    app.run(debug=True)
