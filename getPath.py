from ultralytics import YOLO
import yolov5
import cv2
import check
import ss
import click
import math
from time import sleep

"""计算距离 防止选到boss"""
def dist(x, y, mex, mey):
    return math.sqrt((x - mex) ** 2 + (y - mey) ** 2) < 500



"""确定目标的名字"""
def select(loc, me):

    print('into select')
    name = 'None'
    for i in range(len(loc)): # 选择目标 条件： 1. 选到的目标不是我 2. 选到的目标在我右边
        if dist(loc[i][1], loc[i][2], me[0], me[1]) and loc[i][1] > me[0]:
            x, y, name = loc[i][1], loc[i][2], loc[i][0]
            print("name in select: ", name)
            loc[i] = ['None', -1, -1] # 删除已经选中的目标
            click.click(x, y)
            sleep(2)
            if check.check(): # 如果出现enter界面
                return name
            else:
                continue   # 如果没有出现进入的界面就换下一个目标


def getLoc():
    print('into getLoc')

    toName = ['battle', 'me', 'unknown', 'boss', 'bus', 'shop', 'elite', 'warning']
    toList = [0, 1, 2, 3, 4, 5, 6, 7]

    ss.ss()
    cv2.imread(r'screenshot/ss.png')
    # 通过yolo模型判定地图上的节点及种类
    model = YOLO(r'C:\Users\25988\PycharmProjects\pythonProject2\model\best.pt')
    img = cv2.imread(r'screenshot/ss.png')  # BGR
    results = model.predict(img)

    ans = results[0].boxes.xyxy # 获取坐标
    loc = []
    cnt = 0

    for i in ans: # i表示一个目标的坐标
        x1, y1, x2, y2 = i
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cls = results[0].boxes.cls.tolist()
        loc.append([toName[int(cls[cnt])], (x1 + x2) // 2, (y1 + y2) // 2]) # 储存目标的名字和坐标
        cnt += 1

    return loc

            # cv2.circle(img, centre, 50, (0, 255, 0), -1)
            # cv2.imshow('test', img)
            # cv2.waitKey(20000)


def getMe(loc): # 返回我的坐标 并删除我
    print('into getMe')
    x = -1
    y = -1
    for i in range(len(loc)):
        if loc[i][0] == 'me':
            x = loc[i][1]
            y = loc[i][2]
            loc[i] = ['None', -1, -1]
            break
    return [x, y]


def getPath():
    print("into getPath")
    click.scroll() # 缩放地图 确保有目标可选
    loc = getLoc() # 获取所有可走的目标的坐标

    me = getMe(loc)

    # print(me)

    name = select(loc, me) # 目标的名字
    print("name in getPath: ", name)
    return name, True


# if __name__ == '__main__':
#     getPath()

