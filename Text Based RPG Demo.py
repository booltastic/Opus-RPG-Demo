import random

class God:
    def __init__(self,name,level,atk,defe,hp,exp,money,magic,equipment):
        self.name=name
        self.atk=atk
        self.defe=defe
        self.hp=round(hp, 0)
        self.magic=magic
        self.exp=exp
        self.money=money
        self.equipment=equipment
        self.level=level
    def myfunc(self):
        print(self.name+'\nLevel: '+str(self.level)+'\nAttack: '+str(self.atk)+"\nDefense: "+str(self.defe)+"\nMagic: "+str(self.magic)+"\nHP: "+str(self.hp)+'\nMoney: '+str(self.money)+'\nExperience: '+str(self.exp)+'/'+str(explimit)+'\nEquipment: '+str(self.equipment)+'\n')
class Equipment:
    def __init__(self,name,wepatk,armor,magic,cost):
        self.name=name
        self.wepatk=wepatk
        self.armor=armor
        self.magic=magic
        self.cost=cost
    def equipstats(self):
        print(self.name+' - Atk: '+str(self.wepatk)+', Def: '+str(self.armor)+', Magic: '+str(self.magic)+', Cost: '+str(self.cost))

# class DMG:
#     def DMGRounder(self,damage):
#         damage=round(damage,2)
#Character List
Chad=God('Chad',1,10,10,200,0,60,0,[])
Spinny=God('Spinny',300,350,350,10000,500,500,0,[])

#Item list
Dagger=Equipment('Dagger',20,0,0,10)
Shield=Equipment('Shield',0,15,0,30)
GodSword=Equipment('God Sword',150,0,0,250)
Dchain=Equipment('Dragon Chainmail',0,150,0,250)
Spellbook=Equipment('Spellbook',0,0,1,50)

