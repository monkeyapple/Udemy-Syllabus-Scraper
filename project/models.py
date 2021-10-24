from project import db
import datetime
class Course(db.Model):
    __tablename__='course'
    course_id=db.Column(db.Integer,primary_key=True)
    course_name=db.Column(db.String(80),nullable=False)
    course_link=db.Column(db.String(250),unique=True,nullable=False)
    course_syllabus=db.Column(db.Text,nullable=False)
    platform_id=db.Column(db.Integer,nullable=False)
    last_update=db.Column(db.DateTime,default=datetime.timezone.utc,nullable=False)


    def __init__(self,course_name,course_link,course_syllabus,platform_id,last_update):
        self.course_name=course_name
        self.course_link=course_link
        self.course_syllabus=course_syllabus
        self.platform_id=platform_id
        self.last_update=last_update


    def __repr__(self):
        return f"Course name is:{self.course_name}"