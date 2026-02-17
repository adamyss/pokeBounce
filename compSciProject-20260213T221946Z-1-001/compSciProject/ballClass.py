
class ball: 
    damage = 2
    size = 60
    startHealth = 90
    minSpeed = 12
    maxSpeed = 18
    name = "Wooper"
    photoName = "woopy.png"
    spinSpeed = 0.5
    spriteOffset = [-60,-60]
    def __init__(self):
        self.pos = [0,0]
        self.counter = 0
        self.angle = 0
        self.opBally = None
        self.speed = [13,13]
        self.opponent = None
        pass
    def updatePosition(self,posy,angle):
        self.pos[0] = posy[0]
        self.pos[1] = posy[1]
        self.angle = angle
        pass
    def initlize(self,bally,poss):
        self.opponent = bally
        self.pos[0] = poss[0]
        self.pos[1] = poss[1]   
    def setOppy(self,op,opBall):
        self.opponent = op
        self.opBally = opBall
    def onBounce(self):
        self.counter += 1
        if self.counter > 3:
            self.counter = 0
            self.damage = int(self.damage * 1.25)
        pass
    def onOpponentHit(self):
        self.damage += 2
    def onUpdate(self):
        pass

