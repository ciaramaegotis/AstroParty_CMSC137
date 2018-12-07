import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
 		#player
        self.image = pygame.image.load("./images/rocket_ship.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.direction = 1
        self.walls = None

    def rotate(self):
    	print("ROTATE!")
    	self.image = pygame.transform.rotate(self.image, 270)
    	self.direction = 1 if self.direction == 4 else self.direction+1
    
    def fire(self):
    	print("FIRE!")
    	print(self.rect.x)
    	print(self.rect.y)
    	bullet = Bullet(self.rect.x, self.rect.y, self.direction)
    	all_sprite_list.add(bullet)

    def changespeed(self, direction):
        """ Change the speed of the player. """
        self.direction = direction
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        change_x = 0
        change_y = 0
        if (self.direction == 1):
        	change_x = 3
        elif (self.direction == 2):
        	change_y = 3
        elif (self.direction == 3):
        	change_x = -3
        elif (self.direction == 4):
        	change_y = -3
        
        self.rect.x += change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(ORANGE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Bullet(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, direction):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        self.image = pygame.image.load("./images/bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.walls = wall_list
 
        # Make our top-left corner the passed-in location.
        self.direction = direction
        self.rect = self.image.get_rect()
        if (direction == 2):
        	self.rect.y = y + 100
        	self.rect.x = x + 15
        elif (direction == 1):#done
        	self.rect.y = y + 22
        	self.rect.x = x + 100
        elif (direction == 3):#done
        	self.rect.y = y + 20
        	self.rect.x = x - 20
        elif (direction == 4):#done
        	self.rect.y = y - 10
        	self.rect.x = x + 20

    def update(self):
        """ Update the player position. """
        # Move left/right
        change_x = 0
        change_y = 0
        if (self.direction == 1):
        	change_x = 5
        elif (self.direction == 2):
        	change_y = 5
        elif (self.direction == 3):
        	change_x = -5
        elif (self.direction == 4):
        	change_y = -5

        if (self.rect.x > 800 or self.rect.x < 0 or self.rect.y > 600 or self.rect.y < 0):
        	self.kill()
        
        self.rect.x += change_x
        self.rect.y += change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        if (len(block_hit_list) >= 1):
        	self.kill()

 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Astro Party!')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 590, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#randomized maze
maze_number = 1#random.randint(1,4)
if (maze_number == 1):#cross maze (vertical)
	wall = Wall(400, 150, 10, 300)
	wall_list.add(wall)
	all_sprite_list.add(wall)

	wall = Wall(200, 300, 400, 10)
	wall_list.add(wall)
	all_sprite_list.add(wall)
# elif (maze_number == 2):#slanted cross maze

# elif (maze_number == 3):#spiral

# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
            	player.rotate()
            elif event.key == pygame.K_e:
            	player.fire()
 
    all_sprite_list.update()
    screen.fill(BLACK)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()