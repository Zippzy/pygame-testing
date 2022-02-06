
import sys, pygame, time
import random as rand
pygame.init()

BLOCKS = 2
size = WIDTH, HEIGHT = 1000, 1000
background = 50, 50, 50 

class Block:
	def __init__(self, speed, colour):
		self.speed = speed
		self.position = (rand.randrange(100, 900), rand.randrange(100, 900))
		self.Rect = pygame.Rect((self.position), (30, 30))
		self.colour = colour

	def boundry(self):

		# if the new location is colliding with a wall

		if self.Rect.left < 0 or self.Rect.right > WIDTH:
			self.speed[0] = -self.speed[0]

		if self.Rect.top < 0 or self.Rect.bottom > HEIGHT:
			self.speed[1] = -self.speed[1]

def main():

	screen = pygame.display.set_mode(size)	
	objects = []
	counters = []

	for i in range(BLOCKS):
		tmp_colour = (rand.randrange(0, 255), rand.randrange(0, 255), rand.randrange(0, 255)) 
		tmp = Block([rand.randrange(-1, 1), rand.randrange(-1, 1)], tmp_colour)
		objects.append(tmp)

	while 1:

		time.sleep(1)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		for i in objects:
			i.Rect.move(i.speed)
			i.boundry()

		for i in objects:
			for j in objects:
				if i.Rect.colliderect(j.Rect):
					i.speed[0], j.speed[0] = speedAfterCollision(i.speed[0], j.speed[0])
					i.speed[1], j.speed[1] = speedAfterCollision(i.speed[1], j.speed[1])

		draw(screen, objects)
		update()


def draw(screen, objects):

	screen.fill(background)
	for i in objects:
		pygame.draw.rect(screen, i.colour, i.Rect)

def update():
	pygame.display.flip()


def speedAfterCollision(object1Speed, object2Speed):
	temp = object1Speed
	object1Speed = object2Speed - object1Speed
	object2Speed = temp - object2Speed

	return object1Speed, object2Speed

main()