import tkinter
from customtkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restart_time():
    os.system("shutdown /r /t 20")    

def log_out():
    os.system("shutdown -1")
    
def shut_down():
    os.system("shutdown /s /t 20")       

st = CTk()
st.title("Shut-Down App")
st.geometry("500x500")
st.config(bg="black")

r_button = CTkButton(st,
                                 width=120,
                                 height=42,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Restart",command=restart
                                 )
r_button.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

rt_button = CTkButton(st,
                                 width=120,
                                 height=42,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Restart Time", command=restart_time
                                 )
rt_button.place(relx=0.60, rely=0.30, anchor=tkinter.CENTER)

lg_button = CTkButton(st,
                                 width=120,
                                 height=42,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Log Out", command=log_out
                                 )
lg_button.place(relx=0.30, rely=0.60, anchor=tkinter.CENTER)

st_button = CTkButton(st,
                                 width=120,
                                 height=42,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Shut Down", command=shut_down
                                 )
st_button.place(relx=0.60, rely=0.60, anchor=tkinter.CENTER)

# new

simple_label = CTkLabel(st, text="Shut-Down Application", text_color="white", font=("Roboto",20) )
simple_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

st.mainloop()
