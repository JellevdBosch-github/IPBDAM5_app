import sys

from flask import Flask, jsonify
from flask_cors import CORS
from api import config


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


if __name__ == '__main__':
	env = sys.argv[1] if len(sys.argv) > 2 else 'dev'

	if env == 'dev':
		app.config = config.DevConfig
	elif env == 'test':
		app.config = config.TestConfig
	elif env == 'prod':
		app.config = config.ProdConfig
	else:
		raise ValueError('Invalid environment name')

	app.run()
