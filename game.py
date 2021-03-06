import pygame
from pygame.locals import *
import random
import sys
import threading
import ai
import fileStuf as files


WIDTH = 480
HEIGHT = 720
FPS = 120
SPEED = 1
MARGIN = 4

TILE_WIDTH = 120
TILE_HEIGHT = 180


def newRow(rows):
    tile = random.randrange(0, 4)
    if len(rows) == 0:
        return [tile, 0, False]
    top = rows[len(rows) - 1][1] - TILE_HEIGHT-MARGIN
    return [tile, top, False]





def game():

    global SURF, FPSCLOCK

    name = input()


    rows = []
    for i in range(5):
        rows.append(newRow(rows))
    pos = None
    clicked = False
    score = 0
    while True:
        SURF.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = True

        if clicked:
            for row in rows:
                limits = [row[0]*120, (row[0]+1)*120, row[1], row[1]+180]
                if row[1]<0:
                    limits[2] = 0
                elif limits[3]>720:
                    limits[3] = 720
                
                if  limits[0]<=pos[0]<=limits[1] and limits[2]<=pos[1]<=limits[3]:
                    row[2] = True
                    score +=1
                    break
            clicked = False



        if rows[0][1] > HEIGHT:
            rows.append(newRow(rows))
            if not rows[0][2]:
                endGame(score)
                break
            rows.pop(0)
        for row in rows:
            color = (0, 0, 0) if not row[2] else (0, 187, 255)
            pygame.draw.rect(SURF, color,  pygame.Rect(TILE_WIDTH*row[0], row[1], TILE_WIDTH, TILE_HEIGHT))
            row[1]+=SPEED
        FPSCLOCK.tick(FPS)
        pygame.display.update()
    highScore = files.findHighScore()
    
    if score>highScore:
        print("New High Score")
        files.newHighScore(name, highScore)
    

    

        

        

def endGame(score):
    global SURF
    pygame.font.init()
    fontObj = pygame.font.Font('font.ttf', 100)
    textSurfaceObj = fontObj.render(str("Game\nOver\n\nScore = " + str(score)), True, (0, 0, 255), (127, 127, 127))
    SURF.blit(textSurfaceObj,(0, 0))
    pygame.display.update()






def main():
    pygame.init()
    global SURF, FPSCLOCK
    SURF = pygame.display.set_mode((WIDTH, HEIGHT))
    FPSCLOCK = pygame.time.Clock()
    SURF.fill((255, 255, 255))
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game()

if __name__ == '__main__':
    GAME = threading.Thread(target = main)
    
    GAME.start()

    