ItemList = [Dagger.name, Shield.name, GodSword.name,Dchain.name, Spellbook.name]
#######Chapter 1########
sleep=0
fight=0
firstfight=0
exploring=0
finalboss=0
spellbook=0
victory=0
explimit=100
mana=3
goblin2=0
Location='Forest'
while exploring==0:
    while firstfight==0:
        input('Welcome to RPG Game Demo. Enjoy the ride...[Press Enter to continue dialogue]') #enter key disregards any anyput and moves to next line
        input('...')
        input('...Loading...')
        input('You are Chad.')
        slept = 0
        while sleep==0:
            input('You wake up in the middle of a dark forest. Horrified, you take in your surroundings...')
            if slept == 0:
                input('Not much to see besides big trees. But then rustling in the bushes...')
                input("Holy crap. You're surrounded by goblins!!!")
            else:
                input("Holy crap. You're STILL surrounded by goblins!!!")

            print('--------------------\nEnter Key: Fight\n1: Start Running\n2: Try to fall back asleep.')
            Next=input('Input an answer: ')
            if Next=='':
                input('\nTime to fight! (Press Enter to continue)\n')
                firstfight=1
                sleep = 1
                fight=1
            if Next=='1':
                input('You try to run. You trip and die. Whoops.\nGame over.')
                exit()
            if Next=='2':
                input('You manage to fall back asleep. ...')
                input('Several hours pass. ...')
                sleep=0
                slept=1
    #Fight Sequence
    while fight==1:
        if finalboss == 1:
            finalboss=0
            Goblin1=Spinny
            Goblin1.hp = 1000
        else:
            if goblin2==1:
                Goblin1 = God('Elite Goblin', 10, random.randrange(85, 135, 1), random.randrange(105, 145, 1),random.randrange(200, 500, 5),random.randrange(50, 75, 1), random.randrange(25, 50, 1), 0, ['Elite Goblin Armor'])
            else:
                Goblin1 = God('Goblin', 1, random.randrange(15, 35, 1), random.randrange(10, 20, 1),random.randrange(50, 100, 5),random.randrange(15, 20, 1), random.randrange(5, 10, 1), 0, [])
        print('--------------------\n')
        Goblin1.myfunc()
        GobMaxHP=round(Goblin1.hp,0)

        input('--------------------\nYou enter combat!!!')
        while Goblin1.hp>0:
            if mana > 3:
                mana = 3
            if Chad.hp <= 0:
                input('I-....I am sorry LD. I have failed you... Spinny, she is all yours...')
                input('Game Over.')
                exit()
            print('\n--------------------\nWhat would you like to do?\nEnter: Basic attack.\n1: Use evasive maneuvers\n2. Cast a spell (Mana is '+str(mana)+'/3) [1 Mana AutoRecharge Per Combat Turn]\n3: View your stats\n"Run" to retreat.\nEnter a response: ')
            action=input('')

            battle=0 #this stops the battle from restarting when it loops
            if action=='3':
                print('\n')
                Chad.myfunc()
                battle=1
                input('Press Enter to continue...')
            #Magic Attack
            while action=='2':
                if spellbook==1:
                    if mana==3:
                        if Chad.magic>=100:
                            spellcast='Supernova'
                        if Chad.magic>=50 and Chad.magic<100:
                            spellcast='Nuke'
                        if Chad.magic<50 and Chad.magic>=25:
                            spellcast='Fireball'
                        if Chad.magic<25 and Chad.magic>=10:
                            spellcast='Icicle'
                        if Chad.magic<10:
                            spellcast='Strong Wind'
                        input('--------------------\nYou read from your spellbook and cast '+spellcast+'!')
                        damage = round(Chad.magic * (random.randrange(200, 250, 5) / 100),0)
                        Goblin1.hp = Goblin1.hp - damage
                        if spellcast=='Supernova':
                            print('You have rained death and chaos upon this realm!')
                        if spellcast=='Nuke':
                            print('You have decimated the landscape!')
                        if spellcast=='Fireball':
                            print('You launch a fireball at the enemy. Everything is now covered in fire!')
                        if spellcast=='Icicle':
                            print('You launch a sharp icicle at the enemy!')
                        if spellcast == 'Strong Wind':
                            print('You mildly inconvenienced the enemy!')
                        print('You deal ' + str(damage) + ' damage!')

                        Chad.magic=Chad.magic+2
                        mana=mana-3
                        if Goblin1.hp <= 0:
                            victory = 1
                            input('\n'+Goblin1.name+' has '+str(Goblin1.hp)+'/'+str(GobMaxHP)+' HP left!\n'+Goblin1.name+' has died!\n')
                            fight = 0
                            action = 0
                        else:
                            print(Goblin1.name + ' has ' + str(Goblin1.hp) + '/' + str(GobMaxHP) + ' HP left!')
                            input('You get a little better at magic! (Magic skill increased slightly)\n')
                            print(Goblin1.name + ' strikes you back!')
                            goblindamage = round((Goblin1.atk * (random.randrange(89, 131, 10) / 100)) - (
                                        Chad.defe * (random.randrange(49, 76, 5) / 100)),0)
                            if goblindamage < 0:
                                goblindamage = 0
                            Chad.hp = Chad.hp - goblindamage
                            print(Goblin1.name + ' deals ' + str(goblindamage) + ' damage!')
                            input('You have ' + str(Chad.hp) + ' HP left!')
                            action = 1
                            battle = 1
                    else:
                        input('\nI need to wait until my mana recharges more first (Spell Mana Cost: 3')
                        action=1
                        battle = 1
                else:
                    input("\nUhh, abra kadabra? I don't know any spells yet. Maybe a spellbook would help?")
                    action=1
                    battle = 1
            #Evasive Attack
            while action=='1':
                print('--------------------\nYou use evasive maneuvers!')
                damage = round(Chad.atk * (random.randrange(55, 80, 5) / 100),0)
                Chad.hp=Chad.hp+15
                Goblin1.hp = Goblin1.hp - damage
                print('You confuse '+Goblin1.name+' and deal ' + str(damage) + ' damage!')
                print('You manage to catch your breath and restore 15HP!')
                mana = mana + 1
                if Goblin1.hp <= 0:
                    victory = 1
                    input('\n'+Goblin1.name+' has '+str(Goblin1.hp)+'/'+str(GobMaxHP)+' HP left!\n'+Goblin1.name+' has died!')
                    fight = 0
                    action = 0
                else:
                    print(Goblin1.name + ' has ' + str(Goblin1.hp) + '/' + str(GobMaxHP) + ' HP left!')
                    input(Goblin1.name + ' strikes you back!')
                    goblindamage = round((Goblin1.atk * (random.randrange(89, 151, 10) / 100)) - (
                                Chad.defe * (random.randrange(60, 80, 5) / 100)),0)
                    if goblindamage < 0:
                        goblindamage = 0
                    Chad.hp = Chad.hp - goblindamage
                    print('\n'+Goblin1.name + ' deals ' + str(goblindamage) + ' damage!')
                    input('You have ' + str(Chad.hp) + ' HP left!')
                    action = 1
                    battle = 1
            #Normal Attack
            while action=='':
                print('--------------------\nYou attack!')
                damage=round(Chad.atk*(random.randrange(89, 151, 5)/100),0)
                crit=random.randrange(9, 21, 1)
                if crit==20:
                    damage=round(damage*1.5,2)
                    print('Critical strike! Extra damage dealt!')
                Goblin1.hp=Goblin1.hp-damage
                print('You deal '+str(damage)+' damage!')
                mana = mana + 1
                if Goblin1.hp<=0:
                    victory=1
                    input('\n'+Goblin1.name+' has '+str(Goblin1.hp)+'/'+str(GobMaxHP)+' HP left!\n'+Goblin1.name+' has died!')
                    fight=0
                    action=0
                else:
                    print(Goblin1.name+' has '+str(Goblin1.hp)+'/'+str(GobMaxHP)+' HP left!')
                    input(Goblin1.name+' strikes you back!')
                    goblindamage=round((Goblin1.atk*(random.randrange(89, 151, 10)/100))-(Chad.defe*(random.randrange(9, 51, 10)/100)),0)
                    if goblindamage<0:
                        goblindamage=0
                    Chad.hp=Chad.hp-goblindamage
                    print('\n'+Goblin1.name+' deals '+str(goblindamage)+' damage!')
                    input('You have '+str(Chad.hp)+' HP left!')
                    action=1
                    battle=1
            else:
                if battle == 0:
                    Goblin1.hp=0
                    fight=0
    if victory==1:
        input('\n--------------------\n\nYou win! You gain '+str(Goblin1.exp)+' exp and '+str(Goblin1.money)+' money. Congrats idiot.\n')
        Chad.exp=Chad.exp+Goblin1.exp
        Chad.money=Goblin1.money+Chad.money
        victory=0
        choosestat=0
        #print(Chad.exp)

        if Chad.exp>=explimit:
            Overflow=Chad.exp-explimit
        if Chad.exp>=explimit:
            while choosestat==0:
                statincrease=input('Level up! Choose a stat to increase!\n1. Attack power\n2. Defense\n3. Magic Power\nEnter the corresponding number: ')
                if statincrease=='1':
                    Chad.atk=Chad.atk+5
                    print('Attack increased by 5!')
                    choosestat=1
                if statincrease=='2':
                    Chad.defe=Chad.defe + 5
                    print('Defense increased by 5!')
                    choosestat = 1
                if statincrease=='3':
                    Chad.magic=Chad.magic+5
                    print('Magic increased by 5!')
                    choosestat = 1

            Chad.hp = Chad.hp + 100
            input('Restored 100HP!\n')
            Chad.exp=Overflow
            explimit=explimit+10
            Chad.level=Chad.level+1
        #Goblin1=Goblin
        print('--------------------\n')
        Chad.myfunc()
        input('Press Enter to continue...')
    NextDecision=input('--------------------\nWhat will be your next move?\n\nLocation: '+Location+'\n\nEnter Key: Fight again \n1: Rest at the inn. (30HP for 7 dollars) \n2: Fight the final boss \n3: Enter the shop.\n4. View character\n5. Change area\nEnter a response: ')
    if NextDecision == '':
        fight=1
    if NextDecision == '1':
        input('You feel well rested, and more healthy than before.')
        Chad.hp=Chad.hp+30
        Chad.money=Chad.money-7
        NextDecision=99
    if NextDecision == '2':
        finalboss=1
        fight=1
    #Shop
    if NextDecision == '3':
        print('--------------------\nYou spot a traveling salesman walking down a nearby path. He looks like a friendly face.\n')
        print("'Howdy! Hyuck hyuck! My name is J1!")
        input("'What u finna buy cuhhhh!?' (Press Enter to proceed)\n")
        while NextDecision=='3':
            print('--------------------\n')
            ShopItems=[Dagger.equipstats(),Shield.equipstats(),GodSword.equipstats(),Dchain.equipstats(),Spellbook.equipstats()]
            print('\nYou have '+str(Chad.money)+' money available.\nWhat would you like?\n')
            buyitem=input('Items in stock: '+str(ItemList)+'\nType what you want or hit "Enter" to leave: ')
            #buy=input('Would you like to buy sumn?\n1. '+Dagger.name+'\n2. '+Shield.name+'\n3. '+GodSword.name+'\n4. '+Spellbook.name+'\nChoose one: ')
            if buyitem=='':
                NextDecision = 99
            else:
                if buyitem=='Dagger':
                    buy=Dagger.cost
                    name=Dagger.name
                if buyitem=='Shield':
                    buy=Shield.cost
                    name = Shield.name
                if buyitem=='God Sword':
                    buy=GodSword.cost
                    name = GodSword.name
                if buyitem == 'Dragon Chainmail':
                    buy = Dchain.cost
                    name = Dchain.name
                if buyitem=='Spellbook':
                    buy=Spellbook.cost
                    name = Spellbook.name
                if Chad.money>=buy:
                    try:
                        ItemList.remove(name)
                        Chad.money = Chad.money - buy
                        input(name + ' purchased and equipped! (Press Enter to proceed)\n')
                        Chad.equipment.append(name)
                        if buyitem == 'Dagger':
                            Chad.atk = Dagger.wepatk + Chad.atk
                        if buyitem == 'Shield':
                            Chad.defe = Shield.armor + Chad.defe
                        if buyitem == 'God Sword':
                            Chad.atk = GodSword.wepatk + Chad.atk
                        if buyitem == 'Dragon Chainmail':
                            Chad.defe = Dchain.armor + Chad.defe
                        if buyitem == 'Spellbook':
                            Chad.magic = Spellbook.magic + Chad.magic
                            spellbook=1
                    except ValueError:
                        input('\nYou already bought that!\n')
                else:
                    input('\nYou lack the funds to buy that! (Press Enter to continue)\n')

    if NextDecision == '4':
        print('\n')
        Chad.myfunc()
        input('Press Enter to continue...')
    if NextDecision == '5':
        if goblin2==0:
            input('\nYou spot a path nearby. You have a feeling there are stronger monsters down that way.')
            if Chad.level>=1:
                cave=input('\nYou spot a cave. Check it out?\n1: Proceed\n2: Turn back\nEnter an answer: ')
                if cave=='1':
                    goblin2=1
                    Location='Cave'
                    input('\nYou follow the path down to a cave. You enter and find yourself among dangerous elite goblins. Better be careful!\n')
                else:
                    input('\nYou decide to not explore the cave quite yet.')
        else:
            forest=input('\nYou are currently in the cave. Would you like to go back to the forest?\n1. Go back to the forest\n2. Stay in the cave\nEnter an answer: ')
            if forest=='1':
                goblin2=0
                Location='Forest'
                input('\nYou decide to go back to the forest.')
            else:
                input('\nYou decide to remain in the cave.')
    # else:
    #     print('ok game over')
    #     exit()