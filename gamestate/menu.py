from .state import State

class MenuState(State):
	def __init__(self, game):
		State.__init__(self, game)
	def draw(self, screen):
		print('Drawing...')
