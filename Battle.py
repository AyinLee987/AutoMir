import sandc
from time import sleep


def battle():
    # 通过检查是否出现了wave&turn和stop来判断是否在战斗中

    waveTurn = r'./Graph/wave&turn.png'
    stop = r'./Graph/stop.png'

    q, a = sandc.check(waveTurn)
    w, b = sandc.check(stop)

    if a or b:  # 二次检查 确保在战斗中
        return True

    sleep(3)

    q, a = sandc.check(waveTurn, 0.8)
    w, b = sandc.check(stop, 0.8)

    if a or b:
        return True

    else:
        return False
