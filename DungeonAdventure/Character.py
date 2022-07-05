import os
from pydoc import doc
import time
import random
import Animation
#from AnimationAssets import Animation

#Nama Skill, Scale attack Power, MP cost
#PlayerSkill = [("Basic Attack", 1, 0),
#            ("Fireball", 1.5, 3), 
#            ("Meteor", 3, 5)]

class Character():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.maxHp = 75 + (level*25)
        self.hp = self.maxHp
        self.atkPower=15+(level*5)
        self.die=False
        #Opsional
        self.maxMP = 10 #(level*10)
        self.mp = self.maxMP

    def levelUp(self):
        self.level += 1
        self.maxHp+=25
        self.atkPower+=5
        #Recover health and MP when level up
        self.recoverHp(100)
        self.mp = self.maxMP
    
    def recoverHp(self,percentage):
        self.hp += self.maxHp*(percentage/100)
        #Agar tidak melebihi maxHP ketika Heal
        if(self.hp > self.maxHp):
            self.hp = self.maxHp
    
    def hit(self,damage):
        self.hp-=damage
        if(self.hp<=0):
            self.hp=0
            self.die=True     

class Player(Character):
    def __init__(self, name, level,life=3):
        self.life = life
        super().__init__(name, level)
        #self.life = life
        self.expLimit = 100*(pow((1.5), (self.level-1)))
        self.exp = 0
        self.skill = [
            ("Sword Slash        ", 1.0, 0),
            ("Fire Blast         ", 2, 2), 
            ("Flames of Purgatory", 3.5, 5)]
    
    def levelUp(self):
        super().levelUp()
        self.expLimit = (100*(pow((1.5), (self.level-1))))
    
    def expIncrease(self,expAm):
        self.exp = self.exp + expAm
        if(self.exp >=self.expLimit):
            self.exp-=self.expLimit
            self.levelUp()
            
    def attack(self, choice):
        attack = self.skill[choice]
        #info
        print(self.name+" used "+attack[0])
        time.sleep(1)
        if(choice ==0):
            self.mp +=1
            if (self.mp > self.maxMP):
                self.mp = self.maxMP
            damage = self.atkPower * attack[1]
            print("Total Damage: ",damage)
            time.sleep(1)
            if(choice==0):
                Animation.swordSlash()
            return damage
        else:
            if(self.mp < attack[2]):
                print("Not Enough Mana")
                print("Do another Action")
                return -1 
            else:
                #Mana Player dikurangi oleh Mana Cost Jenis Attack
                self.mp -= attack[2]
                damage = self.atkPower * attack[1]
                print("Total Damage: ",damage)
                time.sleep(1)
                if(choice==1):
                    Animation.fireBlast()
                elif(choice==2):
                    Animation.fop()
                return damage

    def statusBattle(self):
        print('''
                            ================== STATUS ==================
                            Name    : ''',self.name,''' 
                            Lv      : ''',self.level,'''
                            HP      : ''',self.hp,'''/''',self.maxHp,'''
                            Attack  : ''',self.atkPower,'''      
                            MP      : ''',self.mp,'''/''',self.maxMP,''' 
                            ================== STATUS ==================
              '''  )
    def status(self):
        print('''
                            ===================== STATUS ======================
                            Name    : ''',self.name,''' 
                            Lv      : ''',self.level,'''
                            HP      : ''',self.hp,'''/''',self.maxHp,'''
                            Attack  : ''',self.atkPower,'''      
                            MP      : ''',self.mp,'''/''',self.maxMP,''' 
                            EXP     : ''',(self.exp/self.expLimit)*100,''' %''','''          
                            Skill   :
              ''')
        for i in range(0,len(self.skill)):
            print('                           ',(i+1),'. ',self.skill[i][0],' ATK : ',self.skill[i][1]*self.atkPower,' MP Cost : ',self.skill[i][2])
        print('''                          
                            ===================== STATUS ======================''')
        
