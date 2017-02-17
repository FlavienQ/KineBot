import os
from flask import Flask, render_template
from flask.ext.socketio import SocketIO
import json


app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')

if __name__ = '__main__':
	from werkzeug.wsgi import SharedDataMiddleware
	app = SharedDataMiddleware(app, {
        '/': os.path.join(os.path.dirname(__file__), 'public')
        })
	port = int(os.environ.get('PORT', 5000))
	print('Listening on local port...')
	app.debug = True
	app.run(host='0.0.0.0', port=port)