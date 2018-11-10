from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

interpreter = RasaNLUInterpreter("models/current/nlu")
agent = Agent.load("models/dialogue", interpreter = interpreter)
output = agent.handle_text("hi")
print(output[0]['text'])