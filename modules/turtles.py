from turtle import *
from random import shuffle

#Định nghĩa hàm random thứ tự xuất hiện + lane chạy
def listshuffle(x):
    shuffle(x)
    return x

#Định nghĩa hàm tạo nhân vật
def addTurtles(char, sp):
    turtle = []     #Khởi tạo một list Rùa không có phần tử nào

    dir = {1: 'sheep', 2: 'horse', 3: 'rabbit', 4: 'camel', 5: 'whale'}  #Dùng dictionary định nghĩa các lựa chọn
    Op = dir[char]  
    dir.clear()     #Xóa dict

    c = ['red', 'yellow', 'green', 'blue']   #Tạo list các màu hiển thị trong game (Gán cứng)
    p = [220, 90, 90 - 130, 90 - 130 * 2]   #Tạo list tung độ các lane a.k.a lane chạy

    c = listshuffle(c)  #Random màu
    p = listshuffle(p)  #Random lane chạy

    for i in range(4):  #Vòng lặp tạo Rùa
        tur = Turtle()

        tur.color(c[i])
        shape = 'characters/' + c[i] + Op + '.gif'
        addshape(shape)
        tur.shape(shape)

        tur.penup()
        tur.goto(sp - 20, p[i])
        tur.pensize(7)
        tur.pendown()

        tur.left(90)
        tur.forward(10)
        tur.left(180)
        tur.forward(20)
        tur.left(180)
        tur.forward(10)
        tur.right(90)
        tur.penup()

        tur.speed(1)
        
        turtle.append(tur)  #Append rùa vừa tạo vào list

    return (turtle, c, Op)



			