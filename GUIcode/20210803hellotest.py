'''''
from tkinter import *

class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidge()
    def createWidge(self):
        self.helloLable = Label(self,text ='hello world!')
        self.helloLable.pack()
        self.quitButton = Button(self,text = 'Quit',command = self.quit())
        self.quitButton.pack()

app = Application()
app.master.title('t')
app.mainloop()
'''
'''''
from tkinter import *
import tkinter.messagebox as messagebox

class Appcation(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWindge()
    def createWindge(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text = 'Hello',command = self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, %s' % name)

app = Appcation()
app.master .title('Hello')
app.mainloop()
'''
from turtle import *

width(4)

forward(200)
right(90)

pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

done()