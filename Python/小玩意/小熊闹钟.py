import datetime
import turtle

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

# 绘制闹钟背景
# 耳朵
turtle.color(248/256, 232/256, 121/256)
r = 80
turtle.penup()
turtle.goto(-r*2, r*0.7)
turtle.pendown()
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.penup()
turtle.goto(r*2, r*0.7)
turtle.pendown()
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
# 闹钟外框
turtle.color(209/256, 138/256, 58/256)
r = 170
turtle.penup()
turtle.goto(-r*0.3, -r)
turtle.pendown()
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.begin_fill()
for i in range(2):
    turtle.forward(r*0.6)
    turtle.left(90)
    turtle.forward(r*2)
    turtle.left(90)
turtle.end_fill()
turtle.forward(r*0.6)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

# 闹钟黑框
turtle.color("black")
r = 160
turtle.penup()
turtle.goto(-r*0.3, -r)
turtle.pendown()
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
turtle.begin_fill()
for i in range(2):
    turtle.forward(r*0.6)
    turtle.left(90)
    turtle.forward(r*2)
    turtle.left(90)
turtle.end_fill()
turtle.forward(r*0.6)
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()

temp_date = ""
while True:
    # 获取当前系统时间
    date = str(datetime.datetime.now())
    # print(date)
    date = date.split(' ')[-1]
    date = date.split('.')[0]
    if date == temp_date:
        continue
    else:
        temp_date = date
    hh, mm, ss = map(int, date.split(':'))

    # 初始化
    turtle.seth(0)
    # 闹钟背景
    turtle.color(201/256, 119/256, 59/256)
    r = 150
    turtle.penup()
    turtle.goto(-r*0.3, -r)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(r*0.6)
        turtle.left(90)
        turtle.forward(r*2)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(r*0.6)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

    # 脸
    # 左眼
    turtle.penup()
    turtle.goto(-r*0.7, r*0.2)
    turtle.pendown()
    turtle.dot(60, "black")
    turtle.penup()
    turtle.goto(r*0.7, r*0.2)
    turtle.pendown()
    turtle.dot(60, "black")
    # 白色脸颊
    turtle.color("white")
    r = 60
    turtle.penup()
    turtle.goto(-r*0.3, -r*1.4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(r*0.6)
        turtle.left(90)
        turtle.forward(r*2)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(r*0.6)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    # 鼻子
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.dot(40, "black")
    # 嘴巴
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(15)
    turtle.seth(90)
    turtle.circle(50, -80)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pensize(15)
    turtle.seth(270)
    turtle.circle(50, 80)

    # 十二圆点
    dis_list = [180, 170, 155, 140, 155, 170, 180, 170, 155, 140, 155, 170]
    for i in range(12):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.seth(i*30)
        turtle.penup()
        turtle.forward(dis_list[i])
        turtle.pendown()
        turtle.dot(10, "yellow")

    # 时针
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.seth(90)
    turtle.right((hh+mm/60+ss/3600)/12*360)
    turtle.pencolor(114/256, 92/256, 78/256)
    turtle.pensize(10)
    turtle.forward(80)
    # 分针
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.seth(90)
    turtle.right((mm+ss/60)/60*360)
    turtle.pencolor(171/256, 150/256, 133/256)
    turtle.pensize(8)
    turtle.forward(110)
    # 秒针
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.seth(90)
    turtle.right(ss/60*360)
    turtle.pencolor(177/256, 167/256, 165/256)
    turtle.pensize(5)
    turtle.forward(140)
    # 中点
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.dot(40, "black")

    # 刷新
    turtle.update()
