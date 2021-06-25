from . import conn as connection


def browse():
	with connection.connect() as conn:
		results = conn.execute(
			'SELECT * FROM pattern'
		)
	result = []
	for r in results:
		result.append({'pattern': r[0], 'occurences': r[1], 'profit': str(r[2])})
	return result


def count():
	with connection.connect() as conn:
		result = conn.execute(
			'SELECT COUNT(*) FROM pattern'
		)
	for r in result:
		result = r[0]
	return result
