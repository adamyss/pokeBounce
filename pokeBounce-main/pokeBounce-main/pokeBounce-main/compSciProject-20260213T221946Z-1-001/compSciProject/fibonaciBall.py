import ballClass
import minion
import threading
import time
class fibonaciy(ballClass.ball):
    name = "Porygon"
    photoName = "zorygon.png"
    description = "When hitting the opponent, its damage goes to the next number in the Fibonaci sequence"
    previousValue = 2
    previousTwo = 3
    damage = 3
    def onBounce(self):
        pass
    def onOpponentHit(self):
        self.damage = self.previousValue + self.previousTwo
        self.previousTwo = self.previousValue
        self.previousValue = self.damage
    def onUpdate(self):
        pass

class skibidi(ballClass.ball):
    name = "Squirtle"
    photoName = "squirt.png"
    description = "Spawns bubbles (amount increases on hit) that damage opponent"
    spawnAmount = 1
    minions = []
    spawned = False
    minionDamage = 1
    startHealth = 100
    def onBounce(self):
        pass
    def onOpponentHit(self):
        for i in range(self.spawnAmount):
            miniony = minion.minionObj()
            miniony.initilize(self.opponent,self.pos,self)
            self.minions.append(miniony)
        self.spawnAmount += 1
    def onUpdate(self):
        counter = 0
        for miniony in self.minions:
            if miniony != None:
                miniony.updateMinion(self.opBally)
class spinda(ballClass.ball):
    name = "Spinda"
    photoName = "spiny.png"
    description = "Hitting the wall increases spin speed hitting an opponent lowers it, damage scales with spin speed"
    previousValue = 2
    previousTwo = 3
    damage = 3
    size = 45
    spriteOffset = [-45,-45]
    def onBounce(self):
        self.spinSpeed *= 1.5
    def onOpponentHit(self):
        self.spinSpeed /= 8
        if self.spinSpeed < 0.5:
            self.spinSpeed = 0.5
    def onUpdate(self):
        self.damage = int(self.spinSpeed * 1.5)
class quaxly(ballClass.ball):
    name = "Quaxly"
    photoName = "duck.png"
    description = "Shoots a water beam when hitting the opponent the more it hits the bigger the next water beam is"
    spawnAmount = 6
    minions = []
    spawned = False
    shot = False
    minionDamage = 2
    startHealth = 175
    shotRate = 1.25
    spinSpeed = 1
    def onBounce(self):
        self.shotRate *= 0.95
    def onOpponentHit(self):
        self.minionDamage += 1
    def spawnMinionsWithDelay(self):
        for i in range(self.spawnAmount):
            miniony = minion.quaxlyMinion()
            miniony.initilize(self.opponent, self.pos, self)
            self.minions.append(miniony)
            time.sleep(0.03)
        time.sleep(self.shotRate) 
        threading.Thread(target=self.spawnMinionsWithDelay).start()   
    def onUpdate(self):
        if self.shot == False:
            threading.Thread(target=self.spawnMinionsWithDelay).start()
            self.shot = True
        for miniony in self.minions:
            if miniony != None:
                miniony.updateMinion(self.opBally)
class fish(ballClass.ball):
    name = "Wishawashi"
    photoName = "fish.png"
    description = "Is a fish"
    spawnAmount = 1
    minions = []
    minionDamage = 2
    startHealth = 75
    spinSpeed = 1
    minionSpeed = 0
    index = 1
    def onBounce(self):
        pass
    def onOpponentHit(self):
        self.spawnMinionsWithDelay()
        self.minionDamage += 0.5
    def spawnMinionsWithDelay(self):
        for i in range(self.spawnAmount):
            miniony = minion.fishion()
            miniony.initilize(self.opponent, self.pos, self,self.index)
            self.minions.append(miniony)
            self.index += 1
    def onUpdate(self):
        for miniony in self.minions:
            if miniony != None:
                miniony.updateMinion(self.opBally)
            else:
                print("miniony is noney")

    
               
