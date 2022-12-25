
from time import *
from tkinter import *
import time


class Ball:
    def __init__(self,canvas,x,y,d,xspeed,yspeed,hight,width,color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.d = d
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.hight = hight
        self.width = width
        self.color = color
        self.ball = canvas.create_oval(x,y,d,d,width=0,fill=color)

    def move(self):
        cord = self.canvas.coords(self.ball)
        if cord[2]> width or cord[0]<0:
            self.xspeed *=-1
        if cord[3]> hight or cord[1]<0:
            self.yspeed *=-1

        self.canvas.move(self.ball,self.xspeed,self.yspeed)

def update():
    c_time = strftime("%I:%M:%S %p")     #recressive function
    time_lable.config(text=c_time)

    time_lable.after(1000,update)


win =Tk()
win.geometry("500x400")
hight =275
width = 495
d = 50

time_lable = Label(win,font=("arial",60),fg="#00FF00",bd=10,border=5,bg="black")
time_lable.pack()
update()

canvas = Canvas(win,height=hight,width=width,bg="gray")
canvas.place(x=1,y=120)


circle1 = Ball(canvas,1,1,d,1,4,hight,width,"white")
circle2 = Ball(canvas,1,1,d,2,3,hight,width,"#00FF00")
circle3 = Ball(canvas,1,1,d,3,2,hight,width,"#FF00FF")
circle4 = Ball(canvas,1,1,d,4,1,hight,width,"#800000")

while True:
    circle1.move()
    circle2.move()
    circle3.move()
    circle4.move()

    win.update()
    time.sleep(0.01)





win.mainloop()


#----------------------------class-------------------------------


