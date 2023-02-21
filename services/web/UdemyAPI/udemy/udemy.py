import requests
import os
from requests.auth import HTTPBasicAuth

class PyUdemyException(Exception):
	''' Custom exception class for the module!  '''
	pass

class PyUdemy(object):
	__apiroot = 'https://www.udemy.com/api-2.0/'
	__clientID = None
	__clientSecret = None
	__auth = None
	def __init__(self,*args, **kwargs):
		''' We either get the clientID and clientSecret from OS environment variable or as keyword arguments '''		
		if len(kwargs) == 0:
			if os.getenv('udemyClientID'):
				self.__clientID = os.getenv('udemyClientID')
			else:
				raise PyUdemyException('The argument clientID was not specified, aborting!')

			if os.getenv('udemyClientSecret'):
				self.__clientSecret = os.getenv('udemyClientSecret')	
			else:
				raise PyUdemyException('The argument clientSecret was not specified, aborting!')


		elif len(kwargs) == 2:
			if kwargs.get('clientID'):
				self.__clientID = kwargs['clientID']
			else:
				raise PyUdemyException('The argument clientID was not specified, aborting!')

			if kwargs.get('clientSecret'):
				self.__clientSecret = kwargs['clientSecret']
			else:
				raise PyUdemyException('The argument clientSecret was not specified, aborting!')

		self.__auth = HTTPBasicAuth(self.__clientID, self.__clientSecret)		
	

	def __str__(self):
		''' Override of str function, be careful! '''
		return f"{self.__class__.__name__}(clientID = {self.__clientID}, clientSecret = {self.__clientSecret})"

	def __format__(self,r):
		''' Override of format function, be careful! '''
		return f"{self.__class__.__name__}(clientID = {self.__clientID}, clientSecret = {self.__clientSecret})"

	def __repr__(self):
		''' Override of repr function, be careful! '''
		return f"{self.__class__.__name__}(clientID = {self.__clientID}, clientSecret = {self.__clientSecret})"

	def __unicode__(self):
		''' Override of unicode function, be careful! '''
		return f"{self.__class__.__name__}(clientID = {self.__clientID}, clientSecret = {self.__clientSecret})"



	def get_courseslist(self, **kwargs):
		''' Returns the list of courses available on udemy, you may use keywords to filter! '''
		allowedKwargs = ['page','page_size','search','category','subcategory','price','is_affiliate_agreed','is_fixed_priced_deals_agreed','is_percentage_deals_agreed','language','has_closed_caption','has_coding_exercises','has_simple_quiz','instructional_level','ordering','ratings','duration']
		if len(kwargs) != 0:
			for key in kwargs.keys():
				if not key in allowedKwargs:
					raise PyUdemyException("The specified keyword is not allowed: {}, allowed are: {}".format(key,','.join(allowedKwargs)))
			query = '&'.join(["{}={}".format(key, kwargs[key]) for key in kwargs.keys()])
		else:
			query = None

		try:
			if query:
				url = self.__apiroot + f"courses/?{query}" 
			else:
				url = self.__apiroot + f"courses/"
			response = requests.get(url = url, auth = self.__auth)
		except:
			raise PyUdemyException('Could not communicate with the API!')

		if response.status_code == 200:
			return response.text
		else:
			raise PyUdemyException(f"The status code was: {response.status_code}!")
	def get_coursesdetail(self, courseID):
		''' This function will return the details of the specified course ID! '''
		try:
			response = requests.get(url = self.__apiroot + f"courses/{courseID}/", auth = self.__auth)
		except:
			raise PyUdemyException('Could not communicate with the API!')

		if response.status_code == 200:
			return response.text
		else:
			raise PyUdemyException(f"The status code was: {response.status_code}!")

	def get_coursesreviewlist(self, courseID, **kwargs):
		''' Returns the specified courses reviews, filters can be specified. '''
		allowedKwargs = ['page','page','is_text_review','rating','user']
		if len(kwargs) != 0:
			for key in kwargs.keys():
				if not key in allowedKwargs:
					raise PyUdemyException("The specified keyword is not allowed: {}, allowed are: {}".format(key,','.join(allowedKwargs)))
			query = '&'.join(["{}={}".format(key, kwargs[key]) for key in kwargs.keys()])
		else:
			query = None

		try:
			if query:
				url = self.__apiroot + f"courses/{courseID}/reviews/?{query}" 
			else:
				url = self.__apiroot + f"courses/{courseID}/reviews/"
			response = requests.get(url = url, auth = self.__auth)
		except:
			raise PyUdemyException('Could not communicate with the API!')

		if response.status_code == 200:
			return response.text
		else:
			raise PyUdemyException(f"The status code was: {response.status_code}!")

	def get_publiccurriculumlist(self,courseID, **kwargs):
		''' Returns the public curriculum list of a specified curse, filtered by arguments. '''
		allowedKwargs = ['page','page_size']
		if len(kwargs) != 0:
			for key in kwargs.keys():
				if not key in allowedKwargs:
					raise PyUdemyException("The specified keyword is not allowed: {}, allowed are: {}".format(key,','.join(allowedKwargs)))
			query = '&'.join(["{}={}".format(key, kwargs[key]) for key in kwargs.keys()])
		else:
			query = None

		try:
			if query:
				url = self.__apiroot + f"courses/{courseID}/public-curriculum-items/?{query}" 
			else:
				url = self.__apiroot + f"courses/{courseID}/public-curriculum-items/"
			response = requests.get(url = url, auth = self.__auth)
		except:
			raise PyUdemyException('Could not communicate with the API!')

		if response.status_code == 200:
			return response.text
		else:
			raise PyUdemyException(f"The status code was: {response.status_code}!")