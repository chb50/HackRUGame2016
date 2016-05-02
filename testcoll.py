import pygame, sys
import math #need this for Pythagorean Thm - Jon Cheng
# And...because I can't math after staying up for almost 24 hours
# for this hackathon ;D
from pygame.locals import *

pygame.init()

def load_image(name):
  image = pygame.image.load(name)
  return image

class Block(pygame.sprite.Sprite):

    # layer -- JC
    layer = 1

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, offset_x, offset_y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       self.imagesFront = []
       self.imagesFront.append(pygame.image.load('images/player_front.png'))
       self.imagesFront.append(pygame.image.load('images/player_front_move1.png'))
       self.imagesFront.append(pygame.image.load('images/player_front_move2.png'))

       self.imagesBack = []
       self.imagesBack.append(pygame.image.load('images/player_back.png'))
       self.imagesBack.append(pygame.image.load('images/player_back_move1.png'))
       self.imagesBack.append(pygame.image.load('images/player_back_move2.png'))

       self.imagesLeft = []
       self.imagesLeft.append(pygame.image.load('images/player_left.png'))
       self.imagesLeft.append(pygame.image.load('images/player_left_move.png'))

       self.imagesRight = []
       self.imagesRight.append(pygame.image.load('images/player_right.png'))
       self.imagesRight.append(pygame.image.load('images/player_right_move.png'))
       

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.rightIndex = 0
       self.leftIndex = 0
       self.frontIndex = 0
       self.backIndex = 0
       self.image = self.imagesFront[self.frontIndex]

       self.count = 0

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = offset_x
       self.rect.y = offset_y

       self.pokeballcheck = False

    #update animation function with right movement
    def rightUpdate(self, move):
      # on key press -> animate
      if move == True:
        self.count += 1
        if self.count%4 == 0:
          self.rightIndex += 1
        if self.rightIndex >= len(self.imagesRight):
          self.rightIndex = 0
        self.image = self.imagesRight[self.rightIndex]
      # on key release -> stop animation
      else:
        self.rightIndex = 0
        self.image = self.imagesRight[self.rightIndex]

    #update animation function with left movement
    def leftUpdate(self, move):
       # on key press -> animate
      if move == True:
        self.count += 1
        if self.count%4 == 0:
          self.leftIndex += 1
        if self.leftIndex >= len(self.imagesLeft):
          self.leftIndex = 0
        self.image = self.imagesLeft[self.leftIndex]
      # on key release -> stop animation
      else:
        self.leftIndex = 0
        self.image = self.imagesLeft[self.leftIndex]

    #update animation function with left movement
    def frontUpdate(self, move):
             # on key press -> animate
      if move == True:
        self.count += 1
        if self.count%4 == 0:
          self.frontIndex += 1
        if self.frontIndex >= len(self.imagesFront):
          self.frontIndex = 0
        self.image = self.imagesFront[self.frontIndex]
      # on key release -> stop animation
      else:
        self.frontIndex = 0
        self.image = self.imagesFront[self.frontIndex]

    #update animation function with left movement
    def backUpdate(self, move):
             # on key press -> animate
      if move == True:
        self.count += 1
        if self.count%4 == 0:
          self.backIndex += 1
        if self.backIndex >= len(self.imagesBack):
          self.backIndex = 0
        self.image = self.imagesBack[self.backIndex]
      # on key release -> stop animation
      else:
        self.backIndex = 0
        self.image = self.imagesBack[self.backIndex]

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

       # layer priority so that the player "steps over" the object
       # Unused # self.layer = 1

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load('images/object.jpg')

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = offset_x
       self.rect.y = offset_y

# Creating another object - Jon Cheng
class Item(pygame.sprite.Sprite):

    #layer -- Jon Cheng
    # Unused # layer = 2

   def __init__(self, offset_x, offset_y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # layer priority and passing sprite in as layer -- JC
       # Unused # sprites.add(self, layer = self.layer)


       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load('images/masterball.jpg')

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = offset_x
       self.rect.y = offset_y

#trying to print out that you obtained a pokeball on the screen
def displayMessage():
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)


# NOTE: the 7 lines below may not be used!
# Layered Updates so that the player can "step over" items - Jon Cheng
#sprites = pygame.sprite.LayeredUpdates()
#players = pygame.sprite.LayeredUpdates()
#items = pygame.sprite.LayeredUpdates() #for the walls in the future

