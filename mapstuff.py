import pygame, sys
from pygame.locals import *
from classes import *

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700

#COLORS         R   G   B
BLACK = list((  0,  0,  0))
WHITE = list((255,255,255))
BROWN = list(( 90, 30,  0))
GREEN = list((  0,150,  0))
BLUE  = list((  0,255,255))
RED   = list((180,  0,  0))

SCALE = 1
TILESIZE = 20
FPS = 120*SCALE
SIZE = TILESIZE*SCALE

Player_Left = False
Player_Right = False
Player_Up = False
Player_Down = False

Left = False
Right = False
Up = False
Down = False

#Wall Class: this is what a wall is made of.  Always black.
#Parameters: width, height, top corner coords
class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, topcorn):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = topcorn

#Door Class: This is what a door is made of.  Always brown.
#Parameters: Top corner coords, character that determines orientation.
class Door(pygame.sprite.Sprite):
    def __init__(self, topcorn, cha):
        pygame.sprite.Sprite.__init__(self)
        #Players pass up to down or down to up
        if cha == 'u':
            self.image = pygame.Surface([2*SIZE, SIZE])
        #else, players pass left to right or right to left
        else:
            self.image = pygame.Surface([SIZE, 2*SIZE])
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.topleft = topcorn

#Player Class: TEST CLASS ONLY.
#To utilize with full Player class, change reference to player with
#player.sprite.
#class Player(pygame.sprite.Sprite):
#    def __init__(self, topcorn):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.Surface([SIZE, SIZE])
#        self.image.fill(GREEN)
#        self.rect = self.image.get_rect()
#        self.rect.topleft = topcorn

#move_map function: Moves the map.  Iterates through two groups of
#items(later, two more: other players and items), and moves them depending
#on what is pressed.
def move_map():
    for spr in wallgroup:
        if Up == True:
            spr.rect.y += 1
        if Down == True:
            spr.rect.y -= 1
        if Left == True:
            spr.rect.x += 1
        if Right == True:
            spr.rect.x -= 1
    for spr in doorgroup:
        if Up == True:
            spr.rect.y += 1
        if Down == True:
            spr.rect.y -= 1
        if Left == True:
            spr.rect.x += 1
        if Right == True:
            spr.rect.x -= 1
    for spr in enemygroup:
        if Up == True:
            spr.rect.y += 1
        if Down == True:
            spr.rect.y -= 1
        if Left == True:
            spr.rect.x += 1
        if Right == True:
            spr.rect.x -= 1
    if Up == True:
        floor.y += 1
    if Down == True:
        floor.y -= 1
    if Left == True:
        floor.x += 1
    if Right == True:
        floor.x -= 1

#correct_map function: corrects the map position after collision.
#Parameters: change in x, change in y.
def correct_map(dx, dy):
    for spr in wallgroup:
        spr.rect.x += dx
        spr.rect.y += dy
    for spr in doorgroup:
        spr.rect.x += dx
        spr.rect.y += dy
    for spr in enemygroup:
        spr.rect.x += dx
        spr.rect.y += dy
    floor.x += dx
    floor.y += dy

pygame.init()

fpsClock = pygame.time.Clock()

pygame.display.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Uncle Jerry\'s Funhouse')

#Instantiate the three Groups: walls, doors, and player.
wallgroup = pygame.sprite.Group()
doorgroup = pygame.sprite.Group()
playgroup = pygame.sprite.Group()

#MAP
#Alright, here's the thing.  Each variable name is formatted as such:
    #> first two characters - r(Room)#(Number)
    #> third character ------ l(Left) || r(Right) || t(Top) || b(Bottom)
    #> next four characters - type of barrier (wall || door)
    #> OPTIONAL: If there is a door on that side of the room, include a _%c,
    #where %c follows the same convention as the third character (l||r||t||b)

floor = Rect(0, 0, WINDOWWIDTH*SCALE, WINDOWHEIGHT*SCALE)

