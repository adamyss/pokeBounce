import random
import pygame
import pygame.locals
import ballClass
import os
import math
import fibonaciBall
width = 800
height = 800
def main():
    shinyOdds = 10
    pygame.init()
    clock = pygame.time.Clock()
    width = 800        
    height = 800
    screen_res = (width, height)
    fps = 60
    textColor = (50,50,50)
    screen = pygame.display.set_mode(screen_res)
    pygame.display.set_caption("BALL")
    ballies = []
    ballies.append(ballClass.ball())
    ballies.append(fibonaciBall.fibonaciy())
    ballies.append(fibonaciBall.skibidi())
    ballies.append(fibonaciBall.spinda())
    ballies.append(fibonaciBall.quaxly())
    selectedIndexOne = 2
    selectedIndexTwo = 4
    bally = ballies[selectedIndexOne]
    ballyTwo = ballies[selectedIndexTwo]
    ballyTwo.initlize(bally,[width/2 + 150,height/2])
    bally.initlize(bally,[width/2 - 150,height/2])
    numyOne = random.randint(1,shinyOdds)
    numyTwo = random.randint(1,shinyOdds)
    # its midnight rn idk WHY but I must code shinies instead of going to sleep
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    if numyOne == 1:
        bally.photoName = "s" + bally.photoName
        print("SHINY")
    if numyTwo == 1:
        ballyTwo.photoName = "s" + ballyTwo.photoName
        print("SHINY")
    imgyPath = os.path.join(scriptDir, bally.photoName)
    print(imgyPath)
    imgy = pygame.image.load(imgyPath)
    imgy = pygame.transform.scale(imgy,(bally.size * 2,bally.size * 2))
    imgyPathTwo = os.path.join(scriptDir,ballyTwo.photoName)
    imgyTwo = pygame.image.load(imgyPathTwo)
    imgyTwo = pygame.transform.scale(imgyTwo,(ballyTwo.size * 2,ballyTwo.size * 2))
    bgPath = os.path.join(scriptDir,"towny.png")
    bgImg = pygame.image.load(bgPath)
    bgImg = pygame.transform.scale(bgImg,(width,height))
    sizeOne = bally.size
    sizeTwo = ballyTwo.size
    healthOne = bally.startHealth
    healthTwo = ballyTwo.startHealth
    rotateValOne = random.uniform(0,360)
    rotateValTwo = random.uniform(0,360)
    colorOne = (0,0,0)
    colorTwo = (0,0,0)
    forceQuit = False
    ballOne = pygame.draw.circle(
        surface=screen, color=colorOne, center=[bally.pos[0],bally.pos[1]], radius=sizeOne)
    ballTwo = pygame.draw.circle(
        surface=screen, color=colorTwo, center=[ballyTwo.pos[0], ballyTwo.pos[1]], radius=sizeTwo)
    font = pygame.font.SysFont("arial", 32)
    playerOneWins = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                forceQuit = True
        clock.tick(fps)
        orig_rect = imgy.get_rect()
        rot_image = pygame.transform.rotate(imgy, rotateValOne)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        imgyTemp = rot_image.subsurface(rot_rect).copy()
        orig_rect = imgyTwo.get_rect()
        rot_image = pygame.transform.rotate(imgyTwo, rotateValTwo)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        imgyTwoTemp = rot_image.subsurface(rot_rect).copy()
        rotateValOne += bally.spinSpeed
        rotateValTwo += ballyTwo.spinSpeed
        if rotateValOne > 360:
            dif = rotateValOne - 360
            rotateValOne = dif
        if rotateValTwo > 360:
            dif = rotateValTwo - 360
            rotateValTwo = dif
        sizeOne = bally.size
        sizeTwo = ballyTwo.size
        bally.speed = ballCollisionCheck(bally.speed,ballOne,bally)
        ballyTwo.speed = ballCollisionCheck(ballyTwo.speed,ballTwo,ballyTwo)
        screen.blit(bgImg,[0,0])
        healthOne = bally.startHealth
        healthTwo = ballyTwo.startHealth
        if healthOne <= 0:
            running = False
        if healthTwo <= 0:
            running = False
            playerOneWins = True
        ballOne = ballOne.move(bally.speed[0]*0.5,bally.speed[1]*0.5)
        ballTwo = ballTwo.move(ballyTwo.speed[0]*0.5,ballyTwo.speed[1] * 0.5)
        bally.updatePosition([ballOne.centerx,ballOne.centery],rotateValOne)
        ballyTwo.updatePosition([ballTwo.centerx,ballTwo.centery],rotateValTwo)
        bally.setOppy(ballyTwo,ballTwo)
        ballyTwo.setOppy(bally,ballOne)
        if pygame.Vector2(ballOne.center).distance_to(ballTwo.center) < sizeOne + sizeTwo:
            tempSpeedyOne, tempSpeedyTwo,ballOne,ballTwo = ballColide(ballOne, ballTwo,bally.speed,ballyTwo.speed,bally,ballyTwo)
            bally.onOpponentHit()
            ballyTwo.onOpponentHit()
            bally.speed[0], bally.speed[1] = tempSpeedyOne[0], tempSpeedyOne[1]
            ballyTwo.speed[0], ballyTwo.speed[1] = tempSpeedyTwo[0], tempSpeedyTwo[1]
        pygame.draw.circle(surface=screen, color=colorOne,
                        center=[bally.pos[0],bally.pos[1]], radius=sizeOne)
        pygame.draw.circle(surface=screen, color=colorTwo,
                        center=[ballyTwo.pos[0], ballyTwo.pos[1]], radius=sizeTwo)
        healthTextOne = font.render(str(healthOne), True, (textColor))
        screen.blit(imgyTemp,[bally.pos[0] + bally.spriteOffset[0],bally.pos[1] + bally.spriteOffset[0]])
        screen.blit(imgyTwoTemp,[ballyTwo.pos[0] + ballyTwo.spriteOffset[0],ballyTwo.pos[1] + ballyTwo.spriteOffset[0]])
        screen.blit(healthTextOne,(ballOne[0]+sizeOne/1.5,ballOne[1]+sizeOne/1.5 - 75))
        healthTextTwo = font.render(str(healthTwo), True, (textColor))
        screen.blit(healthTextTwo,(ballTwo[0]+sizeTwo/1.5,ballTwo[1]+sizeTwo/1.5 - 75))
        bally.onUpdate()
        ballyTwo.onUpdate()
        damage = font.render(f'p1 Damage: {bally.damage} p2 Damage: {ballyTwo.damage}', True, (textColor))
        screen.blit(damage,(width/2-150,height - 100))
        pygame.display.flip()
    showWinning = True
    while showWinning and forceQuit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showWinning = False
        screen.blit(bgImg,[0,0])
        winning = None
        if playerOneWins:
            screen.blit(imgy,[width/2 + bally.spriteOffset[0],height/2 + bally.spriteOffset[1]])
            winning = font.render(f'Winner: {bally.name}', True, (textColor))
        else:
            screen.blit(imgyTwo,[width/2 + ballyTwo.spriteOffset[0],height/2 + ballyTwo.spriteOffset[1]])
            winning = font.render(f'Winner: {ballyTwo.name}', True, (textColor))
        screen.blit(winning,(width/2-125,500))
        pygame.display.flip()
    
