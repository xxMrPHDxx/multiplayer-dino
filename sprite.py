import pygame
import json

class SpriteSheet():
	def __init__(self, image):
		self.__image = image
		self.__sprites = {}
	@property
	def image(self): return self.__image
	def __getitem__(self, key):
		assert type(key) == str, 'Key must be a type of str!'
		return self.__sprites[key] if key in self.__sprites else None
	def __setitem__(self, key, region):
		assert type(region) == tuple, 'Expects a region tuple!'
		assert len(region) in [3, 4, 6], \
			'Invalid tuple length (Only 3, 4, 6)!'
		sx, sy, sw, sh, dw, dh = {
			3: (*region, *[region[2] for _ in range(3)]),
			4: (*region, *region[2:]),
			6: region
		}[len(region)]
		surface = pygame.Surface((sw, sh), pygame.SRCALPHA)
		surface.blit(self.__image, (0, 0), (sx, sy, sw, sh))
		self.__sprites[key] = pygame.transform.scale(surface, (dw, dh))
	@staticmethod
	def load(path):
		with open(path, 'r', encoding='utf-8') as f:
			try: obj = json.loads(f.read())
			except: 
				raise RuntimeError('Failed to load sprite config "{path}"!')
		assert 'image' in obj, '"image" key cannot be found!'
		sheet = SpriteSheet(pygame.image.load(obj['image']))
		assert 'sprites' in obj, '"sprites" key cannot be found!'
		sprites = obj['sprites']
		assert type(sprites) == list, '"sprites" is not a list!'
		for i, sprite in enumerate(sprites):
			assert 'name' in sprite, \
				'"name" key cannot be found in sprite definition!'
			assert 'region' in sprite and type(sprite['region']) == list, \
				'"region" key cannot be found in sprite definition or is not a list!'
			sheet[sprite['name']] = tuple(sprite['region'])
		return sheet
