from . import conn as connection
from utils.datetime import get_current_epoch_ms


def browse(timestamp=get_current_epoch_ms()):
	with connection.connect() as conn:
		results = conn.execute(
			f'SELECT * FROM candlestick WHERE close_timestamp < {timestamp};'
		)
	result = []
	for r in results:
		result.append(
			{
				'candlestick_id': r[0],
				'timestamp': r[1],
				'open': str(r[3]),
				'high': str(r[4]),
				'low': str(r[5]),
				'close': str(r[6]),
			}
		)
	return result


def count():
	with connection.connect() as conn:
		result = conn.execute(
			'SELECT COUNT(*) FROM candlestick'
		)
	for r in result:
		result = r[0]
	return result
