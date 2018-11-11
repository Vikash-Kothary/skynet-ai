from flask import Flask, request, g
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

app = Flask(__name__)

interpreter = RasaNLUInterpreter("models/current/nlu")
app.agent = Agent.load("models/dialogue", interpreter = interpreter)

@app.route('/')
def home():
    output = app.agent.handle_text(request.args.get('q').replace('%20', ' '))
    try:
        return output[0]['text']
    except Exception as e: 
        print(output, e)
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