from flask import Flask,session,redirect,jsonify,request,redirect,url_for,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,Regexp

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

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
        session['courseLink']=form.courseLink.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,urlQuery=session.get('courseLink',None))

def submit():
    pass

def scrape():
    pass

if __name__=='__main__':
    app.run(debug=True)
