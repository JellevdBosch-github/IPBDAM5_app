import sys
from flask import Flask, jsonify
from flask_cors import CORS
from routes.candlestick import module_candlestick
from routes.currency import module_currency
from routes.trade import module_trade
from routes.wallet import module_wallet
from routes.pattern import module_pattern
import config


app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})


app.register_blueprint(module_candlestick)
app.register_blueprint(module_currency)
app.register_blueprint(module_trade)
app.register_blueprint(module_wallet)
app.register_blueprint(module_pattern)


@app.route('/')
def index():
	return jsonify('/')


@app.route('/api')
def api():
	return jsonify('/api')


if __name__ == '__main__':
	env = sys.argv[1] if len(sys.argv) >= 2 else 'dev'

	if env == 'dev':
		print('Dev Config')
		app.config.from_object(config.DevConfig)
	elif env == 'test':
		print('Test Config')
		app.config.from_object(config.TestConfig)
	elif env == 'prod':
		print('Production Config')
		app.config.from_object(config.ProdConfig)
	else:
		raise ValueError('Invalid environment name')

	app.run()
