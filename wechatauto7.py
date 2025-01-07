# 根据预定的csv数据自动回复
import numpy as np
import pandas as pd
from uiautomation import WindowControl

# 绑定微信主窗口
wx = WindowControl(Name='微信', searchDepth=1)  # searchDepth=1参数指定在查找窗口时只搜索直接子级窗口，以提高查找效率
# 切换窗口
wx.ListControl()
wx.SwitchToThisWindow()  # ListControl()方法用于列出所有子级窗口，而SwitchToThisWindow()方法则将焦点切换到微信主窗口
# 寻找会话控件绑定
hw = wx.ListControl(Name='会话')
# 通过pd读取数据
df = pd.read_csv('../response_data.txt', encoding='utf-8')
print(df)
while True:
    message_list = wx.ListControl(Name='消息').GetChildren()  # 获取消息列表中的所有子控件
    msg_num = len(message_list)
    if msg_num != 0:
        print(f"有{msg_num}条新消息：")
        last_msg = message_list[msg_num-1].Name  # 获取最新一条消息
        print(f"收到的消息{last_msg}")
        ##########
        # 判断关键字
        msg = df.apply(lambda x: x['value'] if str(x['key']) in last_msg else None, axis=1)
        # 返回的结果是一个包含处理结果的Series对象，msg和列表差不多
        print(f"匹配到的回复内容：{msg}")
        msg.dropna(axis=0, how='any', inplace=True)  # 这行代码移除回复内容中的空数据（NaN值）
        ar = np.array(msg).tolist()  # 这行代码将筛选后的回复内容转换为列表
        if (ar!= [])&(last_msg.find(ar[0]) < 0):
             nums = len(last_msg.split("."))  # 切割消息内容，获取接龙的序号
             print(f"nums = {nums}")
             sendMag = str(last_msg.replace('\n', '{Shift}{Enter}') + '{Shift}{Enter}' +str(nums) + ". " + ar[0]).replace('{br}', '{Shift}{Enter}')
             print(f"{sendMag}")
             wx.SendKeys(sendMag, waitTime=0)
           # 发送消息，回车键
             wx.SendKeys('{Enter}', waitTime=3)
