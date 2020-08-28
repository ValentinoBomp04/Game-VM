import pygame, sys
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum


	
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
	"""formato de letra, tamaño, color de fondo y color de texto""" 
	font = pygame.freetype.SysFont("Courier", font_size, bold=True)
	surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
	return surface.convert_alpha()


class UIElement(Sprite):
	

	def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
		
		self.mouse_over = False

		default_image = create_surface_with_text(
			text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
		)

		highlighted_image = create_surface_with_text(
			text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
		)

		self.images = [default_image, highlighted_image]

		self.rects = [
			default_image.get_rect(center=center_position),
			highlighted_image.get_rect(center=center_position),
		]

		self.action = action

		super().__init__()

	@property
	def image(self):
		return self.images[1] if self.mouse_over else self.images[0]

	@property
	def rect(self):
		return self.rects[1] if self.mouse_over else self.rects[0]

	def update(self, mouse_pos, mouse_up):
		
		if self.rect.collidepoint(mouse_pos):
			self.mouse_over = True
			if mouse_up:
				return self.action
		else:
			self.mouse_over = False

	def draw(self, surface):
		
		surface.blit(self.image, self.rect)
	

def main():
	pygame.init()

	screen = pygame.display.set_mode((800, 600))
	game_state = GameState.TITLE

	while True:
		if game_state == GameState.TITLE:
			game_state = title_screen(screen)

		if game_state == GameState.NEWGAME:
			game_state = play_level(screen)
			
		if game_state == GameState.LEVELS:
			game_state = play_level(screen)
		
		if game_state == GameState.QUIT:
			pygame.quit()
			return
def title_screen(screen):
	start_btn = UIElement(
		center_position=(400, 300),
		font_size=30,
		bg_rgb=BLUE,
		text_rgb=WHITE,
		text="Start",
		action=GameState.NEWGAME,
	)
	levels_btn = UIElement(
		center_position=(400, 350),
		font_size=30,
		bg_rgb=BLUE,
		text_rgb=WHITE,
		text="Levels",
		action=GameState.LEVELS,
	)
	
	quit_btn = UIElement(
		center_position=(400, 450),
		font_size=30,
		bg_rgb=BLUE,
		text_rgb=WHITE,
		text="Quit",
		action=GameState.QUIT,
	)
	buttons = [start_btn, levels_btn, quit_btn]
	while True:
		mouse_up = False
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				mouse_up = True
		screen.fill(BLUE)

		for button in buttons:
			ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
			if ui_action is not None:
				return ui_action
			button.draw(screen)

		pygame.display.flip()


def play_level(screen):
	level_1_btn = UIElement(
		center_position=(400, 350),
		font_size=30,
		bg_rgb=BLUE,
		text_rgb=WHITE,
		text="Nivel (1)",
		action=GameState.LEVELS,
	)
	return_btn = UIElement(
		center_position=(140, 570),
		font_size=20,
		bg_rgb=BLUE,
		text_rgb=WHITE,
		text="Volver al menu Principal",
		action=GameState.TITLE,
	)
	buttons = [level_1_btn]
	
	while True:
		mouse_up = False
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				mouse_up = True
		screen.fill(BLUE)
		for button in buttons:
			ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
			if ui_action is not None:
				return ui_action
			button.draw(screen)
			
		ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
		if ui_action is not None:
			return ui_action
		return_btn.draw(screen)

		pygame.display.flip()
class GameState(Enum):
		QUIT = -1
		TITLE = 0
		NEWGAME = 1
		LEVELS = 1

if __name__ == "__main__":
		main()
