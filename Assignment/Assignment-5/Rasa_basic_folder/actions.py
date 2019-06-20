from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json

#Action class is the parent class. Inheritance.
class ActionSearchRestaurants(Action):	#This name is given in domain file.
	def name(self):
		return 'action_restaurant'	#This is the name which is given in the stories file.
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f8e764632db822d8f7cac3254c5f8af3"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}

		# The last parameter indicates that we are looking for top 10 results.
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
		d = json.loads(results)

		iChatResponse=0 #Variable used for counting 5 restaurants. To show in the chat. For email all 10 responses will be sent.

		chat_response=""	#variable used for showing chat response
		email_response=""	#variable used for showing email response

		# TODO 1: Add code for sorting restaurant output as per rating (descending)
		if d['results_found'] == 0:
			chat_response= "We do not operate in this city yet."
			email_response="no results found"
		else:
			for restaurant in d['restaurants']:
				if iChatResponse <5:
					chat_response=chat_response + "Found " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
					iChatResponse = iChatResponse+1
				
				email_response=email_response + "Found " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"
				
		
		dispatcher.utter_message("-----"+chat_response)

		#TODO 2: Remove this code before submission
		# code to write result in a file on local drive
		#f= open("result-restaurant-search.json","w+")
		#f.write(results)
		#f.close
		#-----------------------------------------------
		
		return [SlotSet('location',loc)]

# TODO 3: Add action for checking if the city belongs to Tier-1 or Tier-2 city.
# TODO 4: Add action for checking if the mail id provided is correct or not.
# TODO 5: Add action for sending mail.

