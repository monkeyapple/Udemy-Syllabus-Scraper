from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Regexp

###################################################
##################### Form #######################
###################################################
class SearchForm(FlaskForm):
    courseLink=StringField('Enter the Udemy course URL:',validators=[Regexp('https:\/\/www\.udemy\.com\/course\/[\d*\w*\-*]{1,256}\/',message="Please enter the correct Udemy course URL!")])
    submit=SubmitField('Get it')
