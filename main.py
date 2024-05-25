# import getPath
# import inEvent
# import threading
# import time
# from pynput import keyboard
#
#
# def keyboard_on_press(key):
#     global  isEnd
#
#     if key == keyboard.Key.esc:
#         isEnd = True
#         return False
#
#
# def start_key_listener():
#     with keyboard.Listener(on_press=keyboard_on_press) as listener:
#         listener.join()
#
#
# def test():
#
#     times = 0
#
#     while True:
#         print("enter into main fuc, next will exe getPath")
#         name = getPath.getPath()
#
#         if name == 'battle' or name == 'warning' or name == 'elite':
#             times += 1
#
#         print("in main fuc, next will exe inEvent")
#
#         inEvent.inEvnet(name, times)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=start_key_listener)
#     t1.start()
#
#     t2 = threading.Thread(target=test())
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("end")
#
#
#
#
#
#
#
#
#
import getPath
import inEvent
import threading
from pynput import keyboard
import check

isEnd = False


"""监听器 按下esc时终止程序"""


def keyboard_on_press(key):
    global isEnd

    if key == keyboard.Key.esc:
        isEnd = True
        return False


def start_key_listener():
    with keyboard.Listener(on_press=keyboard_on_press) as listener:
        listener.join()


def test(): # 主函数入口
    global isEnd

    cnt = 0 # 连续几次没找到目标 （可优化）

    times = 0 # 第几次进入战斗

    while not isEnd:

        if cnt >= 5: # 如果连续五次没有找到目标 检查是否已经结束 以后再完善
            check.finish()

        cnt += 1 # 计数器
        print("enter into main fuc, next will exe getPath")
        name, notFinish = getPath.getPath()

        if notFinish: # 如果有事件就重置计数器
            cnt = 0

        if name == 'battle' or name == 'warning' or name == 'elite': # 第一次进入战斗重新选人
            times += 1

        print("in main fuc, next will exe inEvent")

        inEvent.inEvnet(name, times) # 进入事件 并传入事件名字和次数


if __name__ == '__main__':
    t1 = threading.Thread(target=start_key_listener)
    t1.start()

    t2 = threading.Thread(target=test)
    t2.start()

    t1.join()
    t2.join()

    print("end")
