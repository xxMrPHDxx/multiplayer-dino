from .state import State
from pygame.font import Font
import pygame

_BLACK = (0, 0, 0)
_WHITE = (255, 255, 255)
_GRAY  = (121, 121, 121)
_RED   = (255, 0, 0)

class MenuState(State):
	def __init__(self, game):
		State.__init__(self, game)

		# Fonts
		self._font1  = Font('freesansbold.ttf', 44)
		self._font2  = Font('freesansbold.ttf', 16)
		self._font3  = Font('freesansbold.ttf', 24)

		# Texts
		self._titles = [
			self._font1.render(text, True, _WHITE)
			for text in ['Multiplayer', 'Dinosaur']
		]
		self._credit = Font('freesansbold.ttf', 12).render(
			'Made by xxMrPHDxx', True, _GRAY
		)
		self._options  = ['Play', 'Join', 'Help']
		self._selected = 0
	def draw(self, screen):
		# Clear screen
		screen.fill(_BLACK)

		# Draw title
		for i, title in enumerate(self._titles):
			w = title.get_rect().width
			screen.blit(title, ((self.game.width-w)/2, 50 + i*50))

		# Draw credit
		w = self._credit.get_rect().width
		screen.blit(self._credit, ((self.game.width-w)/2, 150))

		# Draw options
		for i, option in enumerate(self._options):
			font, col = (
				(self._font3, _RED) 
				if self._selected == i 
				else (self._font2, _WHITE)
			)
			text = font.render(option, True, col)
			rect = text.get_rect()
			w, h = rect.width, rect.height
			screen.blit(
				text, 
				((self.game.width-w)/2, 280 + i*32 - h/2)
			)
	def key_down(self, event):
		if event.key == pygame.K_DOWN:
			self._selected += 1
		if event.key == pygame.K_UP:
			self._selected -= 1
		if self._selected < 0: self._selected = len(self._options)-1
		elif self._selected >= len(self._options): self._selected = 0
