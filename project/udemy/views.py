from flask import Blueprint,render_template,jsonify,request
from project import db
from project.models import Course
from project.udemy.factory import Factory
import datetime

index_blueprint=Blueprint('index_page',__name__)


@index_blueprint.route('/')
def index():
    return render_template('index.html')

@index_blueprint.route('/update',methods=['POST'])
def update():
    factory=Factory()
    #get link from ajax POST
    originalLink=request.form['link']

    #call the categorize()
    platform,link=factory.categorize(originalLink)

    queryRow=Course.query.filter_by(course_link=link).first()
    if queryRow==None:
        name,syllabus=factory.markdowngenerate(originalLink)
        current_time=datetime.datetime.now(datetime.timezone.utc)
        new_course=Course(name,link,syllabus,platform,current_time)
        db.session.add(new_course)
        db.session.commit()
    else:
        name=queryRow.course_name
        syllabus=queryRow.course_syllabus

    return jsonify({'name':name,'syllabus':syllabus})


@index_blueprint.route('/list')
def list_courses():
    courses=Course.query.all()
    return render_template('list_courses.html',courses=courses)
