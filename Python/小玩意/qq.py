import time
from pynput import mouse, keyboard
time.sleep(5)
m_mouse = mouse.Controller()                          #创建一个鼠标
m_keyboard = keyboard.Controller()                    #创建一个键盘
m_mouse.position = (505,329)                          #将鼠标移动到指定位置
m_mouse.click(mouse.Button.left)                      #点击鼠标左键
for i in range(10):                       #无限循环语句
	m_keyboard.type("天门山")       #输入要发的消息
	m_keyboard.press(keyboard.Key.enter)              #按下enter
	m_keyboard.release(keyboard.Key.enter)            #松开enter
	time.sleep(0.5)                                   #设置间隔时间(单位:秒)