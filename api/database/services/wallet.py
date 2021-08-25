from . import conn as connection
from utils.datetime import get_current_epoch_ms


def get(wallet_id=1):
	with connection.connect() as conn:
		results = conn.execute(
			f'SELECT * FROM wallet WHERE wallet_id = {wallet_id};'
		)
	result = []
	for r in results:
		result.append(
			{
				'wallet_id': r[0],
				'eur_value': r[1],
				'usd_value': r[2],
				'doge_value': r[3],
			}
		)
	return result
