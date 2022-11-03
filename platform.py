import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#load images
background = pygame.image.load("C:/Users/705137/Downloads/dungeon.jpg")

torch = pygame.image.load("C:/Users/705137/Downloads/pixil-frame-0 (2).png")

#player variables
xpos = 70 #xpos of player
ypos = 200 #ypos of player
vx = 2 #x velocity of player
vy = 6 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#enemy variable
enemy1= [200, 630, 0]
enemy2 = [400, 780, 40]
enemy3 = [740,80,40]
def enemyMove(enemyInfo):
    enemyInfo[2]+=1
    if enemyInfo[2] <= 40:
        enemyInfo[0]+=1
    elif enemyInfo[2] <=80:
        enemyInfo[0]-=1
    else:
        enemyInfo[2] = 0 #reset timer

def enemyCollide(enemyInfo, playerX, playerY):
    if playerX+20>enemyInfo[0]:
        print("collide!", end = "")
#SOUND--------------------------------------------------------------------
jump = pygame.mixer.Sound('C:/Users/705137/Downloads/Thonny Jumping game/jump.ogg')#load in sound effect
music = pygame.mixer.music.load('C:/Users/705137/Downloads/Thonny Jumping game/music.ogg')#load in background music
pygame.mixer.music.play(-1)#start background music
#-------------------------------------------------------------------------


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
                     
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
            
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(jump) #play the jump sound
    
    #function call
    enemyMove(enemy1)
    enemyMove(enemy2)
    enemyMove(enemy3)
    
    enemyCollide(enemy1, xpos, ypos)
    #COLLISION
    if xpos>500 and xpos<600 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>450 and xpos<550 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>130 and xpos<250 and ypos+40 >470 and ypos+40 <490:
        ypos = 470-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<375 and ypos+40 >340 and ypos+40 <360:
        ypos = 340-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    elif xpos>580 and xpos<780 and ypos+40 >100 and ypos+40 <120:
        ypos = 100-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    screen.blit(background,(0,0))
    screen.blit(torch,(100,100))

    
    #screen.blit(themoon,(0,200))
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    #draw enemy
    pygame.draw.rect(screen, (255, 0, 10), (enemy1[0], enemy1[1], 20, 20))
    
    pygame.draw.rect(screen, (255, 0, 10), (enemy2[0], enemy2[1], 20, 20))
    
    pygame.draw.rect(screen, (255, 255, 0), (enemy3[0], enemy3[1], 20, 20))


    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (500, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))
    
    pygame.draw.rect(screen, (100, 0, 7), (450, 540, 100, 20))
    pygame.draw.rect(screen, (80, 100, 250), (150, 470, 120, 20))
    pygame.draw.rect(screen, (70, 20, 80), (300, 340, 75, 20))
    pygame.draw.rect(screen, (59, 186, 186), (400, 250, 100, 20))
    pygame.draw.rect(screen, (56, 150, 80), (580, 100, 200, 20))
    #change colors i dont like em

    
  
    
    pygame.display.flip()#this actually puts the pixel on the screen
     
#end game loop------------------------------------------------------------------------------
pygame.quit()
