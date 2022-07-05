from encodings import utf_8
import os, time
import Assets

# Clear Console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


#----------------------------------------------------------------------------------------------------------
def swordSlash():
    time.sleep(1)
    clearConsole()
    for i in range (3):
        for j in Assets.swordslashAssets:
            print(j)
            time.sleep(0.25)
            clearConsole()
    time.sleep(1.5)
    clearConsole()

def fireBlast():
    time.sleep(1)
    clearConsole()
    for i in range (2):
        for j in Assets.fireblastAssets:
            print(j)
            time.sleep(0.15)
            clearConsole()
    time.sleep(1.5)
    clearConsole()

def fop():
    time.sleep(1)
    clearConsole()
    for i in range (2):
        for j in Assets.fopAssets:
            print(j)
            time.sleep(0.125)
            clearConsole()
    time.sleep(1.5)
    clearConsole()

def slime():
    time.sleep(1)
    clearConsole()
    for i in range (2):
        for j in Assets.slimeAssets:
            print(j)
            time.sleep(0.2)
            clearConsole()
    time.sleep(1.5)
    clearConsole()

def loading(level= None):
    if level is None :
        print("WELCOME TRAVELER")
    else:
        print("Level", (level+1))
    print("Loading . . .")
    print("Don't Click Anything")
    time.sleep(1)
    for i in range (100):
        clearConsole()
        if level is None :
            print("WELCOME TRAVELER")
        else:
            print("Level", level+1)
        print("Loading", end=" ")
        print((i+int(1)),"%")
        print("Don't Click Anything")
        time.sleep(0.015)
    time.sleep(2)

def load():
    aset=[Assets.loading1,Assets.loading2,Assets.loading3]
    time.sleep(1)
    for i in range (3*3):
        clearConsole()
        print(aset[i%3])
        print("Don't Click Anything")
        time.sleep(1/3)
    time.sleep(1.5)
    clearConsole()

def boss():
    time.sleep(1)
    clearConsole()
    string = Assets.bossSprite
    print(string)
    time.sleep(2)
    clearConsole()
    string = Assets.boss
    print(string)
    time.sleep(2)
    clearConsole()

def bossDefeated():
    time.sleep(1)
    clearConsole()
    string = Assets.bossDefeated
    print(string)
    time.sleep(2)
    clearConsole()

def gameOver():
    time.sleep(1)
    clearConsole()
    string = Assets.gameOver
    print(string)
    time.sleep(4)
    clearConsole()

def oouch():
    time.sleep(0.5)
    clearConsole()
    string = Assets.oouch
    print(string)
    time.sleep(1)
    clearConsole()

def youwin():
    time.sleep(1)
    clearConsole()
    string = Assets.youWin
    print(string)
    time.sleep(1.5)
    clearConsole()

def youLose():
    time.sleep(1)
    clearConsole()
    string = Assets.youLose
    print(string)
    time.sleep(1.5)
    clearConsole()

def yourTurn():
    time.sleep(0.7)
    clearConsole()
    string = Assets.yourTurn
    print(string)
    time.sleep(1.5)
    clearConsole()

def enemyTurn():
    time.sleep(1)
    clearConsole()
    string = Assets.enemyTurn
    print(string)
    time.sleep(1.5)
    clearConsole()

def escape():
    time.sleep(1)
    clearConsole()
    string = Assets.escape
    print(string)
    time.sleep(2)
    clearConsole()

def fight():
    time.sleep(1)
    clearConsole()
    string = Assets.fight
    print(string)
    time.sleep(1)
    clearConsole()

def chest(amount=1):
    time.sleep(1)
    clearConsole()
    print(Assets.congratulation)
    time.sleep(1)
    clearConsole()
    for i in range (amount):
        print(Assets.chestAscii)
        time.sleep(0.5)
    time.sleep(1.5)
    
def exit():
    import sys
    time.sleep(1)
    clearConsole()
    string = Assets.exit
    print(string)
    time.sleep(4)
    clearConsole()
    time.sleep(1)
    clearConsole()
    string = Assets.thankYou
    print(string)
    time.sleep(6)
    sys.exit()

def credits():
    time.sleep(1)
    clearConsole()
    for i in Assets.credits:
        print(i)
        time.sleep(1)
    time.sleep(4)
    print()
