from flask import Flask, request
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

app = Flask(__name__)

@app.route('/')
def home():
    interpreter = RasaNLUInterpreter("models/current/nlu")
    agent = Agent.load("models/dialogue", interpreter = interpreter)
    output = agent.handle_text(request.args.get('q'))
    try:
        return output[0]['text']
    except:
        return 'Sorry'

def main():
    HOST = '0.0.0.0'
    PORT = 5005
    DEBUG = False
    app.config['SERVER_NAME'] = None
    app.run(host=HOST, port=PORT, debug=DEBUG)
    #socketio.run(app, debug=True)

if __name__ == '__main__':
    main()