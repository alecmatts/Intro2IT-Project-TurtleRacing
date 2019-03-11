from turtle import *
from tkinter import *
from modules import menu, options, track, turtles, racing, ranking
from time import sleep
import sys

#Định nghĩa hàm chạy game
def define():
    start = menu.TakeChoose()
    return start


if define() == 1:
    (option, character) = options.TakeOption()  #Lấy số liệu level và nhân vật

    if option != 0 and character != 0:
        (scratch, length) = track.draw_map(option)  #Vẽ đường chạy

        (add, color, char) = turtles.addTurtles(character, scratch)     #Tạo nhân vật
        sleep(1)

        (rank, time) = racing.run(add, length, scratch, color, char)    #Đua + Chiến thắng
        sleep(2)

        ranking = ranking.ranking(rank, time, color, add, char)     #Tổng sắp và bục xếp hạng
    else:
        exit()
else:
    sys.exit()

#123
