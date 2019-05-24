import hashlib
def start(value):
	m = hashlib.sha256()
	m.update(value.encode('utf-8'))
	return m.hexdigest()

start()