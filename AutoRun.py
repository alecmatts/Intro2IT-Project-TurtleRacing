import os
from turtle import *
from tkinter import *
from tkinter.ttk import Button
import sys
from winsound import *

os.system('TurtleRacing.py')    #Chạy game lần đầu

PlaySound('sound/Restart.wav', SND_ASYNC | SND_LOOP)

#Tạo một root Tk mới
root = Tk()
root.title('   T U R T L E    G A M E')
root.iconbitmap('background/icon.ico')

#Định nghĩa hàm quay lại khi nhấn Resume 
def playagain():
    sound = PlaySound('sound/button .wav', SND_ASYNC)
    root.withdraw()
    os.system('TurtleRacing.py')
    root.update()
    root.deiconify()
    PlaySound('sound/Restart.wav', SND_ASYNC | SND_LOOP)


#Định nghĩa hàm end: Tắt chương trình khi nhấn End Game
def end():
    sound = PlaySound('sound/button.wav', SND_ASYNC)
    root.destroy()
    sys.exit()

#Setting root
root.geometry('+0+0')   #Vị trí xuất hiện cửa sổ
img = PhotoImage(file='background/end_BG.gif')  #Ảnh nền
ground = Label(root, image=img) #Hiển thị ảnh
ground.pack()   #Cài widget vào Frame


Continue = PhotoImage(file='options and rewards/Return.gif')    #Hình ảnh nút Resume
Continuebutton = Button(root, image=Continue, command=playagain)    #Định nghĩa nút Resume
Continuebutton.place(x=1100, y=550) #Vị trí đặt nút Resume

Exit = PhotoImage(file='options and rewards/Exit.gif')  #Hình ảnh nút Exit
Exitbutton = Button(root, image=Exit, command=end)  #Định nghĩa nút Exit    
Exitbutton.place(x=1100, y=650)     #Vị trí đặt nút Exit

root.mainloop()
