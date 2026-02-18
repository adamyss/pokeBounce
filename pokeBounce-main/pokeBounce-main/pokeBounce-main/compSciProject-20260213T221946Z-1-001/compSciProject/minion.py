

import random

class minionObj:
    minSpeed = 5
    maxSpeed = 7
    damage = 3
    size = 8
    startHealth = 5
    colory = (118,251,255)
    def __init__(self):
        self.ball = None
        self.invincible = False
        self.ownBall = None
        self.minionSpeed = [25,35]
        self.startPos = [6,6]
        self.parent = None
        self.maxVal = 0
        
    def initilize(self,bally,startPosy,par):
        self.startPos[0] = startPosy[0]
        self.startPos[1] = startPosy[1]
        self.parent = par
        self.minionSpeed = [-par.speed[0],random.uniform(self.minSpeed,self.maxSpeed)]
        self.startHealth = 5
        self.ball = bally
    def updateMinion(self,bally):
        import ballRunner
        self.damage = self.parent.minionDamage
        self.startPos,self.minionSpeed,self.ownBall = ballRunner.drawMinion(self.startPos,self.colory,self.minionSpeed,self)
        if self.ownBall != None:
             if ballRunner.pygame.Vector2(self.ownBall.center).distance_to(bally.center) < self.ball.size + self.size: 
                tempSpeedyOne, tempSpeedyTwo,self.ownBall,bally,bad = ballRunner.ballColide(self.ownBall, bally,self.minionSpeed,self.ball.speed,self,self.ball)
                if bad == True:
                    return
                self.minionSpeed[0], self.minionSpeed[1] = tempSpeedyOne[0], tempSpeedyOne[1]
                self.ball.speed[0], self.ball.speed[1] = tempSpeedyTwo[0], tempSpeedyTwo[1]
                self.hitSpecial()
                for i,o in enumerate(self.parent.minions):
                    if o == self:
                        del self.parent.minions[i]
    def hitSpecial(self):
        self.parent.minionDamage += 1          
    def onBounce(self):
        pass
class quaxlyMinion(minionObj):
    speedMult = 15
    angleOffset = 0
    colory = (0,0,255)
    def initilize(self,bally,startPosy,par):
        import math
        self.startPos[0] = startPosy[0]
        self.startPos[1] = startPosy[1]
        self.parent = par
        r = math.radians(-(par.angle + self.angleOffset))
        # more math I stole cause math is hard :D
        self.minionSpeed = [math.cos(r) * self.speedMult,math.sin(r) * self.speedMult]
        self.startHealth = 5
        self.ball = bally
    def hitSpecial(self):
        self.parent.spawnAmount += 1
    def onBounce(self):
        for i,o in enumerate(self.parent.minions):
                if o == self:
                    del self.parent.minions[i]
class fishion(minionObj):
    speedMult = 95
    angleOffset = 0
    colory = (0,255,0)
    minSpeed = 0
    maxSpeed = 0 
    index = 0
    ogOffset = 0
    def initilize(self,bally,startPosy,par,ind):
        import math
        self.invincible = False
        self.startPos[0] = startPosy[0]
        self.startPos[1] = startPosy[1]
        self.parent = par
        self.maxVal = self.parent.index
        self.angleOffset = 360/self.parent.index * self.index
        r = math.radians(-(par.angle + self.angleOffset))
        # more math I stole cause math is hard :D
        self.offsety = [math.cos(r) * self.speedMult,math.sin(r) * self.speedMult]
        self.startHealth = 5
        self.ball = bally
        self.index = ind
    def updateMinion(self,bally):
        import ballRunner
        import math
        self.damage = self.parent.minionDamage
        self.minionSpeed = [0,0]
        self.angleOffset = 360/self.parent.index * self.index
        r = math.radians(-(self.parent.angle + self.angleOffset))
        # more math I stole cause math is hard :D
        self.offsety = [math.cos(r) * self.speedMult,math.sin(r) * self.speedMult]
        self.startPos = [self.parent.pos[0] + self.offsety[0],self.parent.pos[1] + self.offsety[1]]
        self.useless =[0,0]
        self.useless,self.useless,self.ownBall = ballRunner.drawMinion(self.startPos,self.colory,self.useless,self)
        if self.ownBall != None:
            if ballRunner.pygame.Vector2(self.ownBall.center).distance_to(bally.center) < self.ball.size + self.size: 
                tempSpeedyOne, tempSpeedyTwo,self.ownBall,bally,bad = ballRunner.ballColide(self.ownBall, bally,self.minionSpeed,self.ball.speed,self,self.ball)
                if bad == True:
                    return
                self.minionSpeed[0], self.minionSpeed[1] = tempSpeedyOne[0], tempSpeedyOne[1]
                self.ball.speed[0], self.ball.speed[1] = tempSpeedyTwo[0], tempSpeedyTwo[1]
                self.hitSpecial()
                for i,o in enumerate(self.parent.minions):
                    if o == self:
                        self.parent.index -= 1
                        del self.parent.minions[i]
    def hitSpecial(self):
        self.parent.spawnAmount += 1

    
