# killergame
import random #här importar jag några libraries
import os
import json 
import time 
from time import sleep
fil = ("monstername.txt") # här så gör jag en variabel för att kunna öppna olika txt filar
wes = ("wep.txt")
opwes = ("opwep.txt")
coins = 50 # här är några variblar
dmg = 3 
hp = 100
lvl = 1
ml = 1
hl = 1
level = 0
vs = ["knife"]
mhs = 5
nume = 0
filename = ["new.txt", "bul.txt"]
frames = []
rarity = ["common"]
namn = []

os.system("cls")
namn.append(input("Namn: "))

def rita(delay = 0.6, repeat = 0): #här är en loadinscreen  

    for game in filename:
        os.system("cls")
        with open(game,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for b in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system("cls")


def spara(): # här gör jag så att ja ska kunna spara variablar i en txt file
    sparaData = {
        "coins": coins,
        "hp": hp,
        "dmg":dmg,
        "level":lvl,
        "ml": ml,
        "hl": hl,
        "mhs": mhs,
        "vs": vs,
        "rarity":rarity,
        "level":level}
        
    with open('save.txt', 'w') as convert_file:
        convert_file.write(json.dumps(sparaData))






def ladda(): # här gör jag så att ja kan ladda in alla variablar in i spelet genna om att läsa in txt file save.txt
    global coins, dmg, hp, lvl, ml, hl, mhs, vs, rarity
    with open('save.txt', 'r') as convert_file:
        jsonData = json.loads(convert_file.read())
        coins = jsonData["coins"]
        hp = jsonData["hp"]
        dmg = jsonData["dmg"]
        ml = jsonData["ml"]
        hl = jsonData["hl"]
        mhs = jsonData["mhs"]
        vs = jsonData["vs"]
        rarity = jsonData["rarity"]
        level = jsonData["level"]








class monster: # här gör jag en class för monstret
    def __init__(self) -> None:
        self.mh = random.randint(50,int(100 * ml+1))  # här gör jag så att varje gång ja dödar en boss så får den mer damage och hp
        self.dh = 5 * ml+1
def start(): #här är själva start de som startar när jag kör filen
    global hp
    global nume
    os.system("cls") #detta är bara för att göra så allt ser snyggt ut
    
    os.system("cls")
    print("The Great Warlord",*namn,"\nLevel", level)
    print("Coins",coins)
    print("Health",hp)
    print("Ditt vapen är",*rarity, *vs, "med damage på", dmg)
    print("\nDu går här i skogen men framför dig hör du några vad ska du göra")  
    hem = input("1. Gå hemma och spara/ load save \n2. gå och kolla ljudet\n3. Lootbox/vapeninfo/health uppgrades\n4. Setting\n") #här ger jag alternativ av vad man vill göra
    if hem == "1":
        alt = input("1. save game\n2. load save") #här kan ja välja om ja vill save game eller load save
        if alt == "1":
            spara()
            print("save...")
        elif alt == "2":
            ladda()
            start()


    elif hem == "2":
        print("Du gör fram men ser något sorts monster vad vill du göra\n") #här så är de som händer om ja väljer a gå o kolla ljud 
        hem1 = input("1. Gå hemma och spara\n2. gå och slås mot monstret\n ") # man får välj9a
        if hem1 == "2":
            mon = monster()
            print("du är emot ", randomname("monstername.txt"), "som har", mon.mh,"hp") # man får information om monstret 
            at = input("1. Slås\n2. Springa")
            if at == "1":
                monsterfight(mon) # man börjar slås

            elif at == "2":
                lo = random.randint(1,20) # här är om man väljer att springa iväg så är de 1 i 20 chans att man dör
                if lo == 7:
                    print("monstret kom i kapp och dödade dig")
                    exit
    elif hem == "3":
        os.system("cls")
        #rita(delay = 1, repeat = 4)
        print("ditt vapen är", *vs, "med damage på", dmg)
        
        co = input("1. Öppna loot case meny\n2. Health meny\n3. Gå tillbaka\n") # här får man välja
        if co == "1":
            vs.append(lootcase(wes)) # här så öppnar man lootcase och så lägs vapnet in i en lista
            print("Du fick", *vs, "med damage på", dmg)
            start()
        elif co == "2":
            hpupg = input("1. 25 health bonus 100 coins\n2. 100 health bonus 350 coins\n 3. 500 helth bonus 1000 coins\n4. dubbla health 10000\n5. Gå tillbaka") # här får mna välja hur mycke health man vill köps
            if hpupg == "1" and coins >= 25:
                hp += 25
            elif hpupg == "2" and coins >= 350:
                hp += 100
            elif hpupg =="3" and coins >= 1000:
                hp += 500
            elif hpupg == "4" and coins >= 10000:
                hp * 2
            elif hpupg == "4":
                start()
            else: 
                print("du har inte råd eller skrev felaktigt tal")
                input("tryck enter för att fortsätta")
                start()
        elif co == "3":
            start()     
        else:
            start()       
    elif hem == "4":
        print("Setting")
        set = input("1. byta färg på text\n2. stäng ner spelet\n")
        if set == "1":
            col = input("Välj färg\n1. grön \n2. röd\n3. blå\n")
            if col == "1":
                os.system("color 2")
            elif col == "2":
                os.system("color 4")
            elif col == "3":
                os.system("color 1")
            else:
                start()
        if set == "2":
            exit()
        else:
            start()
    else:
        start()



def monsterfight(mon):
    global hp, coins, lvl, ml, hl, level # här inne så kör man monsteright
    while mon.mh > 0:  
        sleep(0.3)
        print("Du använde",*vs, "för", dmg, "damage")
        mon.mh -= dmg
        l = 0
        l = random.randint(0,1)
        if l == 1:
            hp -= mon.dh
            print("Monstret slog dig för",mon.dh, "du har nu", hp)
            if hp <= 0:
                print("\nDu döds ")
                input("Tryck enter")
                exit()
        print("Nu har monstret", mon.mh)
    if mon.mh <= 0:
        print("grattis du dödade han")
        level += 1
        coins += 50 * lvl
        lvl += 0.14
        hp = 100
        ml += random.randint(1,10)/10
        input("\ntryck enter för att fortsätta")
        
        
        start()

    
    
    

    
    
def randomname(d): # här är bara för att få randomnamn till monster
        lines = open(d).read().splitlines()
        return random.choice(lines)



def randomweponds(d): # här är för att ta slump vapen ut från txt filen
    for o in range(1):
        lin = open(d).read().splitlines()
        return random.choice(lin)


def lootcase(wes): # här är de som händer om man väljer lootcase
    global dmg
    global coins
    global rarity
    chos = input("1. Defult loot case 50 coins\n 2. Medium loot case 200 coins\n 3. Super loot case 500 coins \n 4. Ultra loot case 2000 coins\n 5. Nukes loot case 20000 coins\n")
    if chos == "1" and coins >= 50:
        dmg = random.randint(5,25)
        coins -= 50
        lin = open(wes).read().splitlines()
        rarity.clear()
        rarity.append("common")
        vs.clear()
        return random.choice(lin)
        
    elif chos == "2" and coins >= 200:
        dmg = random.randint(25,100)
        coins -= 200
        lin = open(wes).read().splitlines()
        rarity.clear()
        vs.clear()
        rarity.append("rare")
        return random.choice(lin)

    elif chos == "3" and coins >=500:
        dmg = random.randint(100,300)
        coins -= 500
        lin = open(wes).read().splitlines()
        rarity.clear()
        vs.clear()
        rarity.append("epic")
        return random.choice(lin)
    elif chos == "4" and coins >=2000:
        dmg = random.randint(300,1000)
        coins -= 2000
        lin = open(wes).read().splitlines()
        rarity.clear()
        vs.clear()
        rarity.append("Legendary")
        return random.choice(lin)
    elif chos == "5" and coins >=20000:
        dmg = random.randint(1000, 10000)
        coins -= 20000
        lin = open(wes).read().splitlines()
        rarity.clear()
        vs.clear()
        rarity.append("NUKES")
        return random.choice(lin)
    else:
        print("du har inte råd eller skrev felaktigt tal")
        input("tryck enter för att fortsätta")
        start()




start()