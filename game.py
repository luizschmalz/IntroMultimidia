import pygame
from pygame.locals import *
import random
from audio import get_microphone_frequency
from time import sleep
 
pygame.init()
 
clock = pygame.time.Clock()
fps = 60
 
screen_width = 864
screen_height = 800
 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
 
font = pygame.font.SysFont('Bauhaus 93', 60)
 
white = (255, 255, 255)
 
ground_scroll = 0
scroll_speed = 8
game_over = False
pipe_gap = 120
pipe_frequency = 500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
 
 
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')
button_img = pygame.image.load('img/restart.png')
 
 
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))
 
def reset_game():
	if music_playing:
		pygame.mixer.music.unpause()
	pipe_group.empty()
	flappy.rect.x = 100
	flappy.rect.y = int(screen_height / 2)
	score = 0
	return score
 
 
class Bird(pygame.sprite.Sprite):
 
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range (1, 4):
			img = pygame.image.load(f"img/gota.{num}.png")
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False
 
	def update(self):
 
 
		if game_over == False:
			def move(self):
				var = get_microphone_frequency()
				var = var * 1000
				print(var)
				if var < 13 and var > 2:
					self.rect[1] += 15
				elif var > 13:
					self.rect[1] -= 15
					if self.rect[1] < 0:
						self.rect[1] = 0
				sleep(0.03)
			move(self)
			flap_cooldown = 5
			self.counter += 1
			
			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
				self.image = self.images[self.index]
 
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			self.image = pygame.transform.rotate(self.images[self.index], -90)
 
 
 
class Pipe(pygame.sprite.Sprite):
 
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/pipe.png")
		self.rect = self.image.get_rect()
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		elif position == -1:
			self.rect.topleft = [x, y + int(pipe_gap / 2)]
 
 
	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()
 
 
 
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
 
	def draw(self):
		action = False
 
		pos = pygame.mouse.get_pos()
 
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True
 
		screen.blit(self.image, (self.rect.x, self.rect.y))
 
		return action
 
 
 
pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()
 
flappy = Bird(100, int(screen_height / 2))
 
bird_group.add(flappy)
 
button = Button((screen_width // 2) -65, screen_height // 2, button_img)
 
logo_menu = pygame.image.load('img/logo.png')
logo_menu = pygame.transform.scale(logo_menu, (400, 200))
menu_bg = pygame.image.load('img/menu.png')
menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))
play_button = pygame.image.load('img/start.png')
play_button = pygame.transform.scale(play_button, (200, 100))
quit_button = pygame.image.load('img/quit.png')
quit_button = pygame.transform.scale(quit_button, (200, 100))
mute_button = pygame.image.load('img/mute_button.png')
mute_button = pygame.transform.scale(mute_button, (50, 50))
unmute_button = pygame.image.load('img/unmute_button.png')
unmute_button = pygame.transform.scale(unmute_button, (50, 50))
 
def main_menu():
	global music_playing
	pygame.mixer.init()
	pygame.mixer.music.load('img/musica.mp3')
	pygame.mixer.music.set_volume(0.3)
	pygame.mixer.music.play(-1)
	music_playing = True
	current_button = mute_button
	click = False
	while True:
		screen.fill((0, 0, 0))
		screen.blit(menu_bg, (0, 0))
		screen.blit(logo_menu, (screen_width // 2 - 200, 140))
		screen.blit(play_button, (screen_width // 2 - 100, screen_height // 2))
		screen.blit(quit_button, (screen_width // 2 - 100, screen_height // 2 + 150))
		screen.blit(current_button, (screen_width // 2 + 370, screen_height // 2 - 390))
		mx, my = pygame.mouse.get_pos()
 
		button_1 = Rect(screen_width // 2 - 100, screen_height // 2, 200, 100)
		button_2 = Rect(screen_width // 2 - 100, screen_height // 2 + 150, 200, 100)
		button_3 = Rect(screen_width // 2 + 370, screen_height // 2 - 390, 50, 50)
 
		if button_1.collidepoint((mx, my)):
			if click:
				return False
		if button_2.collidepoint((mx, my)):
			if click:
				pygame.quit()
 
		if button_3.collidepoint((mx, my)):
			if click:
				if music_playing:
					pygame.mixer.music.pause()
					music_playing = False
					current_button = unmute_button
				else:
					pygame.mixer.music.unpause()
					music_playing = True
					current_button = mute_button
 
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
 
		pygame.display.update()
		clock.tick(60)
 
 
run = True
main_menu_active = True
while run:
	
	if main_menu_active:
		main_menu_active = main_menu()
 
	clock.tick(fps)
	screen.blit(bg, (0,0))
	bird_group.draw(screen)
	bird_group.update()
 
	pipe_group.draw(screen)
	pipe_group.update()
 
	screen.blit(ground_img, (ground_scroll, 768))
 
	if len(pipe_group) > 0:
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True and not game_over :
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False
	draw_text(str(score), font, (0,0,0), 417, 76)
 
 
	if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
		game_over = True
	if flappy.rect.bottom >= 768:
		game_over = True
 
 
	if game_over == False:
		time_now = pygame.time.get_ticks()
		if time_now - last_pipe > pipe_frequency*5:
			if score < 2:
				pipe_frequency = 500
			elif score >= 2:
				pipe_frequency = 400	
			elif score >= 4:
				pipe_frequency = 300
			elif score >= 6:
				pipe_frequency = 200	
			else:
				pipe_frequency = 100
 
			pipe_height = random.randint(-100, 100)
			btm_pipe = Pipe(screen_width, int(screen_height / 2) + int(pipe_height+30), -1)
			top_pipe = Pipe(screen_width, int(screen_height / 2) + int(pipe_height+30), 1)
			pipe_group.add(btm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now
 
		pipe_group.update()
 
		ground_scroll -= scroll_speed
		if abs(ground_scroll) > 35:
			ground_scroll = 0
	
	if game_over == True:
		if music_playing:
			pygame.mixer.music.pause()
		if button.draw():
			game_over = False
			score = reset_game()
 
 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
 
	pygame.display.update()
 
pygame.quit()
