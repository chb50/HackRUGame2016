from __future__ import generators
import pygame
import abc #module for using abstract base classes

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

#general items
class computer(Item):
    def __init__(self,image,offset_x,offset_y, message):
        Item.__init__(self,image,offset_x,offset_y)
        self.message = message #message that the computer tells the player
        self.name = "computer"

class Bullet(Item):
    def __init__(self, image, offset_x, offset_y, weapon_dmg):
        Item.__init__(self, image, offset_x, offset_y)
        self.damage = weapon_dmg

#equipable items
class Equipable(Item):
    def __init__(self,image,offset_x,offset_y):
        Item.__init__(self,image,offset_x,offset_y)
        self.damage = None
        self.ammo = None
        self.weight = None
        
class Knife(Equipable):
    def __init__(self,image,offset_x,offset_y):
        Equipable.__init__(self,image,offset_x,offset_y)
        #these values should not change throughout execution of the game
        self.damage = 10
        self.size = (1,2)
        self.name = "knife"
        self.weight = 5

class Pistol(Equipable): #gain ammo by finding more pistols
    def __init__(self ,image, offset_x, offset_y, ammo):
        Equipable.__init__(self, image, offset_x, offset_y)
        #static
        self.damage = 20
        self.size = (1,2)
        self.name = "pistol"
        self.weight = 10
        #variable
        self.ammo = 5
        
    #needs to generate bullets
    def factory(self, type): #the "self" parameter for the factory is explicit, and there for an arguement must be passed in it (the object that contains this function)
        if type == "bullet":
            self.ammo -= 1
            print("test: " + str(self.damage))
            return Bullet(0,0,0,self.damage)
    factory = staticmethod(factory)

#consumable items
class Consumable(Item):
    def __init__(self,image,offset_x,offset_y):
        Item.__init__(self,image,offset_x,offset_y)
        self.healing = None #gain health from this item
        self.rejuvinate = None #gain stamina from this item
        #these two variables track the top left box of the item in inventory
        self.invent_x = None
        self.invent_y = None

class Player(object):
    #sprite will be the image loaded to the character from photoshop
    def __init__(self,sprite, objective, x, y, color, size):
        self.objective = objective # a string explaining to the user what their objective is
        self.invent_weight = 20 #carry capacity (weight) that the player has left
        self.inventory = []
        self.speech = ["don't attack!", "don't mind me.", "I'm here to help.", "stay away!", "your days are numbered.", "time to die!"]
        self.sprite = sprite
        self.dead = False
        self.equip = "hands" #the player's current equiped weapon
        #player stats
        self.health = 100
        self.attack = 5 #the amount of damage that the player deals with their current weapon
        self.stamina = 100
        
        #Front end junk
        self.sprite.image = pygame.Surface([size, size])
        self.sprite.image.fill(color)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.topleft = (x,y)
        
    #NOTE: if you need to refer to the member variables defined with "self" in a method, you need to pass "self" as a parameter to said method
        
    #def player_move(self, move_x, move_y): #NOT TESTED
        #solve for player movement based on keyboard input. render the player at a location on the map pased on the players coordinate parameters
        #self.offset_x = self.offset_x + move_x
        #self.offset_y = self.offset_y + move_y
        
    def player_damage(self, item): #NOT TESTED
        if isinstance(item, Equipable) != True:
            print("Cannot calculate damage of this item!")
            return   
        self.health = self.health - item.damage
        if self.health < 0:
            self.dead = True

    #can generate item names on front end based on the objects "name" parameter pushed in the back end
    def player_add_item_to_inventory(self, item):
        if self.invent_weight > item.weight:
            self.invent_weight - item.weight
            self.inventory.append(item) #can access items by their "name" parameter
        else:
            #will need to be displayed to the player
            print("Cannot pick up item!")
            
    def player_equip_item(self, item): #this function should only pass in items intended to be equipable
        #for collision detection, we will use pygame sprites
        #item_name is the "name" member variable of the item classes above
        if isinstance(item, Equipable) != True:
            print("Cannot equip this item!")
            return         
        self.equip = item.name
        self.attack = item.damage
        
    def player_remove_item(self, item): #allow player to drop items
        self.invent_weight + item.weight
        if self.invent_weight > 20:
            self.invent_weight = 20
        for i in self.inventory:
            if i == item:
                self.inventory.remove(i)
                return
            
    def player_consume_item(self, item): #this function should only pass in items that are intended to be consumable
        if isinstance(item, Consumable) != True:
            print("Cannot use this item!")
            return
        #we need to delete the item from the inventory
        player_remove_item(item)
        self.health = self.health + item.healing
        if self.health > 100:
            self.health = 100
        self.stamina = self.stamina + item.rejuvinate
        if self.stamina > 100:
            self.stamina = 100
        
