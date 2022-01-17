import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)


def ifCollide(data):
    for i in range(492, 567):
        for j in range(1200, 1300):
            if data[i, j] << 100:
                return True
    return False


# def takeScreenshot():

#     # image = ImageGrab.grab().convert('L')

#     # image.show()
#     return image


if __name__ == '__main__':
    
    time.sleep(1)

    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if ifCollide(data):
            hit("up")

        # print(assaray(image))

        # for i in range(492, 567):

        #     for j in range(1149, 1215):

        #         data[i, j] = 0
        

        # image.show()


# image.show()