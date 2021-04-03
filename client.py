from socket_utils import TCPSocket
from threading import Thread

from game import Game

class Client(Thread):
	def __init__(self, server, target, addr=None, port=None):
		Thread.__init__(self, group=None, target=target, name=f'client_{id(self)}', args=(self,))
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
	while True:
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
	
	# Connect to server
	client = Client(server=None, addr='127.0.0.1', port=8000, target=_run_client)

	# Game keeps track of client and vice versa
	game = Game(640, 480)
	client.game = game
	game.client = client

	# Start the socket thread
	client.start()

	# Initialize pygame
	pygame.init()

	# Creating screen and clock for FPS timing
	screen = pygame.display.set_mode((game.width, game.height))
	clock  = pygame.time.Clock()

	# Key states for key held events
	keys = {i: False for i in range(256)}

	# Game loop at 30 FPS
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				break
			if event.type == pygame.KEYUP:
				game.key_up(event)
				keys[event.key_code] = False
			if event.type == pygame.KEYDOWN:
				game.key_down(event)
				keys[event.key_code] = True
			if event.type == pygame.MOUSEBUTTONUP:
				game.mouse_up(event)
			if event.type == pygame.MOUSEBUTTONDOWN:
				game.mouse_down(event)
	
		# Update and draw
		game.update()
		game.draw(screen)

		# Update display and simulate a tick
		pygame.display.update()
		clock.tick()
