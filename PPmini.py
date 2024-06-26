import time
from tkinter import *
from tkinter import END
from tkinter import Toplevel
from tkinter import PhotoImage
from tkinter import Canvas
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import ttk,messagebox
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil
from tkinter import Tk, Label, Button, StringVar,Frame,Entry

# brightness
import screen_brightness_control as pct

# audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# WEBSITE(TKINTER)
import webview 

# clock
from time import strftime

# calendar
from tkcalendar import *

# open google
import pyautogui

import subprocess
import webbrowser as wb
import random

root=Tk()
root.title('mac-soft Tool')
# root.geometry("850x500+300+170")
root.geometry("1500x900+200+100")
root.resizable(False,False)
root.configure(bg='#292e2e')

# icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

Body=Frame(root,width=1500,height=900,bg="#d6d6d6")
Body.pack(pady=20,padx=20)

# ----------------------------
LHS=Frame(Body,width=600,height=835,bg="#f4f5f5",highlightbackground="#abacb1",highlightthickness=1)
LHS.place(x=10,y=10)

# logo
photo=PhotoImage(file="Image/laptop_lg.png")
myimage=Label(LHS,image=photo,background="#f4f5f5")
myimage.place(x=0,y=20)

my_system= platform.uname()

l1=Label(LHS, text=my_system.node, bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l1.place(x=20,y=360)

l2=Label(LHS, text=f"Version:{my_system.version}", bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l2.place(x=20,y=415)

l3=Label(LHS, text=f"System:{my_system.system}", bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l3.place(x=20,y=470)

l4=Label(LHS, text=f"Machine:{my_system.machine}", bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l4.place(x=20,y=525)

l5=Label(LHS, text=f"RAM:{round(psutil.virtual_memory().total/1000000000,2)} GB", bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l5.place(x=20,y=580)

full_processor_name = platform.processor()
l6=Label(LHS, text=f"Processor:{my_system.processor}", bg="#f4f5f5",font=("Acumin Variable Concept",10,"bold"),justify="center")
l6.pack()
l6.place(x=20,y=635)


# -----------------------------
RHS=Frame(Body,width=829,height=412,bg="#f4f5f5",highlightbackground="#abacb1",highlightthickness=1)
RHS.place(x=620,y=10)

system=Label(RHS, text='System:',font=("Acumin Varaible Concept",15),bg="#f4f5f5")
system.place(x=20,y=15)


################## BATTERY ####################


def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"% (hours,minutes,seconds)

battery_label = None
def none():
    global battery_png
    global battery_label
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=convertTime(battery.secsleft)

    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f'Plug in:{str(battery.power_plugged)}')
    lbl_time.config(text=f'{time} remaining')

    if not battery_label:
        battery_label=Label(RHS,background="#f4f5f5")
        battery_label.place(x=15,y=80)

    battery_label.config(text='')

    lbl.after(1000,none)

    if battery.power_plugged==True:
        battery_png=PhotoImage(file="Image/charging.png")
        battery_label.config(image=battery_png)
    else:
        battery_png=PhotoImage(file="Image/battery.png")
        battery_label.config(image=battery_png)


lbl=Label(RHS,font=("Acumin Variable Concept",24,'bold'),bg="#f4f5f5")
lbl.place(x=400,y=65)

lbl_plug=Label(RHS,font=("Acumin Variable Concept",11),bg="#f4f5f5")
lbl_plug.place(x=15,y=200)

lbl_time=Label(RHS,font=("Acumin Variable Concept",15),bg="#f4f5f5")
lbl_time.place(x=400,y=170)

none()

#####################################################

#################### SPEAKER ########################

lbl_speaker=Label(RHS,text="Speaker:",font=('arial',15,'bold'),bg="#f4f5f5")
lbl_speaker.place(x=15,y=250)
volume_value=tk.DoubleVar()

def get_current_volume_value():
    return '{: .2f}'.format(volume_value.get())

def volume_changed(event):
    try:
        device = AudioUtilities.GetSpeakers()
        interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume_level = -float(get_current_volume_value())
        volume.SetMasterVolumeLevel(volume_level, None)
    except Exception as e:
        print("An error occurred while setting the master volume level:", e)


style= ttk.Style()
style.configure("TScale",background='#f4f5f5', thickness=30)


volume=ttk.Scale(RHS, from_=100,to=0,orient='horizontal',command=volume_changed,variable=volume_value, length =400,style="TScale.Horizontal.TScale")
volume.place(x=245,y=265)
volume.set(20)


########################################################

##################### BRIGHTNESS #######################


lbl_brightness=Label(RHS,text='Brightness:',font=('arial',15,'bold'),bg='#f4f5f5')
lbl_brightness.place(x=15,y=320)

current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def brightness_changed(event):
    pct.set_brightness(get_current_value())

brightness= ttk.Scale(RHS,from_=0,to=100,orient='horizontal',command=brightness_changed,variable=current_value,length =400,style="TScale.Horizontal.TScale")
brightness.place(x=245,y=335)
brightness.set(70)



#########################################################



def calculator():
    # f1=Frame(root)
    root = Tk()
    root.title("Simple Calculator")
    root.geometry("600x835")
    root.configure(bg="#C5EBAA")
    

    e = Entry(root, width=43, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=15, pady=15, sticky="nsew")

    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)

    def button_add():
        first_number = e.get()
        global f_num
        global math_operation
        math_operation = "addition"
        f_num = int(first_number)
        e.delete(0, END)

    def button_subtract():
        first_number = e.get()
        global f_num
        global math_operation
        math_operation = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)

    def button_multiply():
        first_number = e.get()
        global f_num
        global math_operation
        math_operation = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)

    def button_divide():
        first_number = e.get()
        global f_num
        global math_operation
        math_operation = "division"
        f_num = int(first_number)
        e.delete(0, END)

    def button_equal():
        second_number = e.get()
        e.delete(0, END)

        if math_operation == "addition":
            e.insert(0, f_num + int(second_number))
        elif math_operation == "subtraction":
            e.insert(0, f_num - int(second_number))
        elif math_operation == "multiplication":
            e.insert(0, f_num * int(second_number))
        elif math_operation == "division":
            e.insert(0, f_num / int(second_number))
    def on_back():
        root.deiconify()  # Show the main window
        calculator_window.withdraw()
    
    # Define Buttons

    button_1 = Button(root, text="1", padx=55, pady=30, command=lambda: button_click(1), bg="#344955", fg="white")
    button_2 = Button(root, text="2", padx=55, pady=30, command=lambda: button_click(2), bg="#344955", fg="white")
    button_3 = Button(root, text="3", padx=55, pady=30, command=lambda: button_click(3), bg="#344955", fg="white")
    button_4 = Button(root, text="4", padx=55, pady=30, command=lambda: button_click(4), bg="#344955", fg="white")
    button_5 = Button(root, text="5", padx=55, pady=30, command=lambda: button_click(5), bg="#344955", fg="white")
    button_6 = Button(root, text="6", padx=55, pady=30, command=lambda: button_click(6), bg="#344955", fg="white")
    button_7 = Button(root, text="7", padx=55, pady=30, command=lambda: button_click(7), bg="#344955", fg="white")
    button_8 = Button(root, text="8", padx=55, pady=30, command=lambda: button_click(8), bg="#344955", fg="white")
    button_9 = Button(root, text="9", padx=55, pady=30, command=lambda: button_click(9), bg="#344955", fg="white")
    button_0 = Button(root, text="0", padx=55, pady=30, command=lambda: button_click(0), bg="#344955", fg="white")

    button_add = Button(root, text="+", padx=53, pady=30, command=button_add, bg="#1B3C73", fg="white")
    button_subtract = Button(root, text="-", padx=54, pady=30, command=button_subtract, bg="#1B3C73", fg="white")
    button_multiply = Button(root, text="*", padx=54, pady=30, command=button_multiply, bg="#1B3C73", fg="white")
    button_divide = Button(root, text="/", padx=56, pady=30, command=button_divide, bg="#1B3C73", fg="white")

    button_equal = Button(root, text="=", padx=154, pady=30, command=button_equal, bg="#070F2B", fg="white")
    button_clear = Button(root, text="Clear", padx=133, pady=30, command=button_clear, bg="#070F2B", fg="white")

    button_back = Button(root, text="Back", command=on_back, bg="#344955", fg="white")
    button_back.grid(row=7, column=0, columnspan=3, pady=10)

    # Put button on screen

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)

    button_add.grid(row=5, column=0)
    button_subtract.grid(row=5, column=1)
    button_multiply.grid(row=5, column=2)

    button_divide.grid(row=6, column=0)
    button_clear.grid(row=6, column=1, columnspan=2)
    button_equal.grid(row=4, column=1, columnspan=2)

    

    calculator_window = root

    root.mainloop()