#Block.groups = sprites, players
#Item.groups = sprites, items

# instantiate objects
person = Block(100,100)
pidgey = Object(200,200)
# Another instantiation...Jon Cheng
an_item = Item(275, 125)
#my_group = pygame.sprite.Group(person)

WHITE = (255, 255, 255) # define white
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Bruh, you grabbed a Pokeball!!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (0, 0)

# Items list
# Unused # Items = pygame.sprite.Group()

#set the counter for displaying a message
messageCounter = 0

# set the FPS 
FPS = 30
# used to ensure a maximum fps setting
fpsClock = pygame.time.Clock()

# set up the window amd caption
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Interaction')

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
    person.backUpdate(True)
    #person.image = pygame.image.load('images/player_back.png')
  elif moveDown == True:
    person.move(0, 5)
    person.frontUpdate(True)
    #person.image = pygame.image.load('images/player_front.png')
  elif moveLeft == True:
    person.move(-5, 0)
    person.leftUpdate(True)
    #person.image = pygame.image.load('images/player_left.png')
  elif moveRight == True:
    person.move(5, 0)
    person.rightUpdate(True)
    #person.image = pygame.image.load('images/player_right.png')


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
      if person.count > 10000:
        person.count = 0
      if event.key == K_UP:
        moveUp = False
        person.backUpdate(False)
      elif event.key == K_LEFT:
        moveLeft = False
        person.leftUpdate(False)
      elif event.key == K_RIGHT:
        moveRight = False
        person.rightUpdate(False)
      elif event.key == K_DOWN:
        moveDown = False
        person.frontUpdate(False)
      elif event.key == K_e:
        ePressed = False
    #check if the player quit
    elif event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Jon Cheng - Tried to fix this by inserting the following lines:
    dist_object = math.hypot(person.rect.x - pidgey.rect.x, person.rect.y - pidgey.rect.y)
    dist_item = math.hypot(person.rect.x - an_item.rect.x, person.rect.y - an_item.rect.y)
  
  # needs to be fixed -- fixed, kinda! 
  #if person.rect.colliderect(pidgey) and ePressed == True: #Vineet's

  # The distance is denoted by the difference between the top left of 
  # the player's/person's image to the top left of the image being compared
  # I'm assuming the solution is in pixels? Test with print statements! 
    if dist_item < 35 and ePressed == True: # Replaced collision check with dist_obj --Jon Cheng
      print "Bruh, you grabbed a Pokeball!"
      displayMessage()
      if person.rect.colliderect(an_item) or dist_item < 32:
      	person.pokeballcheck = True
        an_item.image.fill((255, 255, 255))
        an_item.rect.x = -5000
        an_item.rect.y = -5000

    # check collision with pidgey if player has pokeball  
    if dist_object < 35 and ePressed == True and person.pokeballcheck == True: 
      raise SystemExit, "You Caught a Pidgey!"

    # if dist_item < 32 and ePressed == True: # Jon's addendum
    #   print "Bruh, you grabbed a Pokeball!"
    #   if person.rect.colliderect(an_item) or dist_item < 32:
    #     an_item.image.fill((255, 255, 255))
    #     an_item.rect.x = -5000
    #     an_item.rect.y = -5000
        # We relocated the item very far away to the top left
        # We should figure our how to actually remove the 
        # sprite and save a copy to the inventory when we get
        # closer completing the game structure 
        # 4/17/17 - JC



  #used for updates  
  DISPLAYSURF.blit(pidgey.image, (pidgey.rect.x, pidgey.rect.y))
  #adding another displaysurf for item masterball
  DISPLAYSURF.blit(an_item.image, (an_item.rect.x, an_item.rect.y))


  # Note: by convention, the last 'blit' is the top-most thing on the game window
  # Immediate source: Google pygame sprite layer --> hyperlink beginning with [SOLVED] 
  # TODO - research actual reasoning, or accept it and call it a day, and be 
  # confuzzled the next time we encounter this. 
  # NOTE: if we generate stuff, make sure players are generated last 
  DISPLAYSURF.blit(person.image, (person.rect.x, person.rect.y)) 

  pygame.display.update()
  fpsClock.tick(FPS)