#Border
topwall = Wall(50*SIZE, SIZE, (0,0))
botwall = Wall(50*SIZE, SIZE, (0,35*SIZE-SIZE))
lefwall = Wall(SIZE, 35*SIZE, (0,0))
rigwall = Wall(SIZE, 35*SIZE, (50*SIZE-SIZE,0))

#Room 1
r1bwall = Wall(16*SIZE, SIZE, (0, 6*SIZE))
r1rwall_t = Wall(SIZE, 2*SIZE, (15*SIZE, 0))
r1rdoor = Door((15*SIZE, 2*SIZE), 'l')
r1rwall_b = Wall(SIZE, 3*SIZE, (15*SIZE, 4*SIZE))

#Room 2
r2bwall_l = Wall(3*SIZE, SIZE, (0, 12*SIZE))
r2bdoor = Door((3*SIZE, 12*SIZE), 'u')
r2bwall_r = Wall(10*SIZE, SIZE, (5*SIZE,12*SIZE))
r2rwall = Wall(SIZE, 6*SIZE, (15*SIZE, 7*SIZE))

#Room 3
r3bwall_l = Wall(6*SIZE, SIZE, (0, 22*SIZE))
r3bdoor = Door((6*SIZE, 22*SIZE), 'u')
r3bwall_r = Wall(3*SIZE, SIZE, (8*SIZE, 22*SIZE))
r3rwall_t = Wall(SIZE, 6*SIZE, (10*SIZE, 12*SIZE))
r3rdoor = Door((10*SIZE, 18*SIZE), 'l')
r3rwall_b = Wall(SIZE, 5*SIZE, (10*SIZE, 20*SIZE))

#Room 4
r4rwall_t = Wall(SIZE, 5*SIZE, (10*SIZE, 23*SIZE))
r4rdoor = Door((10*SIZE, 28*SIZE), 'l')
r4rwall_b = Wall(SIZE, 4*SIZE, (10*SIZE, 30*SIZE))

#Room 5
r5bwall_l = Wall(3*SIZE, SIZE, (16*SIZE, 12*SIZE))
r5bdoor = Door((19*SIZE, 12*SIZE), 'u')
r5bwall_r = Wall(2*SIZE, SIZE, (21*SIZE,12*SIZE))
r5rwall_t = Wall(SIZE, 5*SIZE, (23*SIZE, SIZE))
r5rdoor = Door((23*SIZE, 6*SIZE), 'l')
r5rwall_b = Wall(SIZE, 5*SIZE, (23*SIZE, 8*SIZE))

#Room 6
r6rwall_t = Wall(SIZE, 9*SIZE, (23*SIZE, 13*SIZE))
r6rdoor = Door((23*SIZE, 22*SIZE), 'l')
r6rwall_b = Wall(SIZE, 10*SIZE, (23*SIZE, 24*SIZE))

#Room 7
r7bwall_l = Wall(2*SIZE, SIZE, (23*SIZE, 9*SIZE))
r7bdoor_l = Door((25*SIZE, 9*SIZE), 'u')
r7bwall_c = Wall(15*SIZE, SIZE, (27*SIZE, 9*SIZE))
r7bdoor_r = Door((42*SIZE, 9*SIZE), 'u')
r7bwall_r = Wall(5*SIZE, SIZE, (44*SIZE, 9*SIZE))

#Room 8
r8bwall_l = Wall(6*SIZE, SIZE, (23*SIZE, 17*SIZE))
r8bdoor = Door((29*SIZE, 17*SIZE), 'u')
r8bwall_r = Wall(6*SIZE, SIZE, (31*SIZE, 17*SIZE))
r8rwall = Wall(SIZE, 8*SIZE, (36*SIZE, 9*SIZE))

#Room 9
r9bwall_l = Wall(9*SIZE, SIZE, (23*SIZE, 28*SIZE))
r9bdoor = Door((32*SIZE, 28*SIZE), 'u')
r9bwall_r = Wall(8*SIZE, SIZE, (34*SIZE, 28*SIZE))
r9rwall = Wall(SIZE, 12*SIZE, (42*SIZE, 17*SIZE))

