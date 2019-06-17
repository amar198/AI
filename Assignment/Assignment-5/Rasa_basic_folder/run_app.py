from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

#input_channel = SlackInput('xoxp-666069458500-666550655461-660588201441-4119f26d7a320424d5c8a97348e0d558', #app verification token or OAuth access token
#							'xoxb-666069458500-669084704918-1tQkpen0WLhZ8nxODfdWgDdl', # bot verification token or Bot User OAuth Access Token
#							'edH38J69KuMDXBOYytmt10Xh', # slack verification token
#							True)

input_channel = SlackInput('xoxp-666069458500-666550655461-660588201441-4119f26d7a320424d5c8a97348e0d558',
							'xoxb-666069458500-669084704918-1tQkpen0WLhZ8nxODfdWgDdl', 
							'edH38J69KuMDXBOYytmt10Xh',
							True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))