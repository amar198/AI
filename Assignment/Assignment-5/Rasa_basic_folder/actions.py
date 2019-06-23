from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd		# for checking the city names
import re 				# for checking email format

#Action class is the parent class. Inheritance.
class ActionSearchRestaurants(Action):	#This name is given in domain file.
	def name(self):
		return 'action_restaurant'	#This is the name which is given in the stories file.
		
	def run(self, dispatcher, tracker, domain):
		config={ 'user_key':'f8e764632db822d8f7cac3254c5f8af3'}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		mlat=d1['location_suggestions'][0]['latitude']
		mlon=d1['location_suggestions'][0]['longitude']

		#TODO: understand why cuisine is sent this way, because the response does not contain any such dictionary
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}

		# The last parameter indicates that we are looking for top 10 results.
		results=zomato.restaurant_search('', mlat, mlon, str(cuisines_dict.get(cuisine)), 10)
		# results=zomato.restaurant_search(query='', lat=mlat, lon=mlon, cuisine=str(cuisines_dict.get(cuisine)), limit=10)
		d = json.loads(results)

		iChatResponse=0 #Variable used for counting 5 restaurants. To show in the chat. For email all 10 responses will be sent.

		chat_response=''		#variable used for showing chat response
		email_response=''		#variable used for showing email response
		zpy_response=[[]*2] 	#variable to capture response from Zomato API, using a 2 dimensional list.
								#column 1 will store the response, and 2 will store the rating. Will use this column for sorting.
		row, column = 0

		# TODO 1: Add code for sorting restaurant output as per rating (descending)
		if d['results_found'] == 0:
			chat_response 	= 'We do not operate in this city yet'
			email_response 	= 'no results found'
			zpy_response 	= 'We do not operate in this city yet'
		else:
			for restaurant in d['restaurants']:
				#
				if iChatResponse <5:
					chat_response=chat_response + 'Found ' + restaurant['restaurant']['name'] + ' in ' + restaurant['restaurant']['location']['address'] + ' has been rated ' + restaurant['restaurant']['user_rating']['aggregate_rating'] + '\n'
					iChatResponse = iChatResponse+1
				
				email_response=email_response + 'Found ' + restaurant['restaurant']['name'] + ' in ' + restaurant['restaurant']['location']['address'] + ' has been rated ' + restaurant['restaurant']['user_rating']['aggregate_rating'] + '\n'

				#TODO: update below code as it is not in correct python syntax.
				#TODO: study basic python syntax... pathetic amar pathetic...
				#storing the restaurant name and rating in the zpy_response variable.
				#zpy_response[row][column] = 'Found ' + restaurant['restaurant']['name'] + ' in ' + restaurant['restaurant']['location']['address'] + ' has been rated ' + restaurant['restaurant']['user_rating']['aggregate_rating']
				#column=column+1
				#zpy_response[row][column] = restaurant['restaurant']['user_rating']['aggregate_rating']
				#row=row+1
				
		#sortRestRatingWise(zpy_response)
		
		dispatcher.utter_message('-----'+chat_response)

		#TODO 2: Remove this code before submission
		# code to write result in a file on local drive
		#f= open('result-restaurant-search.json','w+')
		#f.write(results)
		#f.close
		#-----------------------------------------------
		
		return [SlotSet('location',loc)]
	
	
	#def sortRestRatingWise(chatResponse):		--Amar to do
		#TODO: check how to create a 2D array in python and assign values in different cells.
		#tempStr = [[]*2]
		#
		#for i in range(10):
		#
		#return chatResponse


#--------------------------------------------------------------------------------------------------------------------------
# TODO 3: Add action for checking if the city belongs to Tier-1 or Tier-2 city.		--Aadhya will do.
class CityCheck(Action):
	def name(self):
		return 'city_check'	#This is the name which is given in the stories file.

	def run(self, dispatcher, tracker, domain):
		cities = pd.read_csv('city-list.csv')			#reading the city-list.csv file.
		slot_city_name = tracker.get_slot('location')	#fetching the location entered by user and saved in location slot.

		#checking if city name exist in tier1/2 list
		#TODO REFACTOR: check if this code can be optimized / written in a better way.
		pd_city_name = (cities.loc[cities['city_name'].str.lower() == slot_city_name.str.lower()]).city_name

		#if no records found then send message to the use else nothing
		if len(pd_city_name) == 0:
			dispatcher.utter_message('We do not operate in this city yet.')

		#setting the location slot with the value provided by the user.
		return [SlotSet('location',slot_city_name)]


#--------------------------------------------------------------------------------------------------------------------------
# TODO 4: Add action for checking if the mail id provided is correct or not.		--Amar will do.
class CheckEmailFormat(Action):
	def name(self):
		return 'email_check'	#This is the name which is given in the stories file.

	def run(self, dispatcher, tracker, domain):
		#fetching the email entered by user and saved in email slot.
		slot_email = tracker.get_slot('email')

		#RegEx query to check for email format. Should provide at least 2 matches.
		#TODO REFACTOR: check if this regex can be written in a better way.
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', slot_email)

		if match == None:
			dispatcher.utter_message('Invalid email id. Please provide a valid email id.')

		return [SlotSet('email', slot_email)]


#--------------------------------------------------------------------------------------------------------------------------
# TODO 5: Add action for sending mail.												--Sasi will do.

