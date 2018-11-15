# import pygame

# (width, height) = (850, 450)
# bg = pygame.image.load("background.jpeg")
# chat_panel = pygame.image.load("obstacle.png")
# chat_panel = pygame.transform.scale(chat_panel, (250, 430))
# screen = pygame.display.set_mode((width, height))
# screen.blit(bg, (0, 0))
# screen.blit(chat_panel, (10, 10))
# pygame.display.flip()
# while True:
# 	pass

import pygame as pg


def main():
	bg = pg.image.load("background.jpeg")
	chat_panel = pg.image.load("obstacle.png")
	chat_panel = pg.transform.scale(chat_panel, (250, 430))
	screen = pg.display.set_mode((850, 450))
	font = pg.font.Font(None, 32)
	clock = pg.time.Clock()
	input_box = pg.Rect(20, 380, 80, 50)
	color_inactive = pg.Color('lightskyblue3')
	color_active = pg.Color('dodgerblue2')
	color = color_inactive
	active = False
	text = ''
	done = False

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True

			if event.type == pg.MOUSEBUTTONDOWN:
				if input_box.collidepoint(event.pos):
					active = not active
				else:
					active = False
					color = color_active if active else color_inactive
			if event.type == pg.KEYDOWN:
				if active:
					if event.key == pg.K_RETURN:
						print(text)
						text = ''
					elif event.key == pg.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode

		screen.fill((30, 30, 30))
		txt_surface = font.render(text, True, color)
		width = max(200, txt_surface.get_width()+10)
		input_box.w = width
		screen.blit(bg, (0, 0))
		screen.blit(chat_panel, (10, 10))
		screen.blit(txt_surface, (20, 380))
		pg.draw.rect(screen, color, input_box, 2)
		pg.display.flip()
		clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()