# imports
# pygame it self
import pygame
# for choosing random digits, symbols, lowercases and uppercases
import random
# getting all digits, symbols, lowercases and uppercases
import string

length = 1 # length of the password
pygame.init()

# getting everything in one ( all )
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

# The icon of the "game"
icon = pygame.image.load('password.png')
pygame.display.set_icon(icon)

# loading images and making rects
minimage = pygame.image.load('minus.jpg')
minimagerect = minimage.get_rect()

plusimage = pygame.image.load('plutteken.png')
plusimagerect = plusimage.get_rect()

# easy colors and cordinates
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
yellow = (250, 218, 94)
X = 800
Y = 800

# setting the display or the window
display_surface = pygame.display.set_mode((X, Y))

# title of the game
pygame.display.set_caption('Password generator')

# font I use
font = pygame.font.Font('freesansbold.ttf', 32)

# texts and making rects for them
text2 = font.render('Generate' , True, yellow, blue)
text2rect = text2.get_rect()

text = font.render(f"Length of the password: {length}" , True, yellow, blue)
textRect = text.get_rect()

passwordsurf = font.render('Password: Wait...', True, yellow, blue)
passwordrect = passwordsurf.get_rect()

# position for the text or image
passwordrect.center = (375, 550)
text2rect.center = (400, 500)
textRect.center = (X // 2, Y // 2.5)
plusimagerect.center = (350, 400)
minimagerect.center = (410, 400)

# game loop
while True:

	# putting everything on the screen
	display_surface.fill(black)
	display_surface.blit(minimage, minimagerect)
	display_surface.blit(text2, text2rect)
	display_surface.blit(plusimage, plusimagerect)
	display_surface.blit(text, textRect)
	display_surface.blit(passwordsurf, passwordrect)


	for event in pygame.event.get():

		# If you click
		if event.type == pygame.MOUSEBUTTONDOWN:
				# if you click on the plusimage
				if plusimagerect.collidepoint(event.pos):
					length += 1
					text = font.render(f"Length of the password: {length}", True, yellow, blue)
					if length >= 94:
						length = 94
				# if you click on the minimage
				if minimagerect.collidepoint(event.pos):
					length -= 1
					if length <= 1:
						length = 1

				# if you click on "Generate"
				if text2rect.collidepoint(event.pos):
					temp = random.sample(all, length)
					password = "".join(temp)
					display_surface.blit(passwordsurf, passwordrect)
					passwordsurf = font.render(f"password: {password}", True, yellow, blue)

		# if you click on the close button
		elif event.type == pygame.QUIT:

			pygame.quit()

			quit()
		text = font.render(f"Length of the password: {length}", True, yellow, blue)
		display_surface.blit(passwordsurf, passwordrect)

		# update screen
		pygame.display.update()
