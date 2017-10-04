def timeout_handler(signum, frame):
		raise TimeoutException()