def clock():
    def clock_c():
        text = strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000, clock_c)

    def on_back():
        root.deiconify()  # Show the main window
        clock_window.withdraw()  # Hide the clock window

    app2 = Toplevel()
    app2.geometry("829x412")
    app2.title('Clock')
    app2.configure(bg='#292e2e')
    app2.resizable(False, False)

    # icon
    image_icon = PhotoImage(file="Image/App2.png")
    app2.iconphoto(False, image_icon)

    clock_frame = Label(app2, bg="#292e2e")
    clock_frame.pack(expand=True)

    lbl = Label(clock_frame, font=('digital-7', 50, 'bold'), width=20, bg="#f4f5f5", fg="#292e2e")
    lbl.pack(pady=20)

    clock_c()

    button_back = Button(clock_frame, text="Back", command=on_back, bg="#FFE6E6", fg="black")
    button_back.pack(pady=10)

    clock_window = app2  # Assigning the app2 window to the clock window for clarity

    app2.mainloop()


def calendar():
    def on_back():
        root.deiconify()  # Show the main window
        calendar_window.withdraw()  # Hide the calendar window

    app3 = Toplevel()
    app3.geometry("829x412")
    app3.title('Calendar')
    app3.configure(bg="#292e2e")
    app3.resizable(False,False)

    # icon
    image_icon=PhotoImage(file="Image/App3.png")
    app3.iconphoto(False,image_icon)

    mycal=Calendar(app3,setmode='day',date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)

    button_back = Button(app3, text="Back", command=on_back, bg="#344955", fg="white")
    button_back.pack(pady=10)

    calendar_window = app3  # Assigning the app3 window to the calendar window for clarity

    app3.mainloop()

