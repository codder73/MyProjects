import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab #pip install pillow
from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(500, 650):#It is the width
        for j in range(950, 1250):#
            if data[i, j] < 1000:
              return True
    return False


# def draw():

if __name__=='__main__':
    # print("Hey... Dino Game will start in 3 seconds")
    time.sleep(1)#it will sleep the time then it will 
    # hit('up')
    # while True:
    image = ImageGrab.grab().convert('L')#.convert('L') changes the photo into black and white form 
    data = image.load()
        # if isCollide(data):
            # hit("up")
    for i in range(500, 650):#It is the width
        for j in range(1000, 1100):#
            data[i, j]==0
            print(asarray(image))


    image.show()
        