from turtle import *
from random import choice,randint
from time import time

def run(t, length, sp, color, char):
    rank = [0] * 4
    time_t = [0.0] * 4

#invent1
    UFO = Turtle()
    addshape("effect/UFO.gif")
    UFO.shape("effect/UFO.gif")
    UFO.ht()
    UFO.penup()
    UFO.left(180)
    Laser = Turtle()
    Laser.ht()
    Laser.left(180)
    stun = [0] * 4

#invent2
    blackgate = Turtle()
    addshape("effect/blackgate.gif")
    blackgate.shape("effect/blackgate.gif")
    blackgate.ht()
    
    s = [0] * 4
    
    count = 1
    now = time()

    while True:
        flag_dels = [0] * 4
        flag_delb = [0] * 4
        cstop = [0] * 4
        cback = [0] * 4
        step = [[-40, -30, 0, 40, 50, 60], 
                [-40, -30, 0, 40, 50, 60],
                [-40, -30, 0, 40, 50, 60], 
                [-40, -30, 0, 40, 50, 60]]
        
        for turn in range(10):
            for i in range(4):
                a, step[i], cstop[i], cback[i] = rand(t[i], step[i], cstop[i], flag_dels[i], cback[i], flag_delb[i])
                
                flag_dels[i], flag_delb[i] = check_step(step[i], flag_dels[i], flag_delb[i])
                
                event2(t, i, blackgate, sp, length, s, rank)
                
                if (event1(t, i, UFO, Laser, char, stun, color, rank, s, sp) == 0):
                    s[i] += a
                    
                    if (s[i]<0):   
                        t[i].setx(sp)
                        s[i]=0
                    elif (rank[i]!= 0):
                        continue
                    elif (s[i] < length):
                        if a < 0:
                            shape_re = 'characters/' + color[i] + char + '_re.gif'
                            addshape(shape_re)
                            t[i].shape(shape_re)   
                            t[i].forward(a)
                            shape = 'characters/' + color[i] + char + '.gif'
                            t[i].shape(shape)
                        elif a == 0:
                            for j in range(10):
                                t[i].ht()
                                t[i].st()
                        else:
                            t[i].forward(a)
                    else:
                        t[i].setx(sp+length)

                        if rank[i] == 0:
                            rank[i] = count
                            count += 1
                            time_t[i] = round(time()-now,2) 
                            t[i].penup()
                            t[i].circle(5)
                            break
                
        if count == 5:
            break

    for i in range(4):  #winning effect
        if rank[i] == 1:
            win = Turtle()
            win.ht()
            addshape('effect/effect.gif')
            win.shape('effect/effect.gif')
            win.penup()
            win.goto(sp + length + 200, t[i].ycor())
            win.st()
            
            t[i].speed(5)
            t[i].penup()
            t[i].forward(80)
            t[i].left(90)

            for j in range(5):
                t[i].forward(60)
                t[i].right(180)
                t[i].forward(60)
                t[i].right(180)

    return rank, time_t


def rand(t, step, cstop, flags, cback, flagb):
    dis = choice(step)

    if dis == 0:
        cstop += 1
    if dis == -30 or dis == -40:
        cback += 1

    if cstop == 2 and flags == 0:
        step.remove(0)
    if cback == 3 and flagb == 0:
        step.remove(-30)
        step.remove(-40)

    return dis, step, cstop, cback


def check_step(step,flags,flagb):
    if 0 in step:
        flags = 0
    else:
        flags = 1
                
    if (-40 and -30) in step:
        flagb = 0
    else:
        flagb = 1

    return flags, flagb


def event1(t,i,UFO,Laser,char,stun,color,rank, s, sp):
    if rank[i]!=0:
        return 0

    if (randint(0,80) == 0):
        UFO.goto(800,t[i].ycor())
        UFO.st()
        UFO.speed(1)
        UFO.forward(50)
        Laser.pensize(30)
        Laser.color("yellow")
        Laser.speed(10)
        Laser.penup()
        Laser.goto(UFO.xcor(),UFO.ycor())
        Laser.pendown()
        Laser.forward(2000)
        s[i]= s[i] - 70

        if s[i] <= 0:
            t[i].setx(sp)
            s[i] = 0
        else:
            t[i].backward(70)
            
        Laser.clear()
        UFO.backward(50)
        return 1
    else:
        return 0


def event2(t,i,blackgate,sp,length,s, rank):
    if rank[i]!=0:
        return 0

    if (randint(0,200) == 0):
        blackgate.penup()
        blackgate.st()
        blackgate.goto(t[i].xcor(),t[i].ycor())
        t[i].ht()
        blackgate.ht()
        blackgate.goto(randint(sp,sp+length),t[i].ycor())
        blackgate.st()
        t[i].goto(blackgate.xcor(),blackgate.ycor())
        t[i].st()
        s[i] = blackgate.xcor() - sp
        blackgate.ht()
        return 1
    else:
        return 0