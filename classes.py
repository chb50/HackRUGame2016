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
        super().__init__(self,image,offset_x,offset_y)
        self.message = message #message that the computer tells the player
        self.name = "computer"

#equipable items
class Equipable(Item):
    def __init__(self,image,offset_x,offset_y):
        super().__init__(self,image,offset_x,offset_y)
        self.damage = None
        
class Knife(Equipable):
    def __init__(self,image,offset_x,offset_y):
        #get every paramater of the "Item" parent class
        super().__init__(self,image,offset_x,offset_y)
        #these values should not change throughout execution of the game
        self.damage = 10
        self.size = (1,2)
        self.name = "knife"

#consumable items
class Consumable(Item):
    def __init__(self,image,offset_x,offset_y):
        super().__init__(self,image,offset_x,offset_y)
        self.healing = None #gain health from this item
        self.rejuvinate = None #gain stamina from this item
    


class Player(object):
    #sprite will be the immage loaded to the character from photoshop
    def __init__(self,sprite, objective, offset_x, offset_y):
        self.objective = objective # a string explaining to the user what their objective is
        self.inventory = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]] #4x5 matrix
        self.speech = ["don't attack!", "don't mind me.", "I'm here to help.", "stay away!", "your days are numbered.", "time to die!"]
        self.sprite = sprite
        self.offset_x = offset_x #x coordinate of player
        self.offset_y = offset_y #y coordinate of player
        self.dead = False
        self.equip = "hands" #the player's current equiped weapon
        #player stats
        self.health = 100
        self.attack = 5 #the amount of damage that the player deals with their current weapon
        self.stamina = 100
    def player_move(move_x, move_y):
        #solve for player movement based on keyboard input. render the player at a location on the map pased on the players coordinate parameters
        self.offset_x = self.offset_x + move_x
        self.offset_y = self.offset_y + move_y
    def player_damage(item):
        if isinstance(item, Equipable) != True:
            print("Cannot calculate damage of this item!")
            return   
        self.health = self.health - item.damage
        if self.health < 0:
            self.dead = True
    def player_equip_item(item): #this function should only pass in items intended to be equipable
        #for collision detection, we will use pygame sprites
        #item_name is the "name" member variable of the item classes above
        if isinstance(item, Equipable) != True:
            print("Cannot equip this item!")
            return         
        self.equip = item.name
        self.attack = item.damage
    def player_remove_item(item): #allow player to drop items
        for i in range (0 , len(self.inventory)):
            for j in range (0, len(i)):
                if self.inventory[i][j] == item.name:
                    self.inventory[i][j] == ""
    def player_consume_item(item): #this function should only pass in items that are intended to be consumable
        if isinstance(item, Consumable) != True:
            print("Cannot use this item!")
            return
        #we need to delete the item from the inventory
        player_remove_item(item)
                    #will need to remove the item visually as well
        self.health = self.health + item.healing
        if self.health > 100:
            self.health = 100
        self.stamina = self.stamina + item.rejuvinate
        if self.stamina > 100:
            self.stamina = 100
        
