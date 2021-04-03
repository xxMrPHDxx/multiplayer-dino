from gamestate import StateManager, MenuState

class Game():
	def __init__(self, width, height):
		self.__width, self.__height = width, height
		self.__sm = StateManager(self)

		# Start at menu screen
		self.state.set(MenuState)
	@property
	def width(self): return self.__width
	@property
	def height(self): return self.__height
	@property
	def state(self): return self.__sm
	def update(self):
		self.state.update()
	def draw(self, screen):
		self.state.draw(screen)
	def key_up(self, event):
		self.state.key_up(event)
	def key_down(self, event):
		self.state.key_down(event)
	def key_held(self, event):
		self.state.key_held(event)
	def mouse_up(self, event):
		self.state.mouse_down(event)
	def mouse_down(self, event):
		self.state.mouse_down(event)
