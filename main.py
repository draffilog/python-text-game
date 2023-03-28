import tkinter
import random

main_window = tkinter.Tk()
main_window.title("Text-based adventure game")
main_window.geometry("400x400")
name = input("Enter your name please >> ")
money = random.randint(50,310)
point = 0
health = 100
top_frame = tkinter.Frame(main_window)
top_frame.pack(anchor = "n")

name_label = tkinter.Label(top_frame, text ="Name: "+ name, font = ("Calibri, 16"))
name_label.grid(row = 0, column = 0)
health_label = tkinter.Label(top_frame, text = "Health: "+str(health), font = ("Calibri, 16"))
health_label.grid(row = 1, column = 0)
money_label = tkinter.Label(top_frame, text = "Money: "+str(money), font = ("Calibri, 16"))
money_label.grid(row = 0, column = 1)
point_label = tkinter.Label(top_frame, text = "Point: "+str(point), font = ("Calibri, 16"))
point_label.grid(row = 1, column = 1)

def change_labels(money, health, point):
    money_label.configure(text = "Money: "+str(money))
    health_label.configure(text = "Health: "+str(health))
    point_label.configure(text = "Point: "+str(point))


bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor = "s")

def Room1():
    print("Hello, you are in room 1")
    point = 10
    change_labels(money, health, point)
    pass
def Room2():
    pass
def Room3():
    pass
def Room4():
    pass
def Shop():
    pass
def Inventory():
    pass

R1_btn = tkinter.Button(bottom_frame, text="Room 1", command = Room1)
R1_btn.grid(row=0, column=0)
R2_btn = tkinter.Button(bottom_frame, text="Room 2", command = Room2)
R2_btn.grid(row=0, column=1)
R3_btn = tkinter.Button(bottom_frame, text="Room 3", command = Room3)
R3_btn.grid(row=1, column=0)
R4_btn = tkinter.Button(bottom_frame, text="Room 4", command = Room4)
R4_btn.grid(row=1, column=1)
In_btn = tkinter.Button(bottom_frame, text = "Inventory", command = Inventory)
In_btn.grid(row=0, column=2)
Sh_btn = tkinter.Button(bottom_frame, text="Shop", command = Shop)
Sh_btn.grid(row=1, column=2)


main_window.mainloop()