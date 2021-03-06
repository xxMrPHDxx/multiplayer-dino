from socket import socket as Socket, AF_INET, SOCK_STREAM
from base64 import b64encode, b64decode
import json

class TCPSocket(Socket):
	def __init__(self, socket=None):
		self.__socket = Socket(AF_INET, SOCK_STREAM) if socket is None else socket
	@property
	def socket(self): return self.__socket
	def accept(self):
		socket, addr = self.socket.accept()
		return TCPSocket(socket), addr
	def bind(self, addr):
		self.socket.bind(addr)
	def connect(self, addr):
		self.socket.connect(addr)
	def listen(self):
		self.socket.listen()
	def recv(self, size=None):
		if type(size) != int:
			size = int.from_bytes(self.socket.recv(4), 'big')
		return json.loads(b64decode(self.socket.recv(size)).decode('utf-8'))
	def send(self, obj):
		if type(obj) == str:
			obj = {'type': 'MESSAGE', 'message': obj}
		if type(obj) != dict:
			raise Exception('TCPSocket::send(...) expects a str or dict at argument 1!')
		content = b64encode(json.dumps(obj).encode('utf-8'))
		size    = len(content).to_bytes(4, 'big')
		self.socket.send(size + content)
