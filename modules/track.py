from turtle import *
from tkinter import *
from winsound import *

PlaySound('sound/main.wav', SND_ASYNC | SND_LOOP)

#Định nghĩa hàm vẽ lane chạy
def draw_map(level):
    screen = Screen()   #Tạo con vẽ screen
    screen.bgpic('background/BG.gif')   #Gán background
    screen.screensize(1680, 1050)   #Chỉnh độ phân giải
    screen.setup(width=1.0, height=1.0)

    setY_map_line = 300
    speed(5)
    pencolor('white')
    penup()
    setpos(-100 * level - 200, setY_map_line)

    if level == 1:  #Level 1
        length_of_map = 20
        setX_map_line = 80
    elif level == 2:    #Level 2
        length_of_map = 40
        setX_map_line = 380
    else:   #Level 3
        length_of_map = 50
        setX_map_line = 480

    for draw_number in range(int(length_of_map / 2)):   #Đánh số
        write(draw_number, align='center', font=('Roboto', 12))
        forward(40)

    pensize(3)
    right(180)
    setY_map_line -= 20

    for i in range(5):  #Vẽ lane
        penup()
        setpos(setX_map_line, setY_map_line)
        pendown()
        forward(length_of_map * 20)
        setY_map_line -= 130

    draw_finish_line(setX_map_line, 280)    #Vẽ vạch kết thúc

    return (-100 * level - 200, length_of_map * 20 - 20)

#Định nghĩa hàm vẽ vạch kết thúc
def draw_finish_line(posX, posY):
    penup()
    setpos(posX, posY)
    left(90)
    pensize(5)
    pendown()
    forward(520)
    penup()
    forward(200)



			