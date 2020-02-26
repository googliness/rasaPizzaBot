from rasa.core.channels import SocketIOInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RegexInterpreter
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy

# load your trained agent
agent = Agent.load('models/Pizza-bot',
	action_endpoint=EndpointConfig('http://localhost:5055/webhook')
    #for action endpoint
)

input_channel = SocketIOInput(
    # event name for messages sent from the user
    user_message_evt="user_uttered",
    # event name for messages sent from the bot
    bot_message_evt="bot_uttered",
    # socket.io namespace to use for the messages
    namespace=None
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5500, serve_forever=True)