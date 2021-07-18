from tkinter import *
from tkinter import messagebox
import random
root=Tk() #creating the application main window
ans=["brazil","beijing","mexico","mumbai","tokyo","cairo","japan","france","singapore","iran","indonesia","italy","sweden","python","java","swift","canada","india","america","london","germany","delhi","bhutan","russia","australia"]
words=["bzairl","binegij","xcmoie","mmauib","tokoy","cioar","ajnpa","nfcar","isgnparoe","nrai","niodenisa","yltai","wdeesn","nptoyh","avja","wfsit","cdanaa","aidin","aiearcm","odnlon","graeynm","dlhei","buahtn","irsaus","asuaairlt"]
num=random.randrange(0,25,1)
def res():
    global num,words,ans
    num=random.randrange(0,25,1)
    lbl.config(text=words[num])
    e1.delete(0,END)
def display():
    global num,words,ans
    lbl.config(text=words[num])
def checkans():
    global num,words,ans
    var=e1.get()
    if var==ans[num]:
        messagebox.showinfo("Success","Congrats!!Correct answer") #display of success message
        res()
    else:
        messagebox.showerror("Error","Sorry!!Wrong answer") #display of error message
        e1.delete(0,END)
root.geometry("350x400+400+300")
root.title("Jumbled words") #adding title to window
lbl=Label(root,text="Your here",font="Timesnewroman") #adding label to window
lbl.pack(pady=30,ipady=10,ipadx=10)
v1=StringVar()
e1=Entry(root,font="Timesnewroman",textvariable=v1) #adding entry to window
e1.pack(ipady=5,ipadx=5)
b1=Button(root,text="Check",font="Timesnewroman",command=checkans,fg="Blue") #adding check button to window
b1.pack(pady=40)
b2=Button(root,text="Reset",font="Timesnewroman",command=res,fg="Red") #adding reset button to window
b2.pack()
display()
root.mainloop()
