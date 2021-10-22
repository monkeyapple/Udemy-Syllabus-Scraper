from project import db
class Course(db.Model):
    __tablename__='course'
    course_id=db.Column(db.Integer,primary_key=True)
    course_name=db.Column(db.String(80),nullable=False)
    course_link=db.Column(db.String(250),unique=True,nullable=False)
    course_syllabus=db.Column(db.Text)
    platform_id=db.Column(db.Integer)


    def __init__(self,course_name,course_link,course_syllabus,platform_id):
        self.course_name=course_name
        self.course_link=course_link
        self.course_syllabus=course_syllabus
        self.platform_id=platform_id


    def __repr__(self):
        return f"Course name is:{self.course_name}"