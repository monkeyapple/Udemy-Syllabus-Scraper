from project import db
import datetime
class Course(db.Model):
    __tablename__='course'
    # course_self_id=db.Column(db.Integer,primary_key=True)
    course_id=db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    course_syllabus=db.Column(db.Text,nullable=False)
    platform_id=db.Column(db.Integer,nullable=False)
    last_update=db.Column(db.DateTime,default=datetime.timezone.utc,nullable=False)

    def __init__(self,course_id,course_syllabus,platform_id,last_update):
        self.course_id=course_id
        self.course_syllabus=course_syllabus
        self.platform_id=platform_id
        self.last_update=last_update

    def __repr__(self):
        return f"Course name is:{self.course_name}"
        
class UdemyCourseList(db.Model):
    __tablename__='udemy_courselist'
    udemy_course_id=db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    udemy_course_name=db.Column(db.String(80),nullable=False)
    udemy_course_link=db.Column(db.String(250),unique=True,nullable=False)

    def __init__(self,udemy_course_id,udemy_course_name,udemy_course_link):
        self.udemy_course_id=udemy_course_id
        self.udemy_course_name=udemy_course_name
        self.udemy_course_link=udemy_course_link

    def __repr__(self):
        return f"Udemy course id is:{self.udemy_course_id}"