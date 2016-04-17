from classes import *

player_1 = Player(0,"don't get cut",0,0)
print(player_1.speech[3])

pistol_1 = Pistol(0,0,0,5)
array = [0,0,0,0,0]
for i in range (0, len(array)):
    array[i] = pistol_1.factory(pistol_1,"bullet")
    pistol_1.damage += 1
for i in range (0,len(array)):
    print(array[i].damage)

print(pistol_1.ammo)
