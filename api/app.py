import sys

from flask import Flask, jsonify
from flask_cors import CORS
from api.config import config


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
	return jsonify('hello flask')


if __name__ == '__main__':
	env = sys.argv[1] if len(sys.argv) > 2 else 'dev'

	if env == 'dev':
		print('dev')
		app.config.from_object(config.DevConfig)
	elif env == 'test':
		print('test')
		app.config.from_object(config.TestConfig)
	elif env == 'prod':
		print('prod')
		app.config.from_object(config.ProdConfig)
	else:
		raise ValueError('Invalid environment name')

	app.run()
