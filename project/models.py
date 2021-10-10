from project import db
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