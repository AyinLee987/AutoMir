import pyautogui as pg


def ss():
    ss = pg.screenshot()

    ss_path = r'screenshot/ss.png'

    ss.save(ss_path)
