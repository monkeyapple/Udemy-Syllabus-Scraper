from project import db
import datetime

class UdemyCourseList(db.Model):
    __tablename__='udemy_courselist'
    id=db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    name=db.Column(db.String(80),nullable=False)
    link=db.Column(db.String(250),unique=True,nullable=False)
    course=db.relationship('Course',backref='udemy_courselist',uselist=False)
    searchcount=db.Column(db.Integer,nullable=False)
    def __init__(self,id,name,link,searchcount):
        self.id=id
        self.name=name
        self.link=link
        self.searchcount=searchcount
    def __repr__(self):
        if self.course:
            return f"Course id is {self.id} and updated at{self.course.last_update}"
        else:
            return f"Course id {self.id} hasn't updated yet "

class Course(db.Model):
    __tablename__='course'
    course_id=db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    course_syllabus=db.Column(db.Text,nullable=False)
    platform_id=db.Column(db.Integer,nullable=False)
    last_update=db.Column(db.DateTime,default=datetime.timezone.utc,nullable=False)
    udemy_course_id=db.Column(db.Integer,db.ForeignKey('udemy_courselist.id'))


    def __init__(self,course_syllabus,platform_id,last_update,udemy_course_id):
        self.course_syllabus=course_syllabus
        self.platform_id=platform_id
        self.last_update=last_update
        self.udemy_course_id=udemy_course_id


    def __repr__(self):
        return f"Course name is:{self.course_name}"
        
