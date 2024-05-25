import click
from time import sleep
import Battle
import Select
import check
import sandc
import selectSiner
import pyautogui as pg


"""用于不同事件中的行动"""


def inEvnet(name, times):
    # name == 'battle'

    # pg.moveTo(1, 1)

    if name == 'battle' or name == 'warning' or name == 'elite':

        if times == 1:
            sleep(2)
            click.keyboard('return')  # 出现了enter就点两下进入战斗
            sleep(1)
            selectSiner.check()

        click.keyboard('return')
        sleep(2)
        click.keyboard('return')
        sleep(5)

        print('into battle')

        pg.moveTo(1430, 945)

        while Battle.battle():   # 检查是否在战斗中
            click.keyboard('return')
            sleep(2)
            click.keyboard('p')
        print('out of battle')
        sleep(3)
        Select.ego()  # 检查有没有ego掉落
        sleep(2)
        Select.card()  # 检查有没有card掉落


    # name == 'boss'

    if name == 'boss':
        click.keyboard('return')
        sleep(2)
        click.keyboard('return')
        sleep(5)

        print('into battle')

        while Battle.battle() or check.bossEvent():  # 检查是否在战斗中 是否出现了事件选项
            click.keyboard('return')
            sleep(1)
            click.keyboard('p')
            sleep(1)
            # check.bossEvent()
        print('out of battle')
        sleep(3)
        Select.ego()
        sleep(2)
        Select.card()
        sleep(2)
        Select.boss()
        sleep(1)
        

    # name == 'shop'

    if name == 'shop':

        click.keyboard('return')
        sleep(1)
        click.click(1200, 600)  # click skip
        sleep(1)
        click.click(1700, 500)  # click heal
        sleep(1)
        # 检测是否需要heal
        notHeal = r'Graph/Event/needHeal.png'
        c, b = sandc.check(notHeal, Grey=False) # 以彩色图读入

        if b:  # 如果不需要治疗

            sleep(1)
            click.click(1900, 880) #selection 3
            sleep(1)
            click.click(2300, 1300) # leave
            sleep(1)
            click.click(1575, 980) # confirm
            sleep(1)
        else:
            sleep(1)
            click.click(1900, 650)  # click selection 2
            sleep(1)
            # click.click(500, 500)  # conform

            # sleep(1)
            click.click(2300, 1300)  # comform
            sleep(1)
            click.click(2300, 1300)  # leave
            sleep(1)
            click.click(1575, 980) # confirm

    # name == 'name'

    if name == 'unknown':
        print("enter into unknown")
        sleep(2)
        click.keyboard('return')
        sleep(2)
        for i in range(5):
            click.click(1200, 600)  # click skip
            sleep(0.5)
        sleep(1)

        adcheck = r'./Graph/adcheck.png'   # 七大罪检查
        c, b = sandc.check(adcheck)
        if b:
            click.click(c[0], c[1])
            for i in range(5):
                click.click(1200, 600)  # click skip
                sleep(0.5)
            click.click(2300, 1300)  # proceed
            sleep(2)
            click.click(1200, 600) # skip
            check.prob()   # 选择概率最高的罪人

        selectToGain = r'./Graph/selectToGain.png'  # select to gain选项
        c, b = sandc.check(selectToGain)
        print("the select to gain is:", b)

        if b:
            click.click(c[0], c[1] - 50)
            sleep(1)
            for i in range(5):
                click.click(1200, 600) # skip
                sleep(0.5)
            click.click(2300, 1300) # continue
            sleep(1)
            click.click(1300, 1060) # confirm

        # 如果都没找到就点第一个


# elite 与 battle合并
    # if name == 'elite':
    #     click.keyboard('return')
    #     sleep(1)
    #     click.keyboard('return')
    #     sleep(8)
    #
    #     print('into battle')
    #
    #     while Battle.battle():
    #         click.keyboard('return')
    #         sleep(2)
    #         click.keyboard('p')
    #     print('out of battle')
    #     sleep(3)
    #     Select.eego()
    #     sleep(3)
    #     Select.card()

    if name == 'bus':
        sleep(3)
        click.keyboard('return')
        for i in range(5):
            click.click(1200, 600)  # click skip
            sleep(0.5)

        notHeal = r'Graph/Event/needHeal.png'
        c, b = sandc.check(notHeal, Grey=False) # 以彩色图读入
        if b:
            sleep(1)
            click.click(1900, 880)  # selection 3
            sleep(1)
            click.click(2300, 1300)  # leave
            sleep(1)
            click.click(1575, 980) # confirm
            sleep(1)
        else:
            sleep(1)
            click.click(1520, 420) # click heal
            sleep(1)
            click.click(1900, 650) # section 2
            sleep(1)
            click.click(1200, 600) # skip
            sleep(1)
            click.click(2300, 1300) # continue
            sleep(1)
            click.click(2300, 1300) # leave
            sleep(1)
            click.click(1540, 980) # confirm




# if __name__ == '__main__':
# #     inEvnet('battle')
#
#     inEvnet('unknown')


# selectToGain = r'./Graph/selectToGain.png'
# c, b = sandc.check(selectToGain)
# print("the select to gain is:", b)
#
# if b:
#     click.click(c[0], c[1] - 50)
#     sleep(1)
#     for i in range(5):
#         click.click(500, 500)
#         sleep(1)
#     click.click(2300, 1300)
#     sleep(1)
#     click.click(1300, 1060)

if __name__ == '__main__':
    inEvnet('boss', 1)

