from gamestate import StateManager, MenuState, PlayState
from sprite import SpriteSheet

class Game():
	def __init__(self, width, height):
		self.__width, self.__height = width, height
		self.__sm = StateManager(self)
		self.should_exit = False

		# Assets
		self.__sheet = SpriteSheet.load('assets/sheet.json')

		# Start at menu screen
		# self.state.set(MenuState)
		# TODO: Remove later
		self.state.set(PlayState)
	@property
	def width(self): return self.__width
	@property
	def height(self): return self.__height
	@property
	def state(self): return self.__sm
	@property
	def sheet(self): return self.__sheet
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
