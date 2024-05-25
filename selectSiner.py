from time import sleep
import math
import click
import ss
import cv2
import numpy

def dist(x1, y1, x2, y2):
    # print("the points are: ", x1, y1, x2, y2)
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < 180


# 选人 第一次进入战斗会先把选人取消 然后再选人

def check():
    threshold = 0.7

    select = r'./Graph/selectSiner/select.png'
    ss.ss() # 截图
    screenshot = r'./screenshot/ss.png'
    img = cv2.imread(screenshot, 0)
    goal = cv2.imread(select, 0)

    result = cv2.matchTemplate(img, goal, cv2.TM_CCOEFF_NORMED)

    loc = numpy.where(result > threshold) # 获取所有已选的罪人的坐标

    res = [] # 储存所有可能的坐标

    for pt in zip(*loc[::-1]):
        res.append(pt)
        cv2.rectangle(img, pt, (pt[0] + 50, pt[1] + 50), (0, 0, 255), 2)

    # print(type(res))

    # 去重 判断标准为两个坐标之间的距离

    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if dist(res[i][0], res[i][1], res[j][0], res[j][1]) and i != j:
                res[j] = [-1, -1]

    ans = [] # 最终的坐标

    for i in res:
        if i[0] != -1:
            ans.append(i)

    """获取每一个selected的坐标"""

    for i in ans:
        x, y = i
        click.click(x + 80, y + 20)
        sleep(1)


    """选人"""
    origin = [600, 850]

    siners = [] # 选中的人的坐标
    row_1 = [[600, 450], [850, 450], [1100, 450], [1350, 450], [1600, 450], [1850, 450]]
    row_2 = [[600, 850], [850, 850], [1100, 850], [1350, 850], [1600, 850], [1850, 850]]

    siners.append(row_1[2])
    siners.append(row_1[3])
    siners.append(row_2[3])
    siners.append(row_2[0])
    siners.append(row_1[1])
    siners.append(row_1[4])

    for i in siners:
        click.click(i[0], i[1])
        sleep(1)


#
#
# check()