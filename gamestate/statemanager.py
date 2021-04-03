from .state import State

class StateManager():
	def __init__(self, game):
		self.__game = game
		self.__states = []
	@property
	def game(self): return self.__game
	@property
	def state(self): return self.__states[-1]
	def __len__(self):
		return len(self.__states)
	def push(self, cls, *args, **kwargs):
		state = cls(self.game, *args, **kwargs)
		assert isinstance(state, State), 'state is not an instance of State!'
		self.__states.append(state)
	def pop(self):
		self.__states = self.__states[:-1]
	def set(self, state):
		self.pop()
		self.push(state)
	def update(self):
		if len(self) > 0: self.state.update()
	def draw(self, screen):
		if len(self) > 0: self.state.draw(screen)
	def key_up(self, event):
		if len(self) > 0: self.state.key_up(event)
	def key_down(self, event):
		if len(self) > 0: self.state.key_down(event)
	def key_held(self, event):
		if len(self) > 0: self.state.key_held(event)
	def mouse_up(self, event):
		if len(self) > 0: self.state.mouse_up(event)
	def mouse_down(self, event):
		if len(self) > 0: self.state.mouse_down(event)
