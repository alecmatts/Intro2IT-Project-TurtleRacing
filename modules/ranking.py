from turtle import *
from winsound import *

#Định nghĩa hàm xếp hạng
def ranking(rank, time, c, t, char):
    clearscreen()   #clear màn hình trước đó

    screen = Screen()   #Set lại background
    screen.bgpic("background/rank_BG.gif")
    
    #Tạo lại 4 con rùa
    t[3] = Turtle()
    t[2] = Turtle()
    t[1] = Turtle()
    t[0] = Turtle()

    #Scoreboard Title
    Title = Turtle()
    Title.ht()
    addshape('background/ScoreBoard.gif')
    Title.shape('background/ScoreBoard.gif')
    Title.penup()
    Title.goto(375, 310)
    Title.st()
    
    #Vẽ bảng tổng sắp
    speed(5)
    hideturtle()
    pensize(5)
    pencolor('white')
    penup()
    goto(200, 250)
    pendown()
    forward(360)
    right(90)
    forward(450)
    right(90)
    forward(60)
    right(90)
    penup()
    forward(60)

    for i in range(3,-1,-1):
        write(rank[i],font=("Arial", 10, "bold"))
        forward(90)
    backward(10)
    write("RANK",font=("Arial", 12, "bold"),align="center")
    right(180)
    forward(410)
    pendown()
    right(90)
    forward(60)
    right(90)
    forward(450)
    right(180)
    forward(450)
    right(90)
    forward(60)
    right(90)
    penup()
    forward(60)

    for i in range(3,-1,-1):
        write(time[i],font=("Arial", 10, "bold"),align="center")
        forward(90)

    backward(10)
    write("TIME",font=("Arial", 12, "bold"),align="center")
    right(180)
    forward(410)
    pendown()
    right(90)
    forward(60)
    right(90)
    forward(450)
    right(180)
    forward(450)
    right(90)
    forward(60)
    right(90)
    penup()

    for i in range(3,-1,-1):
        y = 250 - 20 - 90*(i+1)
        t[i].color(c[i])
        shape = 'characters/' + c[i] + char + '.gif'
        t[i].shape(shape)
        t[i].penup()
        t[i].goto(200 + 60, y)

    forward(410)
    write("NAME",font=("Arial", 12, "bold"),align="center")
    right(180)
    forward(410)
    pendown()
    right(90)
    forward(60)
    right(90)
    forward(450)

    inPodium(t, rank)   #Bục xếp hạng

    penup()
    goto(-550,350)
    write("Click on Screen to Exit...",font=("Arial", 20, "bold"),align="center")
    exitonclick()
    
#Định nghĩa bục xếp hạng
def inPodium(t, rank):
    penup()
    pensize(5)
    goto(-590, -320)
    pendown()

    #podium no.3
    forward(200 - 30 * 3)
    right(90)
    forward(190)
    right(90)
    forward(200 - 30 * 3)

    right(180)

    #podium no.1
    forward(200 - 30 * -3)
    right(90)
    forward(190)
    right(90)
    forward(200 - 30 * -3)

    right(180)

    #podium no.2
    forward(200 - 30 * 0)
    right(90)
    forward(190)
    right(90)
    forward(200 - 30 * 0)

    #insertRank
    penup()
    goto(-495, -310)
    write("3",font=("Arial", 50, "bold"),align="center")

    goto(-305, -140)
    write("1",font=("Arial", 55, "bold"),align="center")

    goto(-115, -230)
    write("2",font=("Arial", 50, "bold"),align="center")
    ht()

    #insertTurtle
    for i in range(4): #3rd
        if rank[i] == 3:
            t[i].goto(-495, -160)
            break

    for i in range(4):  #2nd
        if rank[i] == 2:
            t[i].goto(-115, -70)
            break

    for i in range(4):  #1st
        if rank[i] == 1:
            t[i].goto(-305, 20)
            break

            
    for i in range(4):
        if rank[i] == 4:
            t[i].goto(75, -290)
            break

    #insert Cup
    cup3 = Turtle() #3
    addshape('options and rewards/3rd.gif')
    cup3.shape('options and rewards/3rd.gif')
    cup3.penup()
    cup3.goto(-495, -80)

    cup2 = Turtle() #2
    addshape('options and rewards/2nd.gif')
    cup2.shape('options and rewards/2nd.gif')
    cup2.penup()
    cup2.goto(-115, 0)

    cup1 = Turtle() #1
    addshape('options and rewards/1st.gif')
    cup1.shape('options and rewards/1st.gif')
    cup1.penup()
    cup1.goto(-305, 110)
