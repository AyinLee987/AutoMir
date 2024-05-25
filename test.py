import sandc
from time import sleep
import click
import cv2
import check


"""测试用 无实际意义"""


def unknown():
    Continue = r'Graph/Event/continue.png'

    bool = sandc.check(Continue)[1]

    while not bool:

        bool = sandc.check(Continue)[1]

        print("enter into unknown")
        sleep(2)
        click.keyboard('return')
        sleep(2)
        for i in range(4):
            click.click(1200, 600)  # click skip
            sleep(0.5)
        sleep(1)

        adcheck = r'./Graph/adcheck.png'
        c, b = sandc.check(adcheck)
        if b:
            click.click(c[0], c[1])
            for i in range(4):
                click.click(1200, 600)  # click skip
                sleep(0.5)
            click.click(2300, 1300)  # proceed
            sleep(2)
            click.click(1200, 600) # skip
            check.prob()

        selectToGain = r'./Graph/selectToGain.png'
        c, b = sandc.check(selectToGain)
        print("the select to gain is:", b)

        if b:
            click.click(c[0], c[1] - 50)
            sleep(1)
            for i in range(4):
                click.click(1200, 600) # skip
                sleep(0.5)
            click.click(2300, 1300)  # continue
            sleep(1)
            # click.click(1300, 1060)  # confirm

        else:
            click.click(1900, 500) # 第一个选项

        # click.click(2300, 1300) # continue


def test():

    factory = r'./Graph/boss/factory.png'

    img = cv2.imread(factory)

    print(img.shape)



unknown()

# test()