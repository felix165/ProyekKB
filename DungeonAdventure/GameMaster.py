# Mata Kuliah Kecerdasan Buatan
# Semester Genap - Tahun 2022
# Kelompok 13
# Nathanael Abellito L - C14200073
# Filbert Ferdinand Lim - C14200184
# Jimmy Marcelino - C14200177
# Elroy Setiawan Wijaya - C14200027
# Felix - C14200165

from itertools import count
from re import T
from turtle import done
import os
import time
import random

import Character
import Assets
import Chest
import Animation
#from AnimationAssets import Animation

areaLv=1
#Player= Character.Player("Hero",areaLv)
player_inventory=[0,0,0,0]  
defaultExploreChance=60 #greater -> enemy found chance increase

# Clear Console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


def OpenInventory(Player, battle=False):
    clearConsole()
    ops=2
    while(not(ops=="1" or ops=="0")):
        time.sleep(1)
        print(Assets.menuBattleInventoryBorder)
        print(Assets.menuBattleInventoryItem1,player_inventory[0])
        print(Assets.menuBattleInventoryItem2,player_inventory[1])
        print(Assets.menuBattleInventoryItem3,player_inventory[2])
        print(Assets.menuBattleInventoryItem4,player_inventory[3])
        print(Assets.menuBattleInventoryBorder)
        print()
        print("Do you want to use an item?")
        print("[           1:Yes           0:No           ]")
        ops=input("Action: ")
        clearConsole()
    ops=int(ops)
    if(ops==0):
        time.sleep(1)
        return 2
    elif(ops==1):
        while(ops==1):
            time.sleep(1)
            print(Assets.menuBattleInventoryBorder)
            print("1.",Assets.menuBattleInventoryItem1,player_inventory[0])
            print("2.",Assets.menuBattleInventoryItem2,player_inventory[1])
            print("3.",Assets.menuBattleInventoryItem3,player_inventory[2])
            print("4.",Assets.menuBattleInventoryItem4,player_inventory[3])
            print("5.  Back")
            print(Assets.menuBattleInventoryBorder)
            print()
            print("Which Item do you want to use?")
            itemUse=int(input("Action: "))
            clearConsole()
            if(itemUse<1 or itemUse>5):
                print("Option Invalid")
            elif(itemUse==5):
                return
            elif(player_inventory[itemUse-1] <= 0):
                print("Item Is Empty")
            elif(player_inventory[itemUse-1] >= 1):
                if(itemUse==1):
                    if(Player.hp == Player.maxHp):
                        print("HP is full")
                        print("Item can't be used now")
                    else:
                        Player.recoverHp(10)
                        player_inventory[itemUse-1]-=1
                        print("Low Potion is Used")
                        print("Recovering 10% HP")
                        print('''HP      : ''',Player.hp,'''/''',Player.maxHp)
                        if(battle):
                            return 0
                elif(itemUse==2):
                    if(Player.hp == Player.maxHp):
                        print("HP is full")
                        print("Item can't be used now")                        
                    else:
                        Player.recoverHp(25)
                        player_inventory[itemUse-1]-=1
                        print("Mid Potion is Used")
                        print("Recovering 25% HP")
                        print('''HP      : ''',Player.hp,'''/''',Player.maxHp)
                        if(battle):
                            return 0
                elif(itemUse==3):
                    if(Player.hp == Player.maxHp):
                        print("HP is full")
                        print("Item can't be used now")                        
                    else:
                        Player.recoverHp(70)
                        player_inventory[itemUse-1]-=1
                        print("High Potion is Used")
                        print("Recovering 70% HP")
                        print('''HP      : ''',Player.hp,'''/''',Player.maxHp)
                        if(battle):
                            return 0
                elif(itemUse==4):
                    if(not(battle)):
                        print("Item can't be used now")
                    else:
                        #escape item
                        print("Escape Scroll is Used")
                        player_inventory[itemUse-1]-=1
                        return 1

            time.sleep(3)
            clearConsole()
            while(not(ops=="1" or ops=="0")):
                print(Assets.menuBattleInventoryBorder)
                print(Assets.menuBattleInventoryItem1,player_inventory[0])
                print(Assets.menuBattleInventoryItem2,player_inventory[1])
                print(Assets.menuBattleInventoryItem3,player_inventory[2])
                print(Assets.menuBattleInventoryItem4,player_inventory[3])
                print(Assets.menuBattleInventoryBorder)
                print()
                print("Still want to use an item?")
                print("[           1:Yes           0:No           ]")
                ops=input("Action: ")
            ops=int(ops)
        time.sleep(1)
        return 0

