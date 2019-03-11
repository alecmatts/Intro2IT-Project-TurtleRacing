from tkinter.ttk import Frame, Button
from tkinter import *
import tkinter.messagebox as mbox
import sys
from winsound import *

t = [0]
c = [0]
root = Tk()

root.title('   T U R T L E    G A M E')
root.iconbitmap('background/icon.ico')

PlaySound('sound/option.wav', SND_ASYNC | SND_LOOP)


def ExitApplication():
    if t[0] != 0 and c[0] != 0:
        sound = PlaySound('sound/button.wav', SND_ASYNC)
        root.destroy()


def onSmall():
    t[0] = 1
    ExitApplication()


def onMedium():
    t[0] = 2
    ExitApplication()


def onLarge():
    t[0] = 3
    ExitApplication()


def on1():
    c[0] = 1
    ExitApplication()


def on2():
    c[0] = 2
    ExitApplication()


def on3():
    c[0] = 3
    ExitApplication()


def on4():
    c[0] = 4
    ExitApplication()

def on5():
    c[0] = 5
    ExitApplication()


root.geometry('+50+0')
img = PhotoImage(file='background/PickWall.gif')
ground = Label(root, image=img)
ground.pack()

img1 = PhotoImage(file='characters/avatar/sheep.gif')
choose1 = Button(root, image=img1, command=on1)
choose1.place(x=100, y=400)
img2 = PhotoImage(file='characters/avatar/horse.gif')
choose2 = Button(root, image=img2, command=on2)
choose2.place(x=300, y=400)
img3 = PhotoImage(file='characters/avatar/rabbit.gif')
choose3 = Button(root, image=img3, command=on3)
choose3.place(x=100, y=550)
img4 = PhotoImage(file='characters/avatar/camel.gif')
choose4 = Button(root, image=img4, command=on4)
choose4.place(x=300, y=550)
img5 = PhotoImage(file='characters/avatar/whale.gif')
choose5 = Button(root, image=img5, command=on5)
choose5.place(x=200, y=700)

img6 = PhotoImage(file='options and rewards/Level1.gif')
choose6 = Button(root, image=img6, command=onSmall)
choose6.place(x=1150, y=250)
img7 = PhotoImage(file='options and rewards/Level2.gif')
choose7 = Button(root, image=img7, command=onMedium)
choose7.place(x=1150, y=450)
img8 = PhotoImage(file='options and rewards/Level3.gif')
choose8 = Button(root, image=img8, command=onLarge)
choose8.place(x=1150, y=650)

root.mainloop()


def TakeOption():
    return (t[0], c[0])

#test aloalo