import cv2
import pyautogui as pg

# 截图 并检查是否存在目标 返回目标的中心坐标
# 没有找到就返回None False


def check(path, threshold=0.7, result=None, bool=None, Grey=True): # Grey = True 为灰度图像

    print(path)

    threshold = threshold
    ss = pg.screenshot() # 保存截图
    ss.save(r'./screenshot/ss.png')

    # 如果以灰度图像读取
    if Grey:
        ss = cv2.imread(r'./screenshot/ss.png', 0)

        goal = cv2.imread(path, 0)
    # 如果以彩色图像读取
    else:
        ss = cv2.imread(r'./screenshot/ss.png')

        goal = cv2.imread(path)

    result = cv2.matchTemplate(ss, goal, cv2.TM_CCOEFF_NORMED)
    upper_left = cv2.minMaxLoc(result)[3] # 返回目标的左上角坐标

    max_val = cv2.minMaxLoc(result)[1] # 返回概率
    if Grey:
        h, w = goal.shape # 返回目标的高和宽
    else:
        h, w, c = goal.shape # 返回目标的高和宽 以及通道数

    centre = ((upper_left[0] + w // 2), (upper_left[1] + h // 2))
    # centre = ((upper_left[0]), (upper_left[1]))

    print("     the max val is: ", max_val, "    the centre is: ", centre)

    if max_val > threshold: # 如果概率大于阈值 返回目标的中心坐标
        return centre, True
    else:
        return None, False



