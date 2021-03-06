import pyautogui as auto
from PIL import Image
import pyscreenshot as shot

def main():
    ss = shot.grab(bbox = (720, 210, 720+480, 210+700))
    y = 699
    run = True

    while run:

    
        
        while y >= 0 :
            X = 0
            while X<4:
                x = X*120 + 50
                print(x, y)
                if ss.getpixel((x, y)) == (0, 0, 0):
                    
                    auto.click(x+720, y+215)
                    y -= 184
                    X = 0
                    if y< 0 :
                        break
                    continue
                X+=1



                    
            y-=50
        
        
        
        y = 199
        ss = shot.grab(bbox=(720, 210, 720+480, 210+200))




