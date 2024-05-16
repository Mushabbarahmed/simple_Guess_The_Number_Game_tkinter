from tkinter import *
import tkinter.messagebox as t12
from PIL import Image, ImageTk
# import tkinter as tk
# import sys
# import os
from pygame import mixer
from tkinter import Tk, Label, Button, Entry
# import winsound


def main2():
    root = Tk()
    root.geometry("500x500")
    img12 = Image.open("game.png")
    # re = img12.resize((500, 500), Image.ANTIALIAS)
    re = img12.resize((500, 500))
    photo12 = ImageTk.PhotoImage(re)
    pic12 = Label(root, image=photo12)
    pic12.place(x=0, y=0)
    win = StringVar()
    win.set("you are correct")
    label = Label(root, textvariable=win, font="comicsansms 42 bold", fg="white", bg="black")
    label.place(x=50, y=220)
    mixer.music.stop()
    mixer.init()
    mixer.music.load("gw.mp3")
    mixer.music.play(-1)
    def restart_app():
        root.destroy()
        main()
    ab = Button(root, text="Restart", font=" comicsansms 22 bold ", fg="white", bg="black",
                command=restart_app)
    ab.place(x=200, y=400)
    ab.bind("<Control-r>", restart_app)
    root.mainloop()
def fun():
    message = t12.showinfo("game rules", "*guess any number the player who guesses correct wins *you have 5 chances")
def main1():
    root = Tk()
    def t():
        root.destroy()
        main()
    root.title("GUESS THE NUMBER")
    image1 = Image.open("clock2.png")
    photo1 = ImageTk.PhotoImage(image1)
    root.wm_iconphoto(False, photo1)
    # mes = t12.showinfo("game rules", "*guess any number the player who guesses correct wins you have 5 chances")
    root.geometry("500x500")
    img = Image.open("game1.png")
    # re = img.resize((500, 500), Image.ANTIALIAS)
    re = img.resize((500, 500))
    photo = ImageTk.PhotoImage(re)
    pic = Label(root, image=photo)
    pic.place(x=0, y=0)
    Label(text="game over", font="comicsansms 72 bold", fg="white", bg="black").pack()
    b1 = Button(text="Try again", font="comicsansms 18 bold", fg="white", bg="black", command=t)
    b1.place(x=200, y=200)
    mixer.music.stop()
    mixer.init()
    mixer.music.load("lose.wave")
    mixer.music.play(-1)
    root.mainloop()
def main():
    root=Tk()
   # global pho
    def su():
        mixer.music.play(-1)
        picture = Button(root, image=pho, command=mute)
        picture.place(x=450, y=10)
    def mute():

        mixer.music.stop()

        picture1 = Button(root,image=pho1,pady=4,padx=5,command=su)
        picture1.place(x=450,y=10)




    mixer.init()
    mixer.music.load("game.mp3")
    mixer.music.play(-1)
    root.title("GUESS THE NUMBER")
    image1 = Image.open("clock2.png")
    photo1 = ImageTk.PhotoImage(image1)
    root.wm_iconphoto(False, photo1)
    # mes = t12.showinfo("game rules", "*guess any number the player who guesses correct wins you have 5 chances")
    root.geometry("500x500")
    img = Image.open("game1.png")
    # re = img.resize((500, 500), Image.ANTIALIAS)
    re = img.resize((500, 500))
    photo = ImageTk.PhotoImage(re)
    pic = Label(root, image=photo)
    pic.place(x=0, y=0)
    menus1 = Menu(root)  # first u have to give menu variable in which ever u want to pack now packing here is root
    menus1.add_command(label="help", command=fun)  # to add the label menu
    root.config(menu=menus1)
    def start():
        a = i.get()
        a2 = a11.get()
        if (int(a2) < 9):
            win = StringVar()
            win.set("try increasing your number")
            label = Label(root, textvariable=win, font="comicsansms 28 bold", fg="white", bg="black")
            label.place(x=12, y=220)
        else:
            win = StringVar()
            win.set("  try  decreasing your number ")
            label = Label(root, textvariable=win, font="comicsansms 26 bold", fg="white", bg="black")
            label.place(x=10, y=220)
        if int(a2) == 9:
            root.destroy()
            main2()
        if int(i.get()) == 4:
            if int(a2)==9:
                root.destroy()
                main2()
            elif int(i.get())==4:
                root.destroy()
                main1()
        i.set(i.get() + 1)
    f2=Frame(root)
    f1 = Frame(root, bg="black")
    f1.place(x=180, y=120)
    f2.place(x=450,y=10)
    sound = Image.open("sound1.png")
    # re12 = sound.resize((25, 25), Image.ANTIALIAS)
    re12 = sound.resize((25, 25))
    pho = ImageTk.PhotoImage(re12)
    global pho1
    picture = Button(root, image=pho, command=mute)
    picture.place(x=450, y=10)
    sound2 = Image.open("sound2.png")
    # re123 = sound2.resize((25, 25), Image.ANTIALIAS)
    re123 = sound2.resize((25, 25))
    pho1 = ImageTk.PhotoImage(re123)

    a = Label(f1, text="GUESS THE NUMBER",font="comicsansms 12 bold", fg="white", bg="black")
    a.pack()
    i = IntVar()#i=chances numbers
    i.set(1)
    a1 = Label(root, textvariable=i, font="comicsansms 62 bold", fg="white", bg="black")
    a1.place(x=240, y=10)
    value1 = IntVar()
    a11 = Entry(f1, textvariable=value1)#a11=entry box
    a11.pack()
    Button(f1, text="start",font="comicsansms 22 bold", fg="black", bg="grey", command=start).pack()
    def restart_app(event=None):
        root.destroy()
        main()
    ab=Button(root, text="Restart",font="comicsansms 22 bold", fg="white", bg="black", command=restart_app)
    ab.place(x=200,y=400)
    ab.bind("<Control-r>", restart_app)
    root.mainloop()
if __name__ == '__main__':
    main()





