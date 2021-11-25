from flask import Blueprint,render_template,jsonify,request
from project import db
from project.models import Course,UdemyCourseList
from project.udemy.factory import Factory
import datetime
import psycopg2

index_blueprint=Blueprint('index_page',__name__)


@index_blueprint.route('/')
def index():
    return render_template('index.html')

@index_blueprint.route('/update',methods=['POST'])
def update(): 
    factory=Factory()
    #get link from ajax POST
    originalLink=request.form['link']
    #get the platform
    platform,cleanedLink=factory.categorize(originalLink)
    #get the course ID
    courseID=factory.getCourseID(originalLink,platform)

    queryRow=Course.query.filter_by(course_id=courseID).first()
    if queryRow==None:
        current_time=datetime.datetime.now(datetime.timezone.utc)
        name,syllabus=factory.getCurriculumFromApi(courseID,originalLink,platform)
        new_course=Course(syllabus,platform,current_time,courseID)
        new_udemy_courselist=UdemyCourseList(courseID,name,cleanedLink)
        db.session.add_all([new_udemy_courselist,new_course])
        db.session.commit()
    else:
        queryName=UdemyCourseList.query.filter_by(id=courseID).first()
        name=queryName.name
        syllabus=queryRow.course.course_syllabus

    return jsonify({'name':name,'syllabus':syllabus})


@index_blueprint.route('/list')
def list_courses():
    courses=Course.query.all()
    return render_template('list_courses.html',courses=courses)