def foundChest(Player,counter=-1):
    ChestObj=Chest.Chest
    if(counter>=0):
        ChestObj.setChest(ChestObj,counter)
    else:
        counter=ChestObj.spawnChest(ChestObj,Player)
    Animation.chest(counter)
    itemFound=ChestObj.openChest(ChestObj,Player)
    for i in itemFound:
        player_inventory[i]+=1
    time.sleep(2)
    print("Press Enter Continue...")
    input()
    print()
    clearConsole()

def battle(Player=Character.Player("Hero",1), Enemy=Character.Enemy("Monster",1,Character.Player("Hero",1),False)):
    time.sleep(1)
    clearConsole()
    time.sleep(0.5)
    turn=1
    while(True):
        #Player Turn
        Animation.yourTurn()
        time.sleep(1)
        clearConsole()
        Enemy.statusBattle()
        print()
        Player.statusBattle()
        print(Assets.menuBattle)
        ops=int(input("Input: "))
        if(ops==1):
            #Attack
            clearConsole()
            Player.status()
            print("""                              0. Back""")
            attack=int(input("Action: "))
            if(attack>=1 and attack<=3): #Back if 0
                time.sleep(0.75)
                clearConsole()
                damage=Player.attack(attack-1)
                if(damage>0): #Back if skill can not be used
                    turn+=1
                    Enemy.hit(damage)
                    time.sleep(0.5)
                    clearConsole()
                    Enemy.statusBattle()
                    if(Enemy.die):
                        #Enemy Die
                        Animation.youwin()
                        if(Enemy.dropChest()):
                            return 1 #WIN #Drop Chest
                        else:
                            return 0 #WIN #No Drop Chest
                else:
                    time.sleep(1.2)
                    clearConsole()
                    continue
            elif(attack==0):
                time.sleep(0.5)
                clearConsole()
                continue
            else:
                clearConsole()
                time.sleep(1.2)
                print("Action Invalid")
                time.sleep(0.5)
                print("Try Another Action")
                continue

        elif(ops==2):
            #Open Inventory
            time.sleep(1.5)
            escape=OpenInventory(Player,True)
            if(escape==1):
                Animation.escape()
                return -1
            elif(escape==2):
                continue
            print()
            time.sleep(1)

        elif(ops==3):
            #Escape
            time.sleep(0.75)
            clearConsole()
            print("Attempting to Escape...")
            time.sleep(1.5)
            rate=random.randint(0,100)
            if(rate>=21):
                print("Escape Failed")
            else:
                #Escape
                print("Escape Succesfull")
                Animation.escape()
                return -1
            time.sleep(1)
        else:
            print("Action Invalid")
            print("Try Another Action")
            time.sleep(1)
            continue
        
        #Enemy Turn
        Animation.enemyTurn()
        #Animation.Slime()
        escape=Enemy.escape()   
        if(escape):
            time.sleep(1)
            Animation.youwin()
        else:
            time.sleep(1)
        clearConsole()

        Enemy.attack()
        time.sleep(2)
        clearConsole()
        Player.statusBattle()
        time.sleep(1.5)
        if(Player.die):
            
            Player.life -= 1
            
            if(Player.life > 0):
                Player.die=False
                Player.mp=Player.maxMP
                Animation.youLose()
                print("Player Live Left ",Player.life,"x")
                input("Press Enter To Continue...")
                Player.recoverHp(100)
                return 0
            else:
                Animation.youLose()    
                clearConsole()
                time.sleep(0.5)
                Animation.gameOver()
                return -1
        turn+=1
        if(Player.mp < Player.maxMP):
            Player.mp += 1