############################## MODE #######################

button_mode=True

def mode():
    global button_mode
    if button_mode:
        # Change LHS frame configuration
        LHS.config(bg="#292e2e")
        myimage.config(bg="#292e2e")
        l1.config(bg="#292e2e", fg="#d6d6d6")
        l2.config(bg="#292e2e", fg="#d6d6d6")
        l3.config(bg="#292e2e", fg="#d6d6d6")
        l4.config(bg="#292e2e", fg="#d6d6d6")
        l5.config(bg="#292e2e", fg="#d6d6d6")
        l6.config(bg="#292e2e", fg="#d6d6d6")

        # Change RHS frame configuration
        RHS.config(bg="#292e2e")
        # Change the background color of labels in the RHS frame
        lbl_speaker.config(bg="#292e2e", fg="#d6d6d6")
        lbl_brightness.config(bg="#292e2e", fg="#d6d6d6")
        lbl_plug.config(bg="#292e2e", fg="#d6d6d6")
        system.config(bg="#292e2e", fg="#d6d6d6")
        lbl_time.config(bg="#292e2e", fg="#d6d6d6")
        lbl.config(bg="#292e2e", fg="#d6d6d6")
        battery_label.config(bg="#292e2e", fg="#d6d6d6")

        # Change RHB frame configuration
        RHB.config(bg="#292e2e")
        # Change the background color of buttons in the RHB frame
        app1.config(bg="#292e2e")
        app2.config(bg="#292e2e")
        app3.config(bg="#292e2e")
        app4.config(bg="#292e2e")
        app5.config(bg="#292e2e")
        app6.config(bg="#292e2e")
        app7.config(bg="#292e2e")
        app8.config(bg="#292e2e")
        app9.config(bg="#292e2e")
        app10.config(bg="#292e2e")
        apps.config(bg="#292e2e", fg="#d6d6d6")

        # Change the background color of the parent widget/frame of volume
        volume.master.config(bg="#292e2e")

        # Change the battery icon color
        battery_label.config(bg="#292e2e", fg="#d6d6d6")

        # Update button_mode
        button_mode = False
    else:
        # Change LHS frame configuration
        LHS.config(bg="#f4f5f5")
        myimage.config(bg="#f4f5f5")
        l1.config(bg="#f4f5f5", fg="#292e2e")
        l2.config(bg="#f4f5f5", fg="#292e2e")
        l3.config(bg="#f4f5f5", fg="#292e2e")
        l4.config(bg="#f4f5f5", fg="#292e2e")
        l5.config(bg="#f4f5f5", fg="#292e2e")
        l6.config(bg="#f4f5f5", fg="#292e2e")

        # Change RHS frame configuration
        RHS.config(bg="#f4f5f5")
        # Change the background color of labels in the RHS frame
        system.config(bg="#f4f5f5", fg="#292e2e")
        lbl_speaker.config(bg="#f4f5f5", fg="#292e2e")
        lbl_plug.config(bg="#f4f5f5", fg="#292e2e")
        lbl_brightness.config(bg="#f4f5f5", fg="#292e2e")
        lbl_time.config(bg="#f4f5f5", fg="#292e2e")
        lbl.config(bg="#f4f5f5", fg="#292e2e")
        battery_label.config(bg="#f4f5f5", fg="#292e2e")

        # Change RHB frame configuration
        RHB.config(bg="#f4f5f5")
        # Change the background color of buttons in the RHB frame
        app1.config(bg="#f4f5f5")
        app2.config(bg="#f4f5f5")
        app3.config(bg="#f4f5f5")
        app4.config(bg="#f4f5f5")
        app5.config(bg="#f4f5f5")
        app6.config(bg="#f4f5f5")
        app7.config(bg="#f4f5f5")
        app8.config(bg="#f4f5f5")
        app9.config(bg="#f4f5f5")
        app10.config(bg="#f4f5f5")
        apps.config(bg="#f4f5f5", fg="#292e2e")

        # Change the background color of the parent widget/frame of volume
        volume.master.config(bg="#f4f5f5")

        # Change the battery icon color
        battery_label.config(bg="#f4f5f5", fg="#292e2e")

        # Update button_mode
        button_mode = True




