from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://www.udemy.com/course/complete-python-bootcamp/')
bs=BeautifulSoup(html.read(),'html.parser')
div_raw=bs.find("div",{"class":"ud-component--course-landing-page-udlite--curriculum"})
print(div_raw['data-component-props'])
