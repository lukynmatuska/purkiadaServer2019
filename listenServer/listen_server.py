import socket
import threading
import logging

while True:
	try:
		threading.current_thread().name = "Listen server"
		logging.info("Starting ...")
		print("Starting ...")
		soc = socket.socket()
		soc.bind(("0.0.0.0",9601))
		soc.listen(1)
		logging.info("Started ... Waiting for connections")
		print("Started ... Waiting for connections")
		def handler(c, a):
			c.send(" This is password for admin (in binary): 01101110 01100101 01101111 01110000 01101001 01110011 01110101 01101010 01110101 00110010 00110000 00110001 00111000".encode())
			logging.info("c:a -> {}:{}".format(c, a))
			print("c -> {}".format(c))
			print("a -> {}".format(a))
			c.close()
		while True:
			c, a = soc.accept()
			cThread = threading.Thread(name="Server", target = handler, args = (c, a))
			cThread.daemon = True
			cThread.start()

	except Exception as problem:
		logging.info(problem)
		print("PROBLEM: {}".format(problem))
		input(".: END :.")
