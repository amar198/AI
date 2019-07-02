from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd		# for checking the city names
import re 				# for checking email format

# for sending emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Action class is the parent class. Inheritance.
class ActionSearchRestaurants(Action):	#This name is given in domain file.
	def name(self):
		return 'action_restaurant'	#This is the name which is given in the stories file.
		
	def run(self, dispatcher, tracker, domain):
		#-------------------------------------------------------------------------------------------------------------------------------
		# variable used for tracking the state of the request, which will help in showing a correct message to the user
		request_state = ''

		# Variable used for counting 5 and 10 restaurants for chat and email respectively.
		iChatResponse = 0
		iEmailResponse = 0

		# variables used for storing restaurants output
		chat_response = ''
		email_response = ''

		# Variable to refactor budget & response code
		isValidRestaurant = False
		#-------------------------------------------------------------------------------------------------------------------------------

		config={ 'user_key':'f8e764632db822d8f7cac3254c5f8af3'}
		zomato = zomatopy.initialize_app(config)

		# fetching user preference
		loc 	= str(tracker.get_slot('location')).lower()
		cuisine = str(tracker.get_slot('cuisine')).lower()
		budget 	= tracker.get_slot('budget')
		#budget='low'

		# getting lat/lon for the city which user has entered
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1['location_suggestions'][0]['latitude']
		lon=d1['location_suggestions'][0]['longitude']

		# Updating the dictionary parameter with the cuisines mentioned in the assignments.
		cuisines_dict={'american':1, 'chinese':25, 'italian':55, 'north indian':50, 'mexican':73, 'south indian':85}

		# Updated the restaurant_search function in the zomatopy.py file to sort the restaurants in descending order of its rating.
		# Added 2 more parameters to this function to accept the field on which sorting needs to be done. As per documentation
		# @ https://developers.zomato.com/documentation for /search function, we can pass cost, rating, and real_distance field in
		# sort parameter, and asc, desc in the order field.
		# The last parameter indicates that we are looking for 20 records.
		results=zomato.restaurant_search('', lat, lon, str(cuisines_dict.get(cuisine)), 'rating', 'desc', 20)

		# loading the results as JSON object
		d = json.loads(results)

		# NOTE: Sorting restaurants in descending order will be done in the restaurant_search function in the zomatopy.py file.
		# Here will categorize the response as per budget
		if d['results_found'] == 0:
			chat_response 	= 'We do not operate in this city yet'
			email_response 	= 'no results found'
			request_state  	= 'no results found'

		else:
			for restaurant in d['restaurants']:
				request_state = 'results found'

				# fetching average cost of 2 ppl and parsing it into an integer
				cost4_2ppl = int(restaurant['restaurant']['average_cost_for_two'])

				# checking the budget and cost for 2 ppl as per search result
				if (budget == '<300' and cost4_2ppl < 300):
					isValidRestaurant = True

				elif (budget == '300-700' and (cost4_2ppl > 300 and cost4_2ppl < 700)):
					isValidRestaurant = True

				elif (budget == '>700' and cost4_2ppl > 700):
					isValidRestaurant = True

				# if a restaurant is valid as per user's requirement then add it in the chat and email response variables
				if isValidRestaurant:
					isValidRestaurant = False

					if iChatResponse < 5:
						iChatResponse += 1

						chat_response = chat_response + str(iChatResponse) + '. ' + restaurant['restaurant']['name'] + ' in ' + \
							restaurant['restaurant']['location']['address'] + ' has been rated ' + \
							restaurant['restaurant']['user_rating']['aggregate_rating'] + '\n'

					if iEmailResponse < 10:
						iEmailResponse += 1

						email_response = email_response + str(iEmailResponse) + '. ' + restaurant['restaurant']['name'] + ' in ' + \
							restaurant['restaurant']['location']['address'] + ' has been rated ' + \
							restaurant['restaurant']['user_rating']['aggregate_rating'] + '\n\n'

		
		# if below condition is satisfied, it would mean that restaurant's data was found but not in the required budget
		if (request_state == 'results found' and chat_response == ''):
			chat_response = 'No restaurants found in the given budget.'

		elif request_state == 'no results found':
			chat_response = 'No restaurants found for the given cuisine and city.'
			

		dispatcher.utter_message(chat_response)
		
		return [SlotSet('email_response', email_response)]

#-------------------------------------------------------------------------------------------------------------------------------
#Action class for checking if the city belongs to Tier-1 or Tier-2 city.
class CityCheck(Action):
	def name(self):
		return 'city_check'

	def run(self, dispatcher, tracker, domain):
		cities = pd.read_csv('city-list.csv')						#reading the city-list.csv file.
		slot_city_name = str(tracker.get_slot('location')).lower()	#fetching the location entered by user and saved in location slot.

		#checking if city name exist in tier1/2 list
		#if no records found then send message to the user else nothing
		if len((cities.loc[cities['city_name'].str.lower() == slot_city_name])) == 0:
			dispatcher.utter_message('We do not operate in this city yet.')
			slot_city_name = ''		# clearing the city name as it's invalid.

		#setting the location slot with the value provided by the user or if its invalid city then with a blank value.
		return [SlotSet('location', slot_city_name)]


#-------------------------------------------------------------------------------------------------------------------------------
# Action class for checking if the format of the mail id is correct or not.
class CheckEmailFormat(Action):
	def name(self):
		return 'email_check'

	def run(self, dispatcher, tracker, domain):
		#fetching the email entered by user and saved in email slot.
		receiver_email = str(tracker.get_slot('email')).strip().lower()

		#RegEx query to check for email format. Should provide at least 2 matches.
		#TODO REFACTOR: check if this regex can be written in a better way.
		try:
			match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', receiver_email)

			if match == None:
				dispatcher.utter_message('Invalid email id. Please provide a valid email id.')
				receiver_email = ''		#clearing the email id as it's invalid.

		except:
			dispatcher.utter_message('Invalid email id. Please provide a valid email id.')
			receiver_email = ''		#clearing the email id as it's invalid.
		
		return [SlotSet('email', receiver_email)]

#-------------------------------------------------------------------------------------------------------------------------------
# Action class for sending mail.

class SendEmail(Action):
	def name(self):
		return 'send_email'

	def run(self, dispatcher, tracker, domain):
		# Configuration details. Ideally it should be read from a configuration file.
		# TODO: read the details from a configuration file.
		sender_email 	= 'iiitbchatbot2019@gmail.com'  # Email from where we want to send the mail.
		receiver_email 	= str(tracker.get_slot('email')).lower()

		#setting-up the server
		server	 		= smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()		# starting the server
		server.login(sender_email, 'iiitb@123')

		#Send the mail
		msg = MIMEMultipart()
		msg['From'] = 'iiitbchatbot2019@gmail.com'
		msg['To'] = receiver_email
		msg['Subject'] = 'Restaurant Search on IIIT-B chatbot'
		email_message = 'List of ' + tracker.get_slot('cuisine') + ' restaurants found in ' + tracker.get_slot('location') \
			+ '\n\n' + tracker.get_slot('email_response')
		msg.attach(MIMEText(email_message, 'plain'))
		server.sendmail(sender_email, receiver_email, msg.as_string())		# sending the email.

		dispatcher.utter_message('Have sent the details on your email ' + receiver_email)

		return [SlotSet('email', receiver_email)]