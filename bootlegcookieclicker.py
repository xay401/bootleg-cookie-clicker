from tkinter import *

#widgets = GUI elemnets : buttons, textboxes, labels,images
#windows = serves as a container to hold or contain these widgets



window = Tk() #instantiate an instance of a window
window.geometry("420x420") #change size of window
window.title("cookie clicker")
window.config(background="white")


count = 0


label = Label(window,text=count)
label.pack()
label.config(font=("Monospace",50))




def click():
    global  count
    count +=1 #makes it count by one
    label.config(text=count)

button = Button(window,text="Click me!!!")
button.config(command=click) #performs callback of function
button.config(font=("Ink free",50,"bold"))
button.config(bg="white") #changes background color
button.config(fg="black")  #changes forground color
button.config(activebackground="black") #when hovering over button it turns white
button.config(activeforeground= "white")
image = PhotoImage(file="cookie.png")
button.config(image=image)
button.config(compound='bottom') #Makes both buttons appear in window
#button.config(state=DISABLED) #disables button
button.pack()






#icon = PhotoImage(file="/home/xay/Documents/February8th2025/guiproject/pythonlogo.png")
#window.iconphoto(True,icon)


window.mainloop() #place window on display, listen for events