screen = pygame.display.get_surface()

def ballColide(ballA, ballB, speedOne, speedTwo, s1, s2):
    # Math I stole from the internet :D
    x1, y1 = ballA.center
    x2, y2 = ballB.center
    vx1, vy1 = speedOne
    vx2, vy2 = speedTwo
    nx = x2 - x1
    ny = y2 - y1
    dist = math.hypot(nx, ny)
    if dist == 0:
        return [5, 5], [5, 5], ballA, ballB
    nx /= dist
    ny /= dist
    p1 = vx1 * nx + vy1 * ny
    p2 = vx2 * nx + vy2 * ny
    vx1_new = vx1 + (p2 - p1) * nx
    vy1_new = vy1 + (p2 - p1) * ny
    vx2_new = vx2 + (p1 - p2) * nx
    vy2_new = vy2 + (p1 - p2) * ny
    vx1_new = max(vx1_new, s1.minSpeed) if vx1_new > 0 else min(vx1_new, -s1.minSpeed)
    vy1_new = max(vy1_new, s1.minSpeed) if vy1_new > 0 else min(vy1_new, -s1.minSpeed)
    vx2_new = max(vx2_new, s2.minSpeed) if vx2_new > 0 else min(vx2_new, -s2.minSpeed)
    vy2_new = max(vy2_new, s2.minSpeed) if vy2_new > 0 else min(vy2_new, -s2.minSpeed)
    s1.startHealth -= s2.damage
    s2.startHealth -= s1.damage
    overlap = (s1.size + s2.size) - dist
    if overlap > 0:
        correction = pygame.Vector2(nx, ny) * (overlap / 2)
        ballA = ballA.move(-correction.x, -correction.y)
        ballB = ballB.move(correction.x, correction.y)
    return [vx1_new, vy1_new], [vx2_new, vy2_new], ballA, ballB
def ballCollisionCheck(ogSpeed,ball,script):
    speedy = ogSpeed
    if ball.left <= 0:
        speedy[0] = random.uniform(script.minSpeed,script.maxSpeed)
        script.onBounce()
    if ball.right >= width:
        speedy[0] = random.uniform(-script.minSpeed,-script.maxSpeed)
        script.onBounce()
    if ball.top <= 0:
        speedy[1] = random.uniform(script.minSpeed,script.maxSpeed)
        script.onBounce()
    if ball.bottom >= height:
        speedy[1] = random.uniform(-script.minSpeed,-script.maxSpeed)
        script.onBounce() 
    return speedy
def drawMinion(pos,color,speed,obj):
    screen = pygame.display.get_surface()
    pos[0] = pos[0] +speed[0]
    pos[1] = pos[1] + speed[1]
    bally = pygame.draw.circle(surface=screen, color=color,
                center=(pos[0],pos[1]), radius=8)
    newSpeed = ballCollisionCheck(speed,bally,obj)
    return pos,newSpeed,bally
# this is due to Anirvinya carrying and it stops the main stuff from getting called on imports
if __name__ == '__main__':
    main()