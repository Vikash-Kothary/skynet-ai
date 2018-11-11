from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import sqlite3

#db = sqlite3.connect('knowledge_base.db')

interpreter = RasaNLUInterpreter("models/current/nlu")
agent = Agent.load("models/dialogue", interpreter = interpreter)

text = 'Hello'
output = agent.handle_text(text)
print(text,"\n",output,"\n\n")

text = 'I need wheelchair access'
output = agent.handle_text(text)
print(text,"\n",output,"\n\n")

text = 'the next station'
output = agent.handle_text(text)
print(text,"\n",output,"\n\n")

text = 'issue resolved'
output = agent.handle_text(text)
print(text,"\n",output,"\n\n")


text = 'bye'
output = agent.handle_text(text)
print(text,"\n",output,"\n\n")


