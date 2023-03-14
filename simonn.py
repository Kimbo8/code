import pygame
import math
import random
import winsound
pygame.init()#initializes Pygame
pygame.display.set_caption("Simon!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen


#collision definition
def collision(xpos,ypos):

    if math.sqrt((xpos-400)**2 + (ypos - 400)**2)>200 or math.sqrt((xpos-400)**2 + (ypos - 400)**2)<100:
        #print("outside of ring")
        return -1

    elif xpos < 400 and ypos < 400:
        #print("red")
        pygame.draw.arc(screen, (255, 0, 0), (200, 200, 400, 400), pi /2, pi, 100)
        pygame.display.flip()
        winsound.Beep(440, 500)
        return 0
    
    elif xpos < 400 and ypos > 400:
        #print("green")
        pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
        pygame.display.flip()
        winsound.Beep(640, 500)  
        return 1
    elif xpos > 400 and ypos < 400:
        #print("yellow")
        pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400),0, pi/2, 100)
        pygame.display.flip()
        winsound.Beep(1050,500)
        return 2
    
    elif xpos > 400 and ypos > 400:
        #print("Blue")
        pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (3*pi/2), 0, 100)
        pygame.display.flip()
        winsound.Beep(840,500)
      
        return 3
        
        
#game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers in a TUPLE
hasClicked = False
playerPattern = []
turn = False
pattern = [] #this holds the random pattern
pi = 3.1415
ded = False

#draw everything first so things don't appear one at a time
pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3*pi/2),0, 100)
pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), pi/2, 0, 100)
#more colors go here!   
pygame.display.flip()




#gameloop###################################################
while True:
    #print(mousePos)
    collision(mousePos[0], mousePos[1])
    
    event = pygame.event.wait()#event queue 

    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        hasClicked = True
        turn = True
    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False
        
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
    
    
    #player turn
    print("starting player turn")
    if turn == True:
        if len(playerPattern) < len(pattern):
            if hasClicked == True:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False
        else:
            turn = False
            pygame.time.wait(800)
            
        for i in range (len(playerPattern)):
            if playerPattern[i] != pattern[i]:
                print("You lost")
    
    #update section---------------------------------------------
        
     
    if turn == False:
        print("starting machine turn")
        pattern.append(random.randrange(0, 4)) #push a new value into the pattern list
        
        #brighten colors and play beep for each number in the pattern
        for i in range(len(pattern)): 
            if pattern[i]==0: #RED
                pygame.draw.arc(screen, (255, 0,0), (200,200,400,400), pi/2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
                
            elif pattern[i]==1:#GREEN
                pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)
                
            elif pattern[i] == 2: #blue
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), (3*pi/2), 0, 100)
                pygame.display.flip()
                winsound.Beep(840,500)
                
            elif pattern[i] == 3: #yellow
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400),0, pi/2, 100)
                pygame.display.flip()
                winsound.Beep(1050,500)
                
            #redraw board after every beep
                
        pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
        pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
        pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3*pi/2), 0, 100)
        pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400),0, pi/2, 100)
        pygame.display.flip()
        pygame.time.wait(200) #slows the game down a bit
        
        turn = True
        playerPattern.clear()
    #render section---------------------------------------------
    
    #game board
    pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), (3*pi/2), 0, 100)
    pygame.draw.arc(screen, (155, 155,0 ), (200, 200, 400, 400),0, pi/2, 100)
    #more colors go here!
   
    pygame.display.flip()
    
  

#end game loop##############################################

pygame.quit()
