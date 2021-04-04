from socket_utils import TCPSocket
from threading import Thread

from game import Game

class Client(Thread):
	def __init__(self, server, target, addr=None, port=None):
		Thread.__init__(
			self, 
			group=None, 
			target=target, 
			name=f'client_{id(self)}', 
			args=(self,), 
			daemon=True
		)
		if not (addr is None and port is None):
			self.__socket, self.__addr = TCPSocket(), (addr, port)
			self.socket.connect(self.__addr)
		else:
			self.__socket, self.__addr = server.socket.accept()
	@property
	def socket(self): return self.__socket
	@property
	def addr(self): return self.__addr

def _run_client(client):
	print('Sending HELLO handshake to server')
	client.socket.send({'type': 'HELLO'})
	while client.game.should_exit:
		msg = client.socket.recv()
		if not 'type' in msg: continue
		t = msg['type']
		if t == 'END':
			print('Client received EXIT signal from server!')
			return
		else:
			client.socket.send({'type': 'IDLE'})

if __name__ == '__main__':
	import pygame

	# Variables
	WIDTH, HEIGHT = 640, 480
	
	# Connect to server
	client = Client(server=None, addr='127.0.0.1', port=8000, target=_run_client)

	# Initialize pygame (Make sure to initialize before we create the game)
	pygame.init()

	# Game keeps track of client and vice versa
	client.game = Game(WIDTH, HEIGHT)
	client.game.client = client

	# Start the socket thread
	client.start()

	# Creating screen and clock for FPS timing
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock  = pygame.time.Clock()

	# Key states for key held events
	keys = {i: False for i in range(256)}

	# Game loop at 30 FPS
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				client.game.should_exit = True
				exit(0)
			if event.type == pygame.KEYUP:
				client.game.key_up(event)
				keys[event.key] = False
			if event.type == pygame.KEYDOWN:
				client.game.key_down(event)
				keys[event.key] = True
			if event.type == pygame.MOUSEBUTTONUP:
				client.game.mouse_up(event)
			if event.type == pygame.MOUSEBUTTONDOWN:
				client.game.mouse_down(event)
	
		# Update and draw
		client.game.update()
		client.game.draw(screen)

		# Update display and simulate a tick
		pygame.display.update()
		clock.tick()
