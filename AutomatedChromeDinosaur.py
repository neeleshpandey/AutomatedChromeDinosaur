import pyautogui
from PIL import ImageGrab 
import time

def pressKey(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):
# Check colison for birds
    for i in range(750, 800):    #Random numbers Works for me, adjust according to dinosaur's position
        for j in range(255, 275):
            if data[i, j] > 100:    #{if data[i, j] > 100:} for Dark Mode in chrome | for light mode use {if data[i, j] < 100:}
                pressKey("down")
                return
 # Check colison for cactus
    for i in range(750, 800):
        for j in range(290,310):
            if data[i, j] > 100:    #{if data[i, j] > 100:} for Dark Mode in chrome | for light mode use {if data[i, j] < 100:}
                pressKey("up")
                return
    return

if __name__ == "__main__":
    print("Start in 5 seconds")
    print("open chrome dinosaur")
    time.sleep(5)
    pressKey('up') 
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
       

        # # # Draw the rectangle for birds    #Uncomment this and adjust x1,x2 and y1,y2 values
        # for i in range(750, 800):           #This Will be the area checked before jump or dodge
        #     for j in range(255, 275):
        #         data[i, j] = 100

        # # Draw the rectangle for cactus   
        # for i in range(750, 800):
        #     for j in range(290,310):
        #          data[i, j] = 0
        
        # image.show()
        # break