#Room 10
r10rwall_t = Wall(SIZE, 3*SIZE, (42*SIZE, 28*SIZE))
r10rdoor = Door((42*SIZE, 31*SIZE), 'l')
r10rwall_b = Wall(SIZE, 2*SIZE, (42*SIZE, 33*SIZE))

#Room 11
r11bwall_l = Wall(3*SIZE, SIZE, (36*SIZE, 17*SIZE))
r11bdoor_l = Door((39*SIZE, 17*SIZE), 'u')
r11bwall_c = Wall(4*SIZE, SIZE, (41*SIZE, 17*SIZE))
r11bdoor_r = Door((45*SIZE, 17*SIZE), 'u')
r11bwall_r = Wall(2*SIZE, SIZE, (47*SIZE, 17*SIZE))

#add_map function: Adds all of the walls and doors to respective groups.
#We probably don't need it, honestly, but we need to do the things inside.
def add_map():
    #Building Walls
    topwall.add(wallgroup)
    botwall.add(wallgroup)
    lefwall.add(wallgroup)
    rigwall.add(wallgroup)
    
    #Room 1
    r1bwall.add(wallgroup)
    r1rwall_t.add(wallgroup)
    r1rdoor.add(doorgroup)
    r1rwall_b.add(wallgroup)

    #Room 2
    r2bwall_l.add(wallgroup)
    r2bdoor.add(doorgroup)
    r2bwall_r.add(wallgroup)
    r2rwall.add(wallgroup)

    #Room 3
    r3bwall_l.add(wallgroup)
    r3bdoor.add(doorgroup)
    r3bwall_r.add(wallgroup)
    r3rwall_t.add(wallgroup)
    r3rdoor.add(doorgroup)
    r3rwall_b.add(wallgroup)

    #Room 4
    r4rwall_t.add(wallgroup)
    r4rdoor.add(doorgroup)
    r4rwall_b.add(wallgroup)

    #Room 5
    r5bwall_l.add(wallgroup)
    r5bdoor.add(doorgroup)
    r5bwall_r.add(wallgroup)
    r5rwall_t.add(wallgroup)
    r5rdoor.add(doorgroup)
    r5rwall_b.add(wallgroup)

    #Room 6
    r6rwall_t.add(wallgroup)
    r6rdoor.add(doorgroup)
    r6rwall_b.add(wallgroup)

    #Room 7
    r7bwall_l.add(wallgroup)
    r7bdoor_l.add(doorgroup)
    r7bwall_c.add(wallgroup)
    r7bdoor_r.add(doorgroup)
    r7bwall_r.add(wallgroup)

    #Room 8
    r8bwall_l.add(wallgroup)
    r8bdoor.add(doorgroup)
    r8bwall_r.add(wallgroup)
    r8rwall.add(wallgroup)

    #Room 9
    r9bwall_l.add(wallgroup)
    r9bdoor.add(doorgroup)
    r9bwall_r.add(wallgroup)
    r9rwall.add(wallgroup)

    #Room 10
    r10rwall_t.add(wallgroup)
    r10rdoor.add(doorgroup)
    r10rwall_b.add(wallgroup)

    #Room 11
    r11bwall_l.add(wallgroup)
    r11bdoor_l.add(doorgroup)
    r11bwall_c.add(wallgroup)
    r11bdoor_r.add(doorgroup)
    r11bwall_r.add(wallgroup)


player = Player(pygame.sprite.Sprite(),'Steal the Declaration of Independence', 3*SIZE, 3*SIZE, GREEN, SIZE)
player.sprite.add(playgroup)

enemygroup = pygame.sprite.Group()

player2 = Player(pygame.sprite.Sprite(),'Find Purpose in Life', 3*SIZE, 9*SIZE, RED, SIZE)
player3 = Player(pygame.sprite.Sprite(),'Kill Player GREEN', 26*SIZE, 31*SIZE, RED, SIZE)
player4 = Player(pygame.sprite.Sprite(),'Kidnap the President', 46*SIZE, 3*SIZE, RED, SIZE)
player2.sprite.add(enemygroup)
player3.sprite.add(enemygroup)
player4.sprite.add(enemygroup)

displaydoors = True

anns = pygame.Surface([0,0])
annr = pygame.Rect(0,0,0,0)

while True: # main game loop
    #draw visual stuff and add_map
    DISPLAYSURF.fill(BLACK)
    pygame.draw.rect(DISPLAYSURF, WHITE, floor, 0)
    add_map()
    wallgroup.draw(DISPLAYSURF)
    
    #DEBUG: Hide doors.  Used to make sure walls and doors don't intersect.
    if displaydoors:
        doorgroup.draw(DISPLAYSURF)
    
    enemygroup.draw(DISPLAYSURF)
    playgroup.draw(DISPLAYSURF)
    
    #Moves the player using booleans.  This ensures continuous movement.
    if Player_Up:
        player.sprite.rect.y -= 1
    if Player_Down:
        player.sprite.rect.y += 1
    if Player_Left:
        player.sprite.rect.x -= 1
    if Player_Right:
        player.sprite.rect.x += 1
    
    #if a player is colliding with a wall, stop their movement and correct it.
    if pygame.sprite.spritecollideany(player.sprite, wallgroup) is not None:
        if Player_Up == True:
            Player_Up = False
            player.sprite.rect.y += 1
        if Player_Down == True:
            Player_Down = False
            player.sprite.rect.y -= 1
        if Player_Left == True:
            Player_Left = False
            player.sprite.rect.x += 1
        if Player_Right == True:
            Player_Right = False
            player.sprite.rect.x -= 1
        xcor = 0
        ycor = 0
        if Up == True:
            Up = False
            ycor = -1
        if Down == True:
            Down = False
            ycor = 1
        if Left == True:
            Left = False
            xcor = -1
        if Right == True:
            Right = False
            xcor = 1
        correct_map(xcor, ycor)
    
    #using the same idea as moving the player, move the map.
    move_map()
    
    #Everything is fine.
    print 'Everything is fine.'
    
    #Receive keyboard input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            #Space to exit
            if event.key == K_SPACE:
                pygame.quit()
                sys.exit()
            #Q to hide doors
            elif event.key == K_q:
                displaydoors = False
            #up/down/left/right to move the player (DEBUG)
            elif event.key == K_UP:
                Player_Up = True
            elif event.key == K_DOWN:
                Player_Down = True
            elif event.key == K_LEFT:
                Player_Left = True
            elif event.key == K_RIGHT:
                Player_Right = True
            #w/a/s/d to move the map.
            elif event.key == K_w:
                Up = True
            elif event.key == K_s:
                Down = True
            elif event.key == K_a:
                Left = True
            elif event.key == K_d:
                Right = True
            elif event.key == K_i:
            	player.player_add_item_to_inventory(Pistol(0, 0, 0, 5))
            	anns = pygame.font.Font('freesansbold.ttf', 18).render(player.inventory[-1].name + ' has been added to your inventory.', True, BLUE)
            	annr = anns.get_rect()
            	annr.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
            	
            elif event.key == K_r:
                stri = player.inventory[-1].name
                player.player_remove_item(player.inventory[-1])
                anns = pygame.font.Font('freesansbold.ttf', 18).render(stri + ' has been removed from your inventory.', True, BLUE)
                annr = anns.get_rect()
                annr.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

        #KeyUp + boolean implentation is used to do things while a button is held.
        elif event.type == KEYUP:
            if event.key == K_q:
                displaydoors = True
            elif event.key == K_UP:
                Player_Up = False
            elif event.key == K_DOWN:
                Player_Down = False
            elif event.key == K_LEFT:
                Player_Left = False
            elif event.key == K_RIGHT:
                Player_Right = False
            elif event.key == K_w:
                Up = False
            elif event.key == K_s:
                Down = False
            elif event.key == K_a:
                Left = False
            elif event.key == K_d:
                Right = False
    DISPLAYSURF.blit(anns, annr)
    pygame.display.update()
    fpsClock.tick(FPS)