# ========================================================================
#mainMenuTitle
def Start(startAreaLevel=1):
    #playerLifes=3

    clearConsole()
    Animation.loading(None)
    clearConsole()
    ops=0
    while (ops!=3):
        print(Assets.mainMenuTitleAlt)
        ops=int(input("Action: "))    
        clearConsole()

        #StartGame
        if(ops==1):
            print("Hello Traveler!!!")
            print("Thank you for coming")
            time.sleep(2)
            clearConsole()
            print("Let's start your Journey")
            print()
            playerName=input("Input Your Name: ")
            time.sleep(1)
            clearConsole()
            areaLv=startAreaLevel
            Player= Character.Player(playerName,(startAreaLevel*5)-4)
            #Player.level=6
            #untuk test-----------------------------------------------------------------------------------------------------------------------------------------------------------------
            #Player.hp -= 99
            explorePity=defaultExploreChance #greater -> enemy found chance increase
            dispMap=random.randint(0,len(Assets.mapArray)-1)
            opsIn=0

            #Exploring
            while(opsIn!=4):
                clearConsole()
                #Game Over?
                if(Player.life == 0):
                    print("Game Over")
                    break
                print(Assets.mapArray[dispMap])
                print("""
                                             Level Area: """,areaLv)
                print(Assets.mainMenu)
                opsIn=int(input("Action: "))
                time.sleep(1)
                clearConsole()

                if(opsIn==1):
                    explRand=random.randint(0,100)
                    if(explRand<=explorePity and Player.level >=(areaLv*5)+1):
                        #battle with boss
                        explorePity-=10
                        Animation.boss()
                        Animation.fight()
                        Enemy=Character.Enemy("Demon Lord",areaLv,Player,True)
                        res=battle( Player,Enemy)
                        if(res==-1):
                            continue
                        elif(res==0):
                            Player.recoverHp(100)
                            print("Another Chance")
                        elif(res==1):
                            foundChest(Player,5)
                        if(Enemy.die):
                            Animation.bossDefeated()
                            #next area
                            dispMap=random.randint(0,len(Assets.mapArray)-1)
                            areaLv+=1
                            continue

                    elif(explRand<=explorePity):
                        #battle with normal monster
                        explorePity-=10
                        Animation.slime()
                        Animation.fight()
                        Enemy=Character.Enemy("Slime",areaLv,Player,False)
                        res=battle(Player,Enemy)
                        if(res==-1):
                            continue
                        elif(res==0):
                            Player.recoverHp(100)
                            
                            print("Another Chance")
                        elif(res==1):
                            foundChest(Player,-1)
                    else:
                        #Found Chests
                        explorePity=defaultExploreChance
                        foundChest(Player,-1)

                #Open Status Window
                elif(opsIn==2):
                    Player.status()
                    print("Press Enter Continue...")
                    input()
                    print()
                    
                #Open Inventory
                elif(opsIn==3):
                    OpenInventory(Player,False)
                    print()
                elif(opsIn==4):
                    Animation.gameOver()
                else:
                    print("Invalid Action")

        #Credits    
        elif(ops==2):
            Animation.credits()
            print("Press Enter Continue...")
            input()
            print()
            clearConsole()
        #Exit Program
        elif(ops==3):
            Animation.exit()
            break

        #...
        else:
            print("Action Invalid")
            print("Try Another Action")


#----------------------------------------------------------------------------------
#default areaLV=1
Start()
