from classes import *

player_1 = Player(0,"don't get cut",0,0)
print(player_1.speech[3])

pistol_1 = Pistol(0,0,0,5)

#bullet generation testing
##array = [0,0,0,0,0]
##for i in range (0, len(array)):
##    array[i] = pistol_1.factory(pistol_1,"bullet")
##for i in range (0,len(array)):
##    print(array[i].damage)

print(pistol_1.ammo)

player_1.player_add_item_to_inventory(pistol_1)
player_1.player_equip_item(pistol_1)
print(player_1.inventory)
player_1.player_remove_item(pistol_1)
print(player_1.inventory)
