from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

class Coordinates():
    replay_button = (481, 375)
    top_of_dino = (223, 379)
    obstacle = (359, 1036)
    
def image_grab():
    box = (223, 379, 359, 1036)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = array(gray_image.getbands())
    print(a)

def restart():
    pyautogui.click(Coordinates.replay_button)

def jump():
    pyautogui.keyDown("Space")
    pyautogui.keyUp("Space")

restart()
while True:
    image_grab()


#jump()


# Nefunguje jak ma
# image_grab ma nejspis spatne X a Y
# taky je treba upravit vypis "a"