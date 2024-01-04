from wxauto import WeChat
wx = WeChat()
wx.GetSessionList()
who = "方鹏程"
wx.ChatWith(who)
for i in range(1):
    wx.SendMsg('1')
    # wx.SendMsg("")
    # wx.SendMsg("")


# with open(r"D:\\VScode\\Workplace\\3.txt", "r",encoding="utf-8") as f:
#     for line in f.readlines():
#         who = "方鹏程"
#         wx.ChatWith(who)
#         for i in range(200):
#             wx.SendMsg(line)
