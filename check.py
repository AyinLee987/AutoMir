import click
import sandc
from time import sleep


def finish(): # 用于完成事件 以后再实现
    pass


def Factory():
    click.click(1200, 600)  # skip
    sleep(1)
    click.click(1550, 670)  # No
    sleep(1)
    click.click(2300, 1300)  # proceed
    sleep(1)
    click.click(1200, 600)  # skip


def bossEvent():
    skip = r'Graph/boss/skip.png'

    c, b = sandc.check(skip) # 通过skip检测是否进入事件界面
    # sleep(1)

    if b:
        for i in range(5):
            click.click(1200, 600) # skip
            sleep(1)

        factory = r'Graph/boss/factory.png' # 工厂事件 阶段1
        c1, b1 = sandc.check(factory, 0.8)
        if b1:
            click.click(c1[0], c1[1])
            sleep(1)
            click.click(1200, 600) # skip
            sleep(1)
            click.click(2300, 1300) # continue
            return True

        button = r'Graph/boss/button.png' # 工厂事件阶段二
        c2, b3 = sandc.check(button, 0.8)
        if b3:
            for i in range(3):
                Factory()
            return True
        if True:
            prob()

            click.click(1890, 530) # first selection
            sleep(1)
            for i in range(2):
                click.click(1200, 600)  # skip
                sleep(1)
            for i in range(2):
                click.click(1200, 600)
                sleep(1)
            click.click(2300, 1300)  # continue

            return True



            # click.click(1200, 600) # skip
            # sleep(1)
            # click.click(1900, 680) # No
            # sleep(1)
            # click.click(2300, 1300) # proceed
            # sleep(1)
            # click.click(1200, 600) # skip
            #
            # click.click(1200, 600)  # skip
            # sleep(1)
            # click.click(1900, 680)  # No
            # sleep(1)
            # click.click(2300, 1300)  # proceed
            # sleep(1)
            # click.click(1200, 600)  # skip
            #
            # click.click(1200, 600)  # skip
            # sleep(1)
            # click.click(1900, 680)  # No
            # sleep(1)
            # click.click(2300, 1300)  # proceed
            # sleep(1)
            # click.click(1200, 600)  # skip
            # sleep(1)
            # click.click(2300, 1300) # continue


def check(): # 检查是否出现enter
    print('enter into check')

    enter = r'./Graph/enter.png'
    a, b = sandc.check(enter, 0.7)
    print(b)
    return b


def bool(path):  # 用于检查概率
    a, b = sandc.check(path)
    if b:
        click.click(a[0], a[1]) # 点击概率坐标
        sleep(0.5)
        click.click(2300, 1250) # proceed
        sleep(3)
        for i in range(5):
            click.click(1200, 600)
            sleep(0.3)
        sleep(2)
        click.click(2300, 1300)  # continue
        sleep(2)
        click.click(1300, 1060)  # confirm
        sleep(1)
        click.click(1280, 890)
        return b
    else:
        return False


def prob(): # 问号事件中的概率选择
    sleep(2)
    print("veryHigh")
    veryHigh = r'./Graph/Prob/veryHigh.png'
    if bool(veryHigh):
        return

    print("high")
    high = r'./Graph/Prob/high.png'
    if bool(high):
        return

    print("normal")
    normal = r'./Graph/Prob/normal.png'
    if bool(normal):
        return

    print("low")
    low = r'./Graph/Prob/veryLow.png'
    if bool(low):
        return


if __name__ == '__main__':
    prob()

