import ballClass
import minion
import threading
import time
class fibonaciy(ballClass.ball):
    name = "Porygon"
    photoName = "zorygon.png"
    spinSpeed = 0
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
    spawnAmount = 8
    minions = []
    spawned = False
    minionDamage = 2
    startHealth = 175
    def onBounce(self):
        pass
    def onOpponentHit(self):
        self.minionDamage += 1
        threading.Thread(target=self.spawnMinionsWithDelay).start()
    def spawnMinionsWithDelay(self):
        for i in range(self.spawnAmount):
            miniony = minion.quaxlyMinion()
            miniony.initilize(self.opponent, self.pos, self)
            self.minions.append(miniony)
            time.sleep(0.075) 
    def onUpdate(self):
        for miniony in self.minions:
            if miniony != None:
                miniony.updateMinion(self.opBally)


    
               
