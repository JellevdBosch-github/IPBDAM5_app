from . import conn as connection
from utils.datetime import get_current_epoch_ms


def browse():
	with connection.connect() as conn:
		results = conn.execute(
			f'SELECT * FROM trade'
		)
	result = []
	for r in results:
		result.append(
			{
				'trade_id': r[0],
				'original_id': r[1],
				'original': r[2],
				'pattern': r[3],
				'usd_value': str(r[4]),
				'doge_value': r[5],
				'timestamp': r[6],
				'taker_side': r[7],
				'wallet_usd_value': str(r[8]),
			}
		)
	return result


def get(trade_id):
	with connection.connect() as conn:
		results = conn.execute(
			f"SELECT * FROM trade WHERE trade_id = {trade_id} OR original_id = {trade_id}"
		)
	result = []
	for r in results:
		result.append(
			{
				'trade_id': r[0],
				'original_id': r[1],
				'original': r[2],
				'pattern': r[3],
				'usd_value': str(r[4]),
				'doge_value': r[5],
				'timestamp': r[6],
				'taker_side': r[7],
				'wallet_usd_value': str(r[8]),
			}
		)
	return result


def count():
	with connection.connect() as conn:
		result = conn.execute(
			'SELECT COUNT(*) FROM trade'
		)
	for r in result:
		result = r[0]
	return result
