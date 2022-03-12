from flask import Blueprint,render_template,jsonify,request
from project import db
from project.models import Course,UdemyCourseList
from project.udemy.factory import Factory
import datetime
import psycopg2

index_blueprint=Blueprint('index_page',__name__)


@index_blueprint.route('/')
def index():
    recentSearches=[]
    recentQuery=Course.query.order_by(Course.last_update.desc()).limit(10).all()
    for row in recentQuery:
        recentSearches.append((row.udemy_courselist.name,row.udemy_courselist.link))
    length=len(recentSearches)
    if length<10:
        recentSearches.extend([('No enough data','#')]*(10-length)) 
    return render_template('index.html',recentSearches=recentSearches)

@index_blueprint.route('/update',methods=['POST'])
def update(): 
    factory=Factory()
    #get link from ajax POST
    originalLink=request.form['link']
    #get the course ID,platform, and cleanedLink
    results=factory.getCourseID(originalLink)
    courseID,platform,cleanedLink=results[0],results[1],results[2]
    queryUdemyCourseListRow=UdemyCourseList.query.filter_by(id=courseID).first()

    if queryUdemyCourseListRow==None:
        current_time=datetime.datetime.now(datetime.timezone.utc)
        name,syllabus=factory.getCurriculumFromApi(courseID)
        new_course=Course(syllabus,platform,current_time,courseID)
        new_udemy_courselist=UdemyCourseList(courseID,name,cleanedLink,1)
        db.session.add_all([new_udemy_courselist,new_course])
        db.session.commit()
    else: 
        name=queryUdemyCourseListRow.name
        syllabus=queryUdemyCourseListRow.course.course_syllabus
        existedRow=UdemyCourseList.query.get(courseID)
        existedRow.searchcount=existedRow.searchcount+1
        db.session.commit()
    return jsonify({'name':name,'syllabus':syllabus})


@index_blueprint.route('/list')
def list_courses():
    courses=Course.query.all()
    return render_template('list_courses.html',courses=courses)
