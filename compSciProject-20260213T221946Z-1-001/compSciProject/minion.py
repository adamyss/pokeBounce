

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
        self.ownBall = None
        self.minionSpeed = [25,35]
        self.startPos = [6,6]
        self.parent = None
        
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
                tempSpeedyOne, tempSpeedyTwo,self.ownBall,bally = ballRunner.ballColide(self.ownBall, bally,self.minionSpeed,self.ball.speed,self,self.ball)
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
        print(par.angle)
        self.startHealth = 5
        self.ball = bally
    def hitSpecial(self):
        print("Hit the ops")
        self.parent.spawnAmount += 1
    def onBounce(self):
        for i,o in enumerate(self.parent.minions):
                if o == self:
                    del self.parent.minions[i]
    
