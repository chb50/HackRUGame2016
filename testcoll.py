import pygame, sys
import math #need this for distance calculation - Jon Cheng
from pygame.locals import *

pygame.init()

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, offset_x, offset_y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load('images/player.jpg')

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = offset_x
       self.rect.y = offset_y


    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        #pidgey collision
        if self.rect.colliderect(pidgey):
            if dx > 0: # Moving right; Hit the left side of the wall
                self.rect.right = pidgey.rect.left
            if dx < 0: # Moving left; Hit the right side of the wall
                self.rect.left = pidgey.rect.right
            if dy > 0: # Moving down; Hit the top side of the wall
                self.rect.bottom = pidgey.rect.top
            if dy < 0: # Moving up; Hit the bottom side of the wall
                self.rect.top = pidgey.rect.bottom

class Object(pygame.sprite.Sprite):
   def __init__(self, offset_x, offset_y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load('images/object.jpg')

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = offset_x
       self.rect.y = offset_y

# instantiate objects
person = Block(100,100)
pidgey = Object(200,200)

# set the FPS 
FPS = 40
# used to ensure a maximum fps setting
fpsClock = pygame.time.Clock()

# set up the window amd caption
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Interaction')

WHITE = (255, 255, 255) # define white

#set booleans to false
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
ePressed = False

#main game loop
while True:
  DISPLAYSURF.fill(WHITE)

  # movements
  if moveUp == True:
    person.move(0, -5)
  elif moveDown == True:
    person.move(0, 5)
  elif moveLeft == True:
    person.move(-5, 0)
  elif moveRight == True:
    person.move(5, 0)

  for event in pygame.event.get():
    #check for a key press
    if event.type == KEYDOWN:
      if event.key == K_UP:
        moveUp = True
      elif event.key == K_LEFT:
        moveLeft = True
      elif event.key == K_RIGHT:
        moveRight = True
      elif event.key == K_DOWN:
        moveDown = True
      elif event.key == K_e:
        ePressed = True
    # check for key release
    elif event.type == KEYUP:
      if event.key == K_UP:
        moveUp = False
      elif event.key == K_LEFT:
        moveLeft = False
      elif event.key == K_RIGHT:
        moveRight = False
      elif event.key == K_DOWN:
        moveDown = False
      elif event.key == K_e:
        ePressed = False
    #check if the player quit
    elif event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Jon Cheng is trying to fix this by inserting the following line:
    dist = math.hypot(person.rect.x - pidgey.rect.x, person.rect.y - pidgey.rect.y)
    print dist
  # needs to be fixed 
  #if person.rect.colliderect(pidgey) and ePressed == True: #Vineet's
    if dist < 40 and ePressed == True: # Jon's
      raise SystemExit, "You win!"

  #used for updates  
  DISPLAYSURF.blit(pidgey.image, (pidgey.rect.x, pidgey.rect.y))
  DISPLAYSURF.blit(person.image, (person.rect.x, person.rect.y))
  pygame.display.update()
  fpsClock.tick(FPS)
