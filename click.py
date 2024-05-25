import win32api
import win32con
import pyautogui as pg
from time import sleep
import sandc


def keyboard(op): # 点击回车和 p 键
    VK_P = 0x50
    VK_Return = 0x0D

    hex_keycode = None
    if op == 'p':
        hex_keycode = VK_P

    elif op == 'return':
        print("         click enter")
        hex_keycode = VK_Return

    win32api.keybd_event(hex_keycode, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    win32api.keybd_event(hex_keycode, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)


def click(x, y): # 点击某个坐标 如果分辨率不为2.5k 需要乘上一个系数
    print("click")
    pg.click(x, y, button='left')


def drag(x, y): # 拖动鼠标 用于选择boss
    pg.moveTo(x, y - 200)
    pg.mouseDown(button='left')
    # sleep(0.5)

    pg.moveRel(0, 500, duration=0.5) # 拖动时间要大于等于0.5
    sleep(0.5)
    pg.mouseUp(button='left')


def scroll(): # 缩小地图
    for i in range(1, 3):
        sleep(0.1)
        pg.scroll(-100)
    sleep(2)


def enter(): # 我忘了这是个啥了
    enter = r'./Graph/enter.png'
    a, b = sandc.check(enter)
    click(a[0], a[1] - 50)
    sleep(0.2)


# pg.FAILSAFE = False