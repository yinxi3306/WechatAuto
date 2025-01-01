# -*- coding:utf-8 -*-
import time
from pyautogui import *

from wxauto import *
from datetime import datetime

wx = WeChat()


def myTime():
    """
    该函数可以用于获取当前时间
    :return: string:当前时间
    """
    nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return nowTime


message = ""
nums = ""
num = 50


def go():
    hours = datetime.now().strftime("%H")
    minutes = datetime.now().strftime("%M")
    sumNumber = int(hours) * 60 + int(minutes)
    print(myTime(), "\t" f"hours={hours},minutes={minutes},sumNumber={sumNumber}")
    return int(sumNumber)


while True:
    sumNumber = go()
    if 465 <= int(sumNumber) <= 490:
        sumNumber = go()

        wx = WeChat()  # 获取微信对象

        wx.GetSessionList()  # 获取聊天列表

        wx.ChatWith("*******")  # 打开指定聊天,改这里

        msgs = wx.GetAllMessage  # 获取指定聊天框内当前显示的聊天记录
        print(f"{myTime()},get message succeed!")

        # 检测接龙
        for lastMessage in msgs[::-1]:
            if str(lastMessage).find("#接龙") >= 0:
                message = lastMessage[1]  # 循环抓取接龙消息
                print(f"{myTime()},get #接龙 message succeed,{message}")
                break

        # 如果出现名字则直接离开
        if message.find("名字") < 0:

            while True:  # 循环,获取接龙的序号
                if message.find(str(num) + ".") > 0:
                    print(f"{myTime()},num = {num}, Index = {num + 1}")
                    nums = num + 1
                    break
                else:
                    num -= 1

            wxauto.WxUtils.SetClipboard(message + f"\n{nums}. 2202名字")
            print(f"{myTime()},get Clipboard succeed")
            wx.SendClipboard()

            print(f"{myTime()},send succeed!")
            click(x=1049, y=63)

    time.sleep(300)