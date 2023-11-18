from tkinter import *
pen_color = "black"
def paint(event) :
    global pen_color
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 5, y1+5
    canvas.create_line(x1, y1,x2, y2, width = 3, fill = pen_color)
def change_color() :
    global pen_color
    pen_color = color("red")
win= Tk()
w = 6
win.title("my paint")
win.geometry("500x500+200+200")
canvas = Canvas(win, bg= "white", width = 500, height = 470)
btn_white = Button(win,text = "white", bg = "white", width = w)
btn_black = Button(win,text = "black", bg = "black", width = w)
btn_blue = Button(win,text = "blue", bg = "blue", width = w)
btn_green = Button(win,text = "green", bg = "green", width = w)
btn_yellow = Button(win,text = "yellow", bg = "yellow", width = w)
btn_red = Button(win,text = "red", bg = "red", width = w)
btn_plus = Button(win,text = "+", bg = "white", width = w)
btn_minus = Button(win,text = "-", bg = "white", width = w)
btn_clear = Button(win,text = "clear", bg = "white", width = w)
canvas.grid(row =0, column = 0, columnspan = 9)
btn_white.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_yellow.grid(row = 1, column = 2)
btn_blue.grid(row = 1, column = 3)
btn_green.grid(row = 1, column = 4)
btn_red.grid(row = 1, column = 5)
btn_plus.grid(row = 1, column = 6)
btn_minus.grid(row = 1, column = 7)
btn_clear.grid(row = 1, column = 8)
win.bind("<B1-Motion>",paint)
win.mainloop()