class Enemy(Character):
    def __init__(self, name,areaLevel, player,isBoss=False):
        self.isBoss=isBoss
        self.player=player
        self.areaLevel=areaLevel
        
        if(isBoss):
            level = (areaLevel * 5) + 5 
            #Difficulty Reductor/Increase
            pity = (3-player.life)
            level -= pity
            #print("Pity Level is ",pity)
            if(level <= 0):
                level=1
            #print(level)
        else:
            rate=random.randint(1,100)
            ratepity=random.randint(0,15) * (3 - player.life) 
            rate-=ratepity
            if(rate<=60):
                level = player.level
            elif(rate<=70):
                if(player.level >1):
                    level = random.randint((areaLevel * 5) - 4, player.level-1)
                else:
                    level = random.randint((areaLevel * 5) - 4, 1)
            elif(rate<=100):
                level = random.randint(player.level+1, areaLevel * 5)  
            #print("Level Before Update Is ",level )
            #input()
            #Difficulty Reductor
            pity = (3-player.life)
            level -= pity
            #print(level)
            if(level <= 0):
                level=1
            #print(level)

        super().__init__(name, level)    
        if(isBoss):
            self.maxHp*= 1.4
            self.hp=self.maxHp
            self.atkPower*= 0.8
            self.skill=[
                ("Shadow Slash", 0.7, 0),
                ("Dark Pulse  ", 1.3, 3), 
                ("Black Void  ", 2, 6)]
            #alternatif names : Shadow Blade, Soul Absorbtion, Domination of darkness, Terroring Nightmare, Dark Pulse 
        else:
            self.maxHp*= 1
            self.hp=self.maxHp
            self.atkPower*= 0.8
            self.skill=[
                ("Basic Attack", 0.7, 0),
                ("Power Attack", 1.0, 3), 
                ("Super Attack", 1.6, 6)]
        
    def attack(self):
        skillCount = len(self.skill)-1
        flag = False
        while (flag == False):
            choice = random.randint(0,skillCount)
            attack = self.skill[choice]
            if(self.mp > attack[2]):
                flag = True
                
        if(choice ==0):
            self.mp +=1
            if (self.mp > self.maxMP):
                self.mp = self.maxMP
                
        print(self.name+" used "+attack[0])
        print()
        #Mana Enemy dikurangi oleh Mana Cost Jenis Attack
        self.mp -= attack[2]
        damage = self.atkPower * attack[1]
        Animation.oouch()
        self.player.hit(damage)
        print("Total Damage: ", damage)
        
        return damage

    def statusBattle(self):
        print('''
                            ================== ENEMY ===================
                            Name    : ''',self.name,''' 
                            Lv      : ''',self.level,'''
                            HP      : ''',self.hp,'''/''',self.maxHp,'''
                            Attack  : ''',self.atkPower,'''
                            MP      : ''',self.mp,'''/''',self.maxMP,'''      
                            ================= ENEMY ===================
              ''')
        
    def dropChest(self):
        if(self.die):
            if(self.isBoss):
                return True
            else:
                rate = random.randint(1, 100)
                if(self.player.hp/self.player.maxHp >= 50):
                    if (rate <= 30):
                        return False
                    else:
                        return True #Drop Chests
                else:
                    if (rate <= 10):
                        return False
                    else:
                        return True #Drop Chests

    def hit(self,damage):
        super().hit(damage)
        if(self.die):
            self.player.expIncrease((pow(self.level,2)/(self.player.level))*70*self.areaLevel)
    
    def escape(self):
        if(self.isBoss):
            return False
        else:
            flag = False
            if (self.hp < self.maxHp*0.2):
                rate = random.randint(1, 100)
                
                if(self.level <= self.player.level):
                    if (rate <= 15):
                        flag = True   
                        print("Enemy Escape!!!")  
                    else:
                        print("Enemy Failed to Escape")
            return flag
    




            
        