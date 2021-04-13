from .state import State
from random import randint
import pygame

_WHITE = (255, 255, 255)

def _between(value, start, end):
	return start < value < end

class PlayState(State):
	def __init__(self, game):
		State.__init__(self, game)
		self.counter = 0
	def update(self):
		self.counter += 1
	def draw(self, screen):
		idx = 2 if _between((self.counter // 220) % 10, 4, 6) else 1
		screen.blit(self.game.sheet[f'dino-idle-{idx}'], (50, 50))
