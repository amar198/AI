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

input_channel = SlackInput(	'xoxp-666069458500-666550655461-661180227443-a16ed89ac2c4596b7ed5dcea3301c496', 
							'xoxb-666069458500-669084704918-RP7oE2aUg9aSII3mPIi6dgpX',
							'edH38J69KuMDXBOYytmt10Xh',
							True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))