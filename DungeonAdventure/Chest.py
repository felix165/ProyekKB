
from audioop import add
import random as rand
from traceback import print_tb

# lowPotion = 10
# medPotion = 25
# highPotion = 70
# escScroll = "Escape Scroll"
# inventory = []


class Chest:
    def __init__(self):
        self.dropRateLowPotion = 65
        self.dropRateMedPotion = 30
        self.dropRateHiPotion = 3
        self.dropRateEscScroll = 2
        self.chest = 0 #chests amount
 
    def openChest(self,Player):
        chestRes=[]
        while(self.chest >= 1):
            num1 = rand.randint(1, 100)
            pityItem = rand.randint(0, 10) * ((Player.maxHp - Player.hp)/100)
            num1 += pityItem
            if(num1 > 0 and num1 <= 65):
                print("You Found Low Potion")
                chestRes.append(0)
            elif(num1>65 and num1<=95):
                chestRes.append(1)
                print("You Found Medium Potion")
            elif(num1>95 and num1<=98):
                chestRes.append(2)
                print("You Found High Potion")
            else:
                chestRes.append(3)
                print("You Found Escape Scroll")
            self.chest = self.chest - 1; 
        return chestRes

    def spawnChest(self,Player):
        spawn = rand.randint(1, 100)
        add = int(10 * (Player.maxHp-Player.hp)/100)
        #print("pl hp stat ",Player.maxHp," cur ",Player.hp)
        #print("Spawn is ",spawn)
        #print("add Is ",add)
        #input()
        spawn += add
        if(spawn>0 and spawn <= 45):
            self.chest = 1
        elif(spawn>45 and spawn<=70):
            self.chest = 2
        elif(spawn>70 and spawn<=85):
            self.chest = 3
        elif(spawn>85 and spawn<=95) :
            self.chest = 4
        else :
            self.chest = 5
        return self.chest
    
    def setChest(self,counter):
        if(counter<0):
            counter=0
        self.chest=counter
    
    def getAmount(self):
        return self.chest

# Chestobj=Chest()
# Chestobj.spawnChest()
# Chestobj.openChest()