from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import array
import time

class Cordinates:
    reply_btn = (480, 500)
    t_rax = (210, 535)

def restart_game():
    # pyautogui.click(Cordinates.t_rax)
    pyautogui.click(Cordinates.reply_btn)

def press_space():
    pyautogui.keyDown('space')
    # time.sleep(0.02)
    print("Jump")
    pyautogui.keyUp('space')

def image_grab():
    print(Cordinates.t_rax[0]+60,\
        Cordinates.t_rax[1],\
        Cordinates.t_rax[0]+110,\
        Cordinates.t_rax[1]+50)
    box = (Cordinates.t_rax[0]+60,\
        Cordinates.t_rax[1],\
        Cordinates.t_rax[0]+100,\
        Cordinates.t_rax[1]+50)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = array(gray_image.getcolors())
    print(a.sum())
    return a.sum()

# restart_game()
# while True:
#     image_grab()

def main():
    restart_game()
    while True:
        if image_grab() != 2247:
            press_space()
            time.sleep(0.1)

main()
# restart_game()
# time.sleep(1)
# press_space()
# (410, 535) (310, 535)
# data = (Cordinates.t_rax[0]+100, Cordinates.t_rax[1])
# data = (Cordinates.t_rax[0]+300, Cordinates.t_rax[1]+100)
# print(data)
# pyautogui.click(data)