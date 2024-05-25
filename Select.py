import click
import sandc
from time import sleep


def ego():

    ego = r'./Graph/finish2.png'

    a, b = sandc.check(ego, 0.7)

    if b:
        click.click(a[0], a[1])
        sleep(1)
        click.click(2300, 1100) # select ege
        sleep(1)
        click.click(1300, 1050) # confirm
    else: return



"""普通战斗也有选卡 逻辑需要改"""
def card():
    card = r'./Graph/Event/card.png'
    a, b = sandc.check(card)

    if b:
        click.click(900, 700)
        sleep(1)
        click.click(1650, 1050)
        sleep(1)
        click.click(1300, 1050)


def boss():
    boss4 = r'boss/boss4.png'
    c, b = sandc.check(boss4)
    if b:
        click.drag(c[0], c[1])
        sleep(8)
    else:
        click.drag(600, 600)


def eego():

    eego = r'./Graph/finish2.png'
    a, b = sandc.check(eego, 0.4)
    if b:
        click.click(a[0], a[1])
        sleep(1)
        click.click(2300, 1100) # select
        sleep(1)
        click.click(1300, 1060) #

