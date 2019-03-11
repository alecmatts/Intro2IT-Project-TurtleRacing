from tkinter.ttk import Frame, Button
from tkinter import *
import sys
from winsound import *

sound = PlaySound('sound/Turtle.wav', SND_ASYNC | SND_LOOP)

t = [0]
root = Tk()

root.title('   T U R T L E    G A M E')
root.iconbitmap('background/icon.ico')


def ExitApplication():
    if t[0] == 1:
        root.destroy()


def start():
    t[0] = 1
    sound = PlaySound('sound/button.wav', SND_ASYNC)
    ExitApplication()


def end():
    t[0] = 0
    sound = PlaySound('sound/button.wav', SND_ASYNC)
    sys.exit()


root.geometry('+100+10')
img = PhotoImage(file='background/black2.gif')
ground = Label(root, image=img)
ground.pack()

play = PhotoImage(file='options and rewards/Start.gif')
playbutton = Button(root, image=play, command=start)
playbutton.place(x=900, y=530)

Exit = PhotoImage(file='options and rewards/Exit.gif')
Exitbutton = Button(root, image=Exit, command=end)
Exitbutton.place(x=900, y=630)
root.mainloop()


def TakeChoose():
    return t[0]