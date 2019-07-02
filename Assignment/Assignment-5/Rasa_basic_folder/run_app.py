from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

#input_channel = SlackInput( app verification token or OAuth access token,
#							 bot verification token or Bot User OAuth Access Token,
#							 slack verification token,
#							True)

input_channel = SlackInput(	'9e035261bd0317708a961f0879a4740c', 
							'a18edb7f554548aaffff43dbc565fafd',
							'CCNjN5izM3BQIwO1ECFLlyU3',
							True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))