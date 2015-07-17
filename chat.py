from flask import Flask, render_template
from flask.ext.socketio import SocketIO
from flask.ext.socketio import send, emit
import logging
import os
logging.basicConfig()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('json')
def handle_my_custom_event(json):
	print('received json: ' + str(json))
	emit('response', json, broadcast=True)

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=int(port))