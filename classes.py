import pygame
import abc #module for using abstract base classes

##class Map(object):
##    def __init__(self):
##

#code for hit ditection, may be useful later
##if (self.offset_x < player.hitbox_x and self.offset_x > player.offset_x and self.offset_y < player.hitbox_y and self.offset_y > player.offset_y
##    or self.offset_x < player.hitbox_x and self.offset_x > player.offset_x and self.hitbox_y < player.hitbox_y and self.hitbox_y > player.offset_y
##    or self.hitbox_x < player.hitbox_x and self.hitbox_x > player.offset_x and self.offset_y < player.hitbox_y and self.offset_y > player.offset_y
##    or self.hitbox_x < player.hitbox_x and self.hitbox_x > player.offset_x and self.hitbox_y < player.hitbox_y and self.hitbox_y > player.offset_y):

class Item(object): #implemented as a pure virtual, in that every item must have at least these parameters
    def __init__(self,image,offset_x,offset_y):
        self.image = image #SUBJECT TO CHANGE
        self.offset_x = offset_x #spawn location
        self.offset_y = offset_y
        self.size = None #size shall be implemented as a tuple, the first value is the "x" size, and the second is the "y" size
        self.name = None #every class should have a name
        

class Knife(Item):
    def __init__(self,image,offset_x,offset_y, hitbox_x, hitbox_y):
        #get every paramater of the "Item" parent class
        super().__init__(self,image,offset_x,offset_y)
        #these values should not change throughout execution of the game
        self.damage = 10
        self.size = (1,2)
        self.name = "knife"
    


class Player(object):
    #sprite will be the immage loaded to the character from photoshop
    def __init__(self,inventory,armed,sprite, offset_x, offset_y, hitbox_x, hitbox_y):
        self.inventory = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]] #4x5 matrix
        self.health = 0
        self.armed = armed #the player's current wealded weapon
        self.sprite = sprite
        self.offset_x = offset_x #x coordinate of player
        self.offset_y = offset_y #y coordinate of player
        #NOTE: hitbox is a value greater than offset. this difference maps the hitbox of the player sprite
        self.hitbox_x = hitbox_x 
        self.hitbox_y = hitbox_y
        self.dead = False
        self.equip = None
    def player_move(move_x, move_y):
        #solve for player movement based on keyboard input. render the player at a location on the map pased on the players coordinate parameters
        self.offset_x = self.offset_x + move_x
        self.offset_y = self.offset_y + move_y
    def player_damage(item_damage)
        self.health = self.health - item_damage
        if self.health < 0:
            self.dead = True
    def player_use_item(item):
        #change the player's hitbox based on the item used
        
            
            
        
        
        
