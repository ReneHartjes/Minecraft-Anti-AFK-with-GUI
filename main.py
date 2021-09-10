from tkinter import *

window = Tk()
window.title("SupercoolBotPickerino")
window.configure(bg="black" )
bg = PhotoImage(file='bg.png')
brt = PhotoImage(file="stpbtn.gif")
starta = PhotoImage(file="btn.gif")
#bg= Label(window, image=photo).place(x=0, y=0)

window.wm_maxsize(width=500, height=500,)



def clack():
    window.destroy()
    exit()

def click():

    import random
    import time
    import keyboard
    import pyautogui



    while True:

        rd = random.randint(4, 8)
        time.sleep(2)
        print(rd)
        if rd == 7:
            keyboard.press('w')
            time.sleep(0.2)
            keyboard.release('w')
            time.sleep(0.2)
            keyboard.press('s')
            time.sleep(0.2)
            keyboard.release('s')

            pyautogui.dragRel(100, 0, duration=0.2)
        if (keyboard.is_pressed('n')):
            break;




canvas1 = Canvas(window, width=500,
                 height=500)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Add Text
#canvas1.create_text(200, 250, text="Welcome")

# Create Buttons

Startbtn = Button(window, image=starta,command=click, borderwidth=0)
button2 = Button(window, image=brt,  command=clack,borderwidth=0)
label1 = Label(window,text="Hold n pressed ingame to interrupt pickerino", fg="White", bg="black")


# Display Buttons


#button2_canvas = canvas1.create_window(100, 40,
                                       #anchor="nw",
                                       #window=button2)

button3_canvas = canvas1.create_window(100, 30, anchor="nw",
                                       window=Startbtn)




button2_canvas = canvas1.create_window(300, 30, anchor="nw",
                                       window=button2)

window.mainloop()