def game():
    global canvas  # Make canvas global
    app5 = Tk()
    app5.title("Pong Game")
    app5.geometry("1000x800")
    app5.resizable(0, 0)
    app5.wm_attributes("-topmost", 1)
    canvas = Canvas(app5, width=1000, height=800, bd=1, highlightthickness=1) 
    canvas.config(bg="black")
    canvas.pack()
    l = canvas.create_text(500, 20, font=("Arial", 23, "bold"), text=" : ", fill="white")
    app5.update()
    canvas.create_line(500, 0, 500, 1000, fill="white")

    class Ball:
        def update(self):
            l.configure(text=str(self.score1) + ' : ' + str(self.score2))

        def __init__(self, canvas, paddle1, paddle2, color):
            self.paddle1 = paddle1
            self.paddle2 = paddle2
            self.canvas = canvas
            self.id = canvas.create_oval(20, 20, 50, 50, fill=color)
            self.canvas.move(self.id, 283, 300)
            starts = [-3, -2, -1, 1, 2, 3]
            random.shuffle(starts)
            self.x = starts[1]
            self.y = starts[2]
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.score1 = 0
            self.score2 = 0

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 4
            if pos[3] >= self.canvas_height:
                self.y = -4
            if pos[0] <= 0:
                self.x = 4
                self.score1 += 1
                print(self.score1)
                canvas.itemconfigure(l, text=str(self.score1) + " : " + str(self.score2))
            if pos[2] >= self.canvas_width:
                self.x = -4
                self.score2 += 1
                print(self.score2)
                canvas.itemconfigure(l, text=str(self.score1) + " : " + str(self.score2))
            if self.hit_paddle1(pos) == True:
                self.x = 4
            if self.hit_paddle2(pos) == True:
                self.x = -4

        def hit_paddle1(self, pos):
            paddle_pos = self.canvas.coords(self.paddle1.id)
            if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                    return True
                return False

        def hit_paddle2(self, pos):
            paddle_pos = self.canvas.coords(self.paddle2.id)
            if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                    return True
                return False

    class Paddle1:
        pos = [0, 0, 0, 0]

        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(10, 150, 45, 350, fill=color)
            self.y = 0
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('a', self.turn_left)
            self.canvas.bind_all('d', self.turn_right)

        def draw(self):
            self.canvas.move(self.id, 0, self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 0
            if pos[3] >= self.canvas_height:
                self.y = 0

        def turn_left(self, event):
            self.y = -4

        def turn_right(self, event):
            self.y = 4

    class Paddle2:
        pos = [0, 0, 0, 0]

        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(950, 150, 985, 350, fill=color)
            self.y = 0
            self.canvas_height = self.canvas.winfo_height()
            self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
            self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

        def draw(self):
            self.canvas.move(self.id, 0, self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 0
            if pos[3] >= self.canvas_height:
                self.y = 0

        def turn_left(self, event):
            self.y = 4

        def turn_right(self, event):
            self.y = -4

    middle_circle = canvas.create_oval(10, 10, 150, 150, outline="white")
    canvas.move(middle_circle, 420,300)

    paddle1 = Paddle1(canvas, "orange")
    paddle2 = Paddle2(canvas, "lightgreen")
    ball = Ball(canvas, paddle1, paddle2, "yellow")

    while True:
        if ball.score1 == 10 or ball.score2 == 10:
            messagebox.showinfo("Game Over", "Player 1 =" + str(ball.score1) + " Player 2 =" + str(ball.score2))
            break
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        app5.update_idletasks()
        app5.update()
        time.sleep(0.01)

    app5.mainloop()



#######################
    
def screenshot():
    root.iconify()
    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')

def crome():
    webview.create_window('Google.com', 'https://www.google.com/', width=775, height=520) 
    webview.start()

def close_apps():
    webview.create_window('Youtube.com','https://www.youtube.com/',width=775, height=520)
    webview.start()


def close_window():
    root.destroy()



# -----------------------------
RHB=Frame(Body,width=829,height=412,bg="#f4f5f5",highlightbackground="#abacb1",highlightthickness=1)
RHB.place(x=620,y=432)

apps=Label(RHB,text='Apps',font=('Acumin Variable Concept',15),bg='#f4f5f5')
apps.place(x=15,y=10)

app1_image=PhotoImage(file='Image/App1.png')
app1=Button(RHB,image=app1_image,bd=0,command=calculator)
app1.place(x=50,y=75)

app2_image=PhotoImage(file='Image/App2.png')
app2=Button(RHB,image=app2_image,bd=0,command=clock)
app2.place(x=200,y=75)

app3_image=PhotoImage(file='Image/App3.png')
app3=Button(RHB,image=app3_image,bd=0,command=calendar)
app3.place(x=350,y=75)

app4_image=PhotoImage(file='Image/App4.png')
app4=Button(RHB,image=app4_image,bd=0,command=mode)
app4.place(x=500,y=75)

app5_image=PhotoImage(file='Image/App5.png')
app5=Button(RHB,image=app5_image,bd=0,command=game)
app5.place(x=650,y=75)

app6_image=PhotoImage(file='Image/App6.png')
app6=Button(RHB,image=app6_image,bd=0,command=screenshot)
app6.place(x=50,y=240)

app7_image=PhotoImage(file='Image/App7.png')
app7=Button(RHB,image=app7_image,bd=0,command=file)
app7.place(x=200,y=240)

app8_image=PhotoImage(file='Image/App8.png')
app8=Button(RHB,image=app8_image,bd=0,command=crome)
app8.place(x=350,y=240)

app9_image=PhotoImage(file='Image/App9.png')
app9=Button(RHB,image=app9_image,bd=0,command=close_apps)
app9.place(x=500,y=240)

app10_image=PhotoImage(file='Image/App10.png')
app10=Button(RHB,image=app10_image,bd=0,command=close_window)
app10.place(x=650,y=240)


root.mainloop()